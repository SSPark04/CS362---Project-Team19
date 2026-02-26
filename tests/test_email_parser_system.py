from email_to_calendar import parse_email_to_events, events_to_ics

def test_system_end_to_end():
    email = """
    HAPPENING SOON
    Feb 24 @ 11:30 am – 3:00 pm | MU Ballroom | Register
    """

    events = parse_email_to_events(email)
    assert len(events) == 1
    ev = events[0]

    # Check parsed event fields
    assert ev["title"] == "Happening Soon"
    assert ev["location"] == "MU Ballroom"
    assert "register" in ev["tags"]

    # Convert to ICS
    ics = events_to_ics(events)
    assert "BEGIN:VCALENDAR" in ics
    assert "SUMMARY:Happening Soon" in ics