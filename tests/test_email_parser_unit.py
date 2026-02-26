import re
from datetime import datetime
from email_parser import (
    _normalize_month_day_to_date,
    _parse_time_on_date,
    extract_events_from_text,
    events_to_ics,
    parse_email_to_events,
)

def test_normalize_month_day_to_date():
    dt = _normalize_month_day_to_date("Feb", "24", reference_year=2026)
    assert dt.year == 2026
    assert dt.month == 2
    assert dt.day == 24

def test_parse_time_on_date():
    base = datetime(2026, 2, 24)
    dt = _parse_time_on_date(base, "11:30 am")
    assert dt.hour == 11
    assert dt.minute == 30
    assert dt.year == 2026
    assert dt.month == 2
    assert dt.day == 24

def test_extract_events_from_text():
    text = "Feb 24 @ 11:30 am – 3:00 pm | MU Ballroom | Register"
    events = extract_events_from_text(text)
    assert len(events) == 1
    ev = events[0]
    assert ev["location"] == "MU Ballroom"
    assert "register" in ev["tags"]
    assert ev["start"].hour == 11
    assert ev["end"].hour == 15

def test_events_to_ics():
    events = [{
        "id": "123",
        "title": "Sample Event",
        "start": datetime(2026, 2, 24, 11, 30),
        "end": datetime(2026, 2, 24, 12, 30),
        "location": "MU Ballroom",
        "description": "",
    }]
    ics = events_to_ics(events)
    assert "BEGIN:VEVENT" in ics
    assert "SUMMARY:Sample Event" in ics
    assert "LOCATION:MU Ballroom" in ics

def test_parse_email_to_events():
    text = """
    THIS WEEK
    Feb 24 @ 11:30 am – 3:00 pm | MU Ballroom
    """
    events = parse_email_to_events(text)
    assert len(events) == 1
    assert events[0]["title"] == "This Week"