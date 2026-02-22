"""
Tests for data_manager.py
"""

import json
import os
import sys
import pytest

# Add the project root to the path so we can import data_manager
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import data_manager


# --- Fixtures ---

@pytest.fixture
def temp_data_dir(tmp_path):
    """
    Override data_manager paths to use a temporary directory.
    This prevents tests from touching the real events.json file.
    """
    original_dir = data_manager.DATA_DIR
    original_file = data_manager.EVENTS_FILE

    test_dir = str(tmp_path / "data")
    os.makedirs(test_dir, exist_ok=True)

    data_manager.DATA_DIR = test_dir
    data_manager.EVENTS_FILE = os.path.join(test_dir, "events.json")

    yield test_dir

    # Restore original paths after test
    data_manager.DATA_DIR = original_dir
    data_manager.EVENTS_FILE = original_file


@pytest.fixture
def sample_event():
    """
    A sample event dict (without event_id).
    """
    return {
        "title": "Test Event",
        "description": "A test event for unit testing.",
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
    Create a JSON file with 2 sample events already in it.
    """
    events = [
        {
            "event_id": "evt-aaa",
            "title": "Event A",
            "description": "First event.",
            "date": "2026-02-10",
            "start_time": "09:00",
            "end_time": "10:00",
            "building": "KEC",
            "room": "1001",
            "latitude": 0,
            "longitude": 0
        },
        {
            "event_id": "evt-bbb",
            "title": "Event B",
            "description": "Second event.",
            "date": "2026-02-15",
            "start_time": "14:00",
            "end_time": "15:00",
            "building": "MU",
            "room": "Ballroom",
            "latitude": 0,
            "longitude": 0
        }
    ]
    file_path = os.path.join(temp_data_dir, "events.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(events, f)

    return events


# --- Tests for load_events ---

class TestLoadEvents:

    def test_load_returns_empty_list_when_no_file(self, temp_data_dir):
        """
        If events.json doesn't exist, return an empty list.
        """
        result = data_manager.load_events()
        assert result == []

    def test_load_returns_events_from_file(self, temp_data_dir, sample_events_file):
        """
        If events.json exists, return the list of events.
        """
        result = data_manager.load_events()
        assert len(result) == 2
        assert result[0]["title"] == "Event A"
        assert result[1]["title"] == "Event B"


# --- Tests for save_events ---

class TestSaveEvents:

    def test_save_creates_file(self, temp_data_dir):
        """
        save_events should create the JSON file.
        """
        events = [{"event_id": "evt-001", "title": "Saved Event"}]
        data_manager.save_events(events)

        file_path = os.path.join(temp_data_dir, "events.json")
        assert os.path.exists(file_path)

        with open(file_path, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        assert len(loaded) == 1
        assert loaded[0]["title"] == "Saved Event"

    def test_save_overwrites_existing_file(self, temp_data_dir, sample_events_file):
        """
        save_events should replace the old data.
        """
        new_events = [{"event_id": "evt-new", "title": "New Event"}]
        data_manager.save_events(new_events)

        result = data_manager.load_events()
        assert len(result) == 1
        assert result[0]["title"] == "New Event"


# --- Tests for get_event_by_id ---

class TestGetEventById:

    def test_find_existing_event(self, temp_data_dir, sample_events_file):
        """
        Should return the event when ID matches.
        """
        result = data_manager.get_event_by_id("evt-aaa")
        assert result is not None
        assert result["title"] == "Event A"

    def test_return_none_for_missing_id(self, temp_data_dir, sample_events_file):
        """
        Should return None when ID does not exist.
        """
        result = data_manager.get_event_by_id("evt-zzz")
        assert result is None


# --- Tests for add_event ---

class TestAddEvent:

    def test_add_event_assigns_id(self, temp_data_dir, sample_event):
        """
        add_event should assign an event_id to the new event.
        """
        result = data_manager.add_event(sample_event)
        assert "event_id" in result
        assert result["event_id"].startswith("evt-")

    def test_add_event_saves_to_file(self, temp_data_dir, sample_event):
        """
        The new event should appear when loading events.
        """
        data_manager.add_event(sample_event)
        events = data_manager.load_events()
        assert len(events) == 1
        assert events[0]["title"] == "Test Event"

    def test_add_event_appends_to_existing(self, temp_data_dir, sample_events_file, sample_event):
        """
        Adding to an existing file should not overwrite old events.
        """
        data_manager.add_event(sample_event)
        events = data_manager.load_events()
        assert len(events) == 3


# --- Tests for update_event ---

class TestUpdateEvent:

    def test_update_existing_event(self, temp_data_dir, sample_events_file):
        """
        Should update the specified fields.
        """
        result = data_manager.update_event("evt-aaa", {"title": "Updated A"})
        assert result is not None
        assert result["title"] == "Updated A"

        # Verify it's saved
        loaded = data_manager.get_event_by_id("evt-aaa")
        assert loaded["title"] == "Updated A"

    def test_update_does_not_change_other_events(self, temp_data_dir, sample_events_file):
        """
        Other events should not be affected.
        """
        data_manager.update_event("evt-aaa", {"title": "Updated A"})
        other = data_manager.get_event_by_id("evt-bbb")
        assert other["title"] == "Event B"

    def test_update_returns_none_for_missing_id(self, temp_data_dir, sample_events_file):
        """
        Should return None when the event doesn't exist.
        """
        result = data_manager.update_event("evt-zzz", {"title": "Nope"})
        assert result is None


# --- Tests for delete_event ---

class TestDeleteEvent:

    def test_delete_existing_event(self, temp_data_dir, sample_events_file):
        """
        Should remove the event and return True.
        """
        result = data_manager.delete_event("evt-aaa")
        assert result is True

        events = data_manager.load_events()
        assert len(events) == 1
        assert events[0]["event_id"] == "evt-bbb"

    def test_delete_returns_false_for_missing_id(self, temp_data_dir, sample_events_file):
        """
        Should return False when event doesn't exist.
        """
        result = data_manager.delete_event("evt-zzz")
        assert result is False

        events = data_manager.load_events()
        assert len(events) == 2


# --- Tests for generate_event_id ---

class TestGenerateEventId:

    def test_id_starts_with_evt(self):
        """
        Generated IDs should start with 'evt-'.
        """
        new_id = data_manager.generate_event_id()
        assert new_id.startswith("evt-")

    def test_ids_are_unique(self):
        """
        Two generated IDs should not be the same.
        """
        id1 = data_manager.generate_event_id()
        id2 = data_manager.generate_event_id()
        assert id1 != id2
