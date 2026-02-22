"""
Tests for routes.py (API endpoint integration tests).
Uses Flask's built-in test client.
"""

import json
import os
import sys
import pytest

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import data_manager
from app import app


# --- Fixtures ---

@pytest.fixture
def client():
    """
    Create a Flask test client for sending requests.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


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
def sample_events(temp_data_dir):
    """
    Create sample events in the temp data file.
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
    data_manager.save_events(events)
    return events


# --- Tests for GET /api/events ---

class TestGetEvents:

    def test_get_all_events(self, client, sample_events):
        """
        GET /api/events should return all events.
        """
        response = client.get("/api/events")
        assert response.status_code == 200

        data = response.get_json()
        assert len(data) == 3

    def test_get_events_empty(self, client, temp_data_dir):
        """
        GET /api/events should return empty list when no events exist.
        """
        response = client.get("/api/events")
        assert response.status_code == 200

        data = response.get_json()
        assert data == []

    def test_get_events_sorted_by_title(self, client, sample_events):
        """
        GET /api/events?sort=title should return events sorted by title.
        """
        response = client.get("/api/events?sort=title")
        assert response.status_code == 200

        data = response.get_json()
        titles = [e["title"] for e in data]
        assert titles == ["Alumni Talk", "Career Fair", "Python Workshop"]

    def test_get_events_sorted_desc(self, client, sample_events):
        """
        GET /api/events?sort=title&order=desc should return reverse sorted.
        """
        response = client.get("/api/events?sort=title&order=desc")
        assert response.status_code == 200

        data = response.get_json()
        titles = [e["title"] for e in data]
        assert titles == ["Python Workshop", "Career Fair", "Alumni Talk"]

    def test_get_events_filter_by_range(self, client, sample_events):
        """
        GET /api/events?start=...&end=... should filter by date range.
        """
        response = client.get("/api/events?start=2026-02-10&end=2026-02-15")
        assert response.status_code == 200

        data = response.get_json()
        assert len(data) == 2
        titles = [e["title"] for e in data]
        assert "Career Fair" not in titles


# --- Tests for GET /api/events/<id> ---

class TestGetEventById:

    def test_get_existing_event(self, client, sample_events):
        """
        GET /api/events/evt-001 should return the event.
        """
        response = client.get("/api/events/evt-001")
        assert response.status_code == 200

        data = response.get_json()
        assert data["title"] == "Python Workshop"

    def test_get_nonexistent_event(self, client, sample_events):
        """
        GET /api/events/evt-zzz should return 404.
        """
        response = client.get("/api/events/evt-zzz")
        assert response.status_code == 404

        data = response.get_json()
        assert "error" in data


# --- Tests for POST /api/events ---

class TestCreateEvent:

    def test_create_valid_event(self, client, temp_data_dir):
        """
        POST /api/events with valid data should return 201.
        """
        new_event = {
            "title": "New Event",
            "description": "A brand new event.",
            "date": "2026-03-01",
            "start_time": "10:00",
            "end_time": "11:00",
            "building": "KEC",
            "room": "1001",
            "latitude": 0,
            "longitude": 0
        }
        response = client.post(
            "/api/events",
            data=json.dumps(new_event),
            content_type="application/json"
        )
        assert response.status_code == 201

        data = response.get_json()
        assert data["title"] == "New Event"
        assert "event_id" in data

    def test_create_invalid_event(self, client, temp_data_dir):
        """
        POST /api/events with missing fields should return 400.
        """
        bad_event = {
            "title": "Missing Fields"
        }
        response = client.post(
            "/api/events",
            data=json.dumps(bad_event),
            content_type="application/json"
        )
        assert response.status_code == 400

        data = response.get_json()
        assert "error" in data

    def test_create_event_no_json_body(self, client, temp_data_dir):
        """
        POST /api/events without JSON body should return 400.
        """
        response = client.post("/api/events")
        assert response.status_code == 400


# --- Tests for PUT /api/events/<id> ---

class TestUpdateEvent:

    def test_update_existing_event(self, client, sample_events):
        """
        PUT /api/events/evt-001 with valid data should return 200.
        """
        updates = {"title": "Updated Workshop"}
        response = client.put(
            "/api/events/evt-001",
            data=json.dumps(updates),
            content_type="application/json"
        )
        assert response.status_code == 200

        data = response.get_json()
        assert data["title"] == "Updated Workshop"

    def test_update_nonexistent_event(self, client, sample_events):
        """
        PUT /api/events/evt-zzz should return 404.
        """
        updates = {"title": "Nope"}
        response = client.put(
            "/api/events/evt-zzz",
            data=json.dumps(updates),
            content_type="application/json"
        )
        assert response.status_code == 404

    def test_update_with_invalid_data(self, client, sample_events):
        """
        PUT /api/events/evt-001 with invalid date should return 404.
        """
        updates = {"date": "bad-date"}
        response = client.put(
            "/api/events/evt-001",
            data=json.dumps(updates),
            content_type="application/json"
        )
        assert response.status_code == 404

        data = response.get_json()
        assert "error" in data


# --- Tests for DELETE /api/events/<id> ---

class TestDeleteEvent:

    def test_delete_existing_event(self, client, sample_events):
        """
        DELETE /api/events/evt-001 should return 200.
        """
        response = client.delete("/api/events/evt-001")
        assert response.status_code == 200

        data = response.get_json()
        assert data["message"] == "deleted"

        # Verify it's gone
        response2 = client.get("/api/events/evt-001")
        assert response2.status_code == 404

    def test_delete_nonexistent_event(self, client, sample_events):
        """
        DELETE /api/events/evt-zzz should return 404.
        """
        response = client.delete("/api/events/evt-zzz")
        assert response.status_code == 404

        data = response.get_json()
        assert "error" in data
