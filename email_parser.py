"""
email_to_calendar.py

Parse Outlook-style college emails into calendar events and export to JSON or ICS.
"""

import re
from datetime import datetime, timedelta, time
from typing import List, Dict, Optional
from dateutil import parser as dateparser
import uuid

# --- Helpers -----------------------------------------------------------------

MONTH_NAME_RE = r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.?"
DATE_TIME_PATTERN = re.compile(
    rf"(?P<month>{MONTH_NAME_RE})\s*\.?\s*(?P<day>\d{{1,2}})\s*(?:@|\s+at\s+)\s*(?P<start>[\d:apm\s]+)\s*(?:–|-|to)\s*(?P<end>[\d:apm\s]+)\s*(?:\|\s*(?P<location>[^|]+))?",
    flags=re.IGNORECASE
)

SINGLE_TIME_PATTERN = re.compile(
    rf"(?P<month>{MONTH_NAME_RE})\s*\.?\s*(?P<day>\d{{1,2}})\s*(?:@|\s+at\s+)\s*(?P<start>[\d:apm\s]+)\s*(?:\|\s*(?P<location>[^|]+))?",
    flags=re.IGNORECASE
)

# Recognize headings that often separate sections
SECTION_HEADING_RE = re.compile(r"^(THIS WEEK|OF INTEREST|STAYING HEALTHY|INTERNS \+ HIRES WANTED|HAPPENING SOON|SHARE YOUR THOUGHTS|TRY THESE RESOURCES)$", re.IGNORECASE | re.MULTILINE)

# --- Core parsing functions --------------------------------------------------

def _normalize_month_day_to_date(month_str: str, day_str: str, reference_year: Optional[int] = None) -> datetime:
    """Return a date object for given month name and day, inferring year."""
    if reference_year is None:
        reference_year = datetime.now().year
    text = f"{month_str} {day_str} {reference_year}"
    try:
        dt = dateparser.parse(text)
    except Exception:
        # fallback: try without punctuation
        dt = dateparser.parse(f"{month_str} {day_str} {reference_year}")
    # If parsed date is earlier than today by more than 180 days, assume next year (handles Dec->Jan emails)
    now = datetime.now()
    if (dt - now).days < -180:
        dt = dt.replace(year=dt.year + 1)
    return dt

def _parse_time_on_date(base_date: datetime, time_str: str) -> datetime:
    """Parse a time string (e.g., '11:30 am') and attach to base_date."""
    # dateparser can parse times; combine with base_date's date
    time_str = time_str.strip().lower().replace(".", "")
    try:
        t = dateparser.parse(time_str)
    except Exception:
        t = None
    if t is None:
        # fallback: assume start of day
        return datetime.combine(base_date.date(), time(9, 0))
    return datetime.combine(base_date.date(), t.time())

