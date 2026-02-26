from datetime import date, time
from event_sort import Event, sort_events


def test_system_end_to_end():
    events = [
        Event("Workshop", date(2026, 3, 12), time(14, 0), tags=["education"]),
        Event("Breakfast", date(2026, 3, 12), time(8, 0), tags=["food"]),
        Event("Team Meeting", date(2026, 3, 12), time(10, 0), tags=["work"]),
    ]

    # Sort by time → full pipeline
    sorted_events = sort_events(events, by="time")

    assert [e.name for e in sorted_events] == [
        "Breakfast",
        "Team Meeting",
        "Workshop",
    ]