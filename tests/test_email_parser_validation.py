from email_parser import extract_events_from_text

def test_extract_events_with_invalid_text():
    text = "No dates here, just random text."
    events = extract_events_from_text(text)
    assert events == []  # Should gracefully return empty list