def extract_events_from_text(email_text: str) -> List[Dict]:
    """
    Scan the email text and extract events.
    Returns a list of event dicts with keys: title, start, end, location, description, tags.
    """
    events = []
    lines = [ln.strip() for ln in email_text.splitlines() if ln.strip()]
    # Join lines to allow multi-line event lines
    joined = " | ".join(lines)

    # First pass: find explicit date ranges like "Feb. 24 @ 11:30 am – 3:00 pm | MU Ballroom | Register"
    for m in DATE_TIME_PATTERN.finditer(joined):
        month = m.group("month")
        day = m.group("day")
        start_str = m.group("start")
        end_str = m.group("end")
        location = (m.group("location") or "").strip()
        base_date = _normalize_month_day_to_date(month, day)
        start_dt = _parse_time_on_date(base_date, start_str)
        end_dt = _parse_time_on_date(base_date, end_str)
        # If end is earlier than start, assume it crosses to next day
        if end_dt <= start_dt:
            end_dt += timedelta(days=1)

        # Heuristic: find a title preceding this match within a short window
        prefix = joined[:m.start()]
        # split by '|' and take last non-empty chunk as title candidate
        title_candidate = None
        parts = [p.strip() for p in prefix.split("|") if p.strip()]
        if parts:
            title_candidate = parts[-1]
            # avoid picking section headings
            if SECTION_HEADING_RE.search(title_candidate):
                title_candidate = None

        title = title_candidate or "Event"
        description = ""
        tags = []
        if "Register" in joined[m.start():m.end()+200]:
            tags.append("register")
        if "Hiring" in joined[m.start():m.end()+200] or "Hiring!" in joined[m.start():m.end()+200]:
            tags.append("hiring")
        if "Food" in joined[m.start():m.end()+200]:
            tags.append("food")

        events.append({
            "id": str(uuid.uuid4()),
            "title": title,
            "start": start_dt,
            "end": end_dt,
            "location": location,
            "description": description,
            "tags": tags,
            "source_excerpt": joined[m.start():m.end()+200][:300]
        })

    # Second pass: single-time events (no end time)
    for m in SINGLE_TIME_PATTERN.finditer(joined):
        # skip if already captured by range pattern (overlap)
        if any(m.start() >= (e["start"].timestamp() if isinstance(e["start"], float) else 0) for e in events):
            pass
        month = m.group("month")
        day = m.group("day")
        start_str = m.group("start")
        location = (m.group("location") or "").strip()
        base_date = _normalize_month_day_to_date(month, day)
        start_dt = _parse_time_on_date(base_date, start_str)
        end_dt = start_dt + timedelta(hours=1)  # default 1 hour
        title = "Event"
        events.append({
            "id": str(uuid.uuid4()),
            "title": title,
            "start": start_dt,
            "end": end_dt,
            "location": location,
            "description": "",
            "tags": [],
            "source_excerpt": joined[m.start():m.end()+200][:300]
        })

    # Final cleanup: sort by start
    events = sorted(events, key=lambda e: e["start"])
    return events

# --- Export helpers ----------------------------------------------------------

def _format_dt_ics(dt: datetime) -> str:
    """Format datetime to ICS UTC naive format (YYYYMMDDTHHMMSS)."""
    return dt.strftime("%Y%m%dT%H%M%S")

def events_to_ics(events: List[Dict], calendar_name: str = "Imported Events") -> str:
    """Convert events list to a simple ICS calendar string."""
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        f"PRODID:-//email-to-calendar//{calendar_name}//EN"
    ]
    for ev in events:
        uid = ev.get("id", str(uuid.uuid4()))
        dtstamp = _format_dt_ics(datetime.utcnow())
        dtstart = _format_dt_ics(ev["start"])
        dtend = _format_dt_ics(ev["end"])
        summary = ev["title"].replace("\n", " ")
        location = ev.get("location", "")
        description = ev.get("description", "")
        lines += [
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTAMP:{dtstamp}Z",
            f"DTSTART:{dtstart}",
            f"DTEND:{dtend}",
            f"SUMMARY:{summary}",
            f"LOCATION:{location}",
            f"DESCRIPTION:{description}",
            "END:VEVENT"
        ]
    lines.append("END:VCALENDAR")
    return "\r\n".join(lines)

# --- Public API --------------------------------------------------------------

def parse_email_to_events(email_text: str) -> List[Dict]:
    """
    Main entry point: parse email text and return structured events.
    Each event dict contains:
      - id, title, start (datetime), end (datetime), location, description, tags
    """
    events = extract_events_from_text(email_text)
    # Post-process titles: if title is generic, try to extract nearby heading
    # (simple heuristic: look for uppercase phrases in the email)
    headings = re.findall(r"^[A-Z0-9 \-&']{4,}$", email_text, flags=re.MULTILINE)
    for ev in events:
        if ev["title"] == "Event":
            # try to assign a heading
            if headings:
                ev["title"] = headings[0].title()
    return events

