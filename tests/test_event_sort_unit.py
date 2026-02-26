import pytest
from datetime import date, time
from event_sort import Event, sort_events


def test_event_dataclass():
    ev = Event(
        name="Meeting",
        date=date(2026, 3, 12),
        time=time(14, 0),
        tags=["work"]
    )
    assert ev.name == "Meeting"
    assert ev.date == date(2026, 3, 12)
    assert ev.time == time(14, 0)
    assert ev.tags == ["work"]


def test_sort_by_name():
    e1 = Event("Zeta", date(2026, 3, 12), time(10, 0))
    e2 = Event("Alpha", date(2026, 3, 12), time(11, 0))
    sorted_events = sort_events([e1, e2], by="name")
    assert [e.name for e in sorted_events] == ["Alpha", "Zeta"]


def test_sort_by_date():
    e1 = Event("A", date(2026, 3, 15), time(10, 0))
    e2 = Event("B", date(2026, 3, 10), time(10, 0))
    sorted_events = sort_events([e1, e2], by="date")
    assert [e.date for e in sorted_events] == [date(2026, 3, 10), date(2026, 3, 15)]


def test_sort_by_time():
    e1 = Event("A", date(2026, 3, 12), time(15, 0))
    e2 = Event("B", date(2026, 3, 12), time(9, 0))
    sorted_events = sort_events([e1, e2], by="time")
    assert [e.time for e in sorted_events] == [time(9, 0), time(15, 0)]


def test_sort_by_tags_with_specific_tag():
    e1 = Event("A", date(2026, 3, 12), time(10, 0), tags=["fun"])
    e2 = Event("B", date(2026, 3, 12), time(10, 0), tags=["work", "fun"])
    e3 = Event("C", date(2026, 3, 12), time(10, 0), tags=["work"])

    sorted_events = sort_events([e1, e2, e3], by="tags", tag="work")

    # Events with "work" should come first
    assert [e.name for e in sorted_events] == ["B", "C", "A"]


def test_sort_by_tags_default():
    e1 = Event("A", date(2026, 3, 12), time(10, 0), tags=["zeta"])
    e2 = Event("B", date(2026, 3, 12), time(10, 0), tags=["alpha"])
    e3 = Event("C", date(2026, 3, 12), time(10, 0), tags=[])

    sorted_events = sort_events([e1, e2, e3], by="tags")

    # Empty tags come first because [""] < ["alpha"]
    assert [e.name for e in sorted_events] == ["C", "B", "A"]