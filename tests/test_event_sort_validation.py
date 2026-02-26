import pytest
from datetime import date, time
from event_sort import Event, sort_events


def test_invalid_sort_key():
    e = Event("Test", date(2026, 3, 12), time(10, 0))
    with pytest.raises(ValueError):
        sort_events([e], by="unknown_key")