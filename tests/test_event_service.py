"""
Tests for event_service.py
"""

import json
import os
import sys
import pytest

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import data_manager
import event_service


# --- Fixtures ---

@pytest.fixture
def temp_data_dir(tmp_path):
    """
    Override data_manager paths to use a temporary directory.
    """
    original_dir = data_manager.DATA_DIR
    original_file = data_manager.EVENTS_FILE

    test_dir = str(tmp_path / "data")
    os.makedirs(test_dir, exist_ok=True)

    data_manager.DATA_DIR = test_dir
    data_manager.EVENTS_FILE = os.path.join(test_dir, "events.json")

    yield test_dir

    data_manager.DATA_DIR = original_dir
    data_manager.EVENTS_FILE = original_file


@pytest.fixture
def valid_event():
    """
    A valid event dict.
    """
    return {
        "title": "Test Event",
        "description": "Description here.",
        "date": "2026-03-01",
        "start_time": "10:00",
        "end_time": "11:00",
        "building": "KEC",
        "room": "1001",
        "latitude": 0,
        "longitude": 0
    }


@pytest.fixture
def sample_events_file(temp_data_dir):
    """
    Create a JSON file with 3 sample events for filter/sort testing.
    """
    events = [
        {
            "event_id": "evt-001",
            "title": "Python Workshop",
            "description": "Learn Python basics.",
            "date": "2026-02-10",
            "start_time": "14:00",
            "end_time": "15:00",
            "building": "KEC",
            "room": "1001",
            "latitude": 0,
            "longitude": 0
        },
        {
            "event_id": "evt-002",
            "title": "Alumni Talk",
            "description": "Alumni sharing experience.",
            "date": "2026-02-12",
            "start_time": "09:00",
            "end_time": "10:30",
            "building": "MU",
            "room": "Ballroom",
            "latitude": 0,
            "longitude": 0
        },
        {
            "event_id": "evt-003",
            "title": "Career Fair",
            "description": "Meet employers.",
            "date": "2026-02-20",
            "start_time": "10:00",
            "end_time": "16:00",
            "building": "CH2M",
            "room": "",
            "latitude": 0,
            "longitude": 0
        }
    ]
    file_path = os.path.join(temp_data_dir, "events.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(events, f)

    return events


# --- Tests for validate_event ---

class TestValidateEvent:

    def test_valid_event_passes(self, valid_event):
        """
        A complete and correct event should pass validation.
        """
        is_valid, error = event_service.validate_event(valid_event)
        assert is_valid is True
        assert error == ""

    def test_missing_title_fails(self, valid_event):
        """
        Missing 'title' should fail.
        """
        del valid_event["title"]
        is_valid, error = event_service.validate_event(valid_event)
        assert is_valid is False
        assert "title" in error

    def test_missing_date_fails(self, valid_event):
        """
        Missing 'date' should fail.
        """
        del valid_event["date"]
        is_valid, error = event_service.validate_event(valid_event)
        assert is_valid is False
        assert "date" in error

    def test_empty_building_fails(self, valid_event):
        """
        An empty string for 'building' should fail.
        """
        valid_event["building"] = ""
        is_valid, error = event_service.validate_event(valid_event)
        assert is_valid is False
        assert "building" in error

    def test_bad_date_format_fails(self, valid_event):
        """
        A date not in YYYY-MM-DD format should fail.
        """
        valid_event["date"] = "March 1, 2026"
        is_valid, error = event_service.validate_event(valid_event)
        assert is_valid is False
        assert "date" in error.lower()

    def test_bad_time_format_fails(self, valid_event):
        """
        A time not in HH:MM format should fail.
        """
        valid_event["start_time"] = "10am"
        is_valid, error = event_service.validate_event(valid_event)
        assert is_valid is False
        assert "start_time" in error

    def test_end_before_start_fails(self, valid_event):
        """
        end_time earlier than start_time should fail.
        """
        valid_event["start_time"] = "14:00"
        valid_event["end_time"] = "13:00"
        is_valid, error = event_service.validate_event(valid_event)
        assert is_valid is False
        assert "end_time" in error

    def test_same_start_and_end_fails(self, valid_event):
        """
        Same start and end time should fail.
        """
        valid_event["start_time"] = "10:00"
        valid_event["end_time"] = "10:00"
        is_valid, error = event_service.validate_event(valid_event)
        assert is_valid is False


# --- Tests for create_event ---

class TestCreateEvent:

    def test_create_valid_event(self, temp_data_dir, valid_event):
        """
        A valid event should be created and saved.
        """
        event, error = event_service.create_event(valid_event)
        assert event is not None
        assert error == ""
        assert "event_id" in event

    def test_create_invalid_event_returns_error(self, temp_data_dir):
        """
        An invalid event should not be created.
        """
        bad_event = {"title": "No Date Event", "building": "KEC"}
        event, error = event_service.create_event(bad_event)
        assert event is None
        assert error != ""


# --- Tests for update_event ---

class TestUpdateEvent:

    def test_update_valid_fields(self, temp_data_dir, sample_events_file):
        """
        Updating with valid data should succeed.
        """
        event, error = event_service.update_event("evt-001", {"title": "Updated Workshop"})
        assert event is not None
        assert error == ""
        assert event["title"] == "Updated Workshop"

    def test_update_with_invalid_data_fails(self, temp_data_dir, sample_events_file):
        """
        Updating with invalid data should be rejected.
        """
        event, error = event_service.update_event("evt-001", {"date": "bad-date"})
        assert event is None
        assert error != ""

    def test_update_nonexistent_event(self, temp_data_dir, sample_events_file):
        """
        Updating a missing event should return an error.
        """
        event, error = event_service.update_event("evt-zzz", {"title": "Nope"})
        assert event is None
        assert "not found" in error.lower()


# --- Tests for delete_event ---

class TestDeleteEvent:

    def test_delete_existing(self, temp_data_dir, sample_events_file):
        """
        Deleting an existing event should return True.
        """
        result = event_service.delete_event("evt-001")
        assert result is True

    def test_delete_nonexistent(self, temp_data_dir, sample_events_file):
        """
        Deleting a missing event should return False.
        """
        result = event_service.delete_event("evt-zzz")
        assert result is False


# --- Tests for filter_events_by_date ---

class TestFilterEventsByDate:

    def test_filter_by_range_returns_matching(self, temp_data_dir, sample_events_file):
        """
        Events within the date range should be returned.
        """
        results = event_service.filter_events_by_date(
            "range",
            start_date="2026-02-10",
            end_date="2026-02-15"
        )
        assert len(results) == 2
        titles = [e["title"] for e in results]
        assert "Python Workshop" in titles
        assert "Alumni Talk" in titles

    def test_filter_by_range_excludes_outside(self, temp_data_dir, sample_events_file):
        """
        Events outside the date range should not be returned.
        """
        results = event_service.filter_events_by_date(
            "range",
            start_date="2026-02-10",
            end_date="2026-02-15"
        )
        titles = [e["title"] for e in results]
        assert "Career Fair" not in titles

    def test_filter_by_range_invalid_dates(self, temp_data_dir, sample_events_file):
        """
        If start > end, return empty list.
        """
        results = event_service.filter_events_by_date(
            "range",
            start_date="2026-03-01",
            end_date="2026-02-01"
        )
        assert results == []

    def test_filter_unknown_type_returns_all(self, temp_data_dir, sample_events_file):
        """
        An unknown filter type should return all events.
        """
        results = event_service.filter_events_by_date("unknown")
        assert len(results) == 3


# --- Tests for sort_events ---

class TestSortEvents:

    def test_sort_by_title(self, temp_data_dir, sample_events_file):
        """
        Events should be sorted alphabetically by title.
        """
        events = data_manager.load_events()
        sorted_events = event_service.sort_events(events, "title")
        titles = [e["title"] for e in sorted_events]
        assert titles == ["Alumni Talk", "Career Fair", "Python Workshop"]

    def test_sort_by_title_reverse(self, temp_data_dir, sample_events_file):
        """
        Reverse sort by title should be Z to A.
        """
        events = data_manager.load_events()
        sorted_events = event_service.sort_events(events, "title", reverse=True)
        titles = [e["title"] for e in sorted_events]
        assert titles == ["Python Workshop", "Career Fair", "Alumni Talk"]

    def test_sort_by_date(self, temp_data_dir, sample_events_file):
        """
        Events should be sorted by date ascending.
        """
        events = data_manager.load_events()
        sorted_events = event_service.sort_events(events, "date")
        dates = [e["date"] for e in sorted_events]
        assert dates == ["2026-02-10", "2026-02-12", "2026-02-20"]

    def test_sort_by_start_time(self, temp_data_dir, sample_events_file):
        """
        Events should be sorted by start_time ascending.
        """
        events = data_manager.load_events()
        sorted_events = event_service.sort_events(events, "start_time")
        times = [e["start_time"] for e in sorted_events]
        assert times == ["09:00", "10:00", "14:00"]

    def test_sort_by_unknown_field_returns_same_order(self, temp_data_dir, sample_events_file):
        """
        Unknown sort field should return events in original order.
        """
        events = data_manager.load_events()
        sorted_events = event_service.sort_events(events, "unknown_field")
        assert len(sorted_events) == len(events)
