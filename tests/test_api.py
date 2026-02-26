import json
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import data_manager
from app import app


# ── Fixtures ──────────────────────────────────

SAMPLE_EVENTS = [
    {
        "event_id": "evt-001",
        "title": "Career Fair",
        "description": "EECS industry career fair",
        "date": "2026-03-10",
        "start_time": "10:00",
        "end_time": "14:00",
        "building": "CH2M",
        "room": "104",
        "latitude": 44.5646,
        "longitude": -123.2620,
    },
    {
        "event_id": "evt-002",
        "title": "Alumni Talk",
        "description": "Alumni sharing experience",
        "date": "2026-03-12",
        "start_time": "09:00",
        "end_time": "10:30",
        "building": "MU",
        "room": "Ballroom",
        "latitude": 44.5651,
        "longitude": -123.2765,
    },
    {
        "event_id": "evt-003",
        "title": "Python Workshop",
        "description": "Intro to Python for EECS students",
        "date": "2026-03-15",
        "start_time": "14:00",
        "end_time": "16:00",
        "building": "KEC",
        "room": "1007",
        "latitude": 44.5670,
        "longitude": -123.2750,
    },
]


@pytest.fixture
def client(tmp_path, monkeypatch):
    path = tmp_path / "events.json"
    path.write_text(json.dumps(SAMPLE_EVENTS), encoding="utf-8")
    monkeypatch.setattr(data_manager, "EVENTS_FILE", str(path))

    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def post_json(client, url, data):
    return client.post(url, data=json.dumps(data), content_type="application/json")


def put_json(client, url, data):
    return client.put(url, data=json.dumps(data), content_type="application/json")


# ══════════════════════════════════════════════
# UNIT TESTS
# One test per main function in api.js
# ══════════════════════════════════════════════

def test_getEvents(client):
    """getEvents() — GET /api/events returns all events."""
    resp = client.get("/api/events")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 3


def test_getEventById(client):
    """getEventById() — GET /api/events/<id> returns correct event."""
    resp = client.get("/api/events/evt-001")
    assert resp.status_code == 200
    assert resp.get_json()["title"] == "Career Fair"


def test_createEvent(client):
    """createEvent() — POST /api/events creates a new event and returns 201."""
    new_event = {
        "title": "New Seminar",
        "date": "2026-04-01",
        "start_time": "10:00",
        "end_time": "11:00",
        "building": "KEC",
    }
    resp = post_json(client, "/api/events", new_event)
    assert resp.status_code == 201
    assert "event_id" in resp.get_json()


def test_updateEvent(client):
    """updateEvent() — PUT /api/events/<id> updates and returns the event."""
    resp = put_json(client, "/api/events/evt-001", {"title": "Updated Career Fair"})
    assert resp.status_code == 200
    assert resp.get_json()["title"] == "Updated Career Fair"


def test_deleteEvent(client):
    """deleteEvent() — DELETE /api/events/<id> removes the event."""
    resp = client.delete("/api/events/evt-001")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "deleted"


def test_getTodaysEvents(client):
    """getTodaysEvents() — GET /api/events?filter=today&sort=start_time&order=asc returns 200."""
    resp = client.get("/api/events?filter=today&sort=start_time&order=asc")
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), list)


def test_getWeekEvents(client):
    """getWeekEvents() — GET /api/events?filter=week&sort=date&order=asc returns 200."""
    resp = client.get("/api/events?filter=week&sort=date&order=asc")
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), list)


def test_getEventsByRange(client):
    """getEventsByRange() — GET /api/events?start=...&end=...&sort=date&order=asc returns matching events."""
    resp = client.get("/api/events?start=2026-03-10&end=2026-03-12&sort=date&order=asc")
    assert resp.status_code == 200
    events = resp.get_json()
    assert len(events) == 2
    assert events[0]["date"] <= events[1]["date"]


# ══════════════════════════════════════════════
# VALIDATION TESTS
# One test per high-level use-case
# ══════════════════════════════════════════════

def test_validation_create_event_missing_fields(client):
    """Use-case: event creation — missing required fields should return 400."""
    resp = post_json(client, "/api/events", {"title": "No Date"})
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_validation_create_event_bad_date_format(client):
    """Use-case: event creation — invalid date format should return 400."""
    resp = post_json(client, "/api/events", {
        "title": "Bad Date",
        "date": "March 10 2026",
        "start_time": "10:00",
        "end_time": "11:00",
        "building": "KEC",
    })
    assert resp.status_code == 400


def test_validation_get_event_not_found(client):
    """Use-case: event retrieval — unknown ID should return 404."""
    resp = client.get("/api/events/evt-does-not-exist")
    assert resp.status_code == 404
    assert "error" in resp.get_json()


def test_validation_update_event_not_found(client):
    """Use-case: event update — unknown ID should return 404."""
    resp = put_json(client, "/api/events/evt-ghost", {"title": "Ghost"})
    assert resp.status_code == 404


def test_validation_delete_event_not_found(client):
    """Use-case: event deletion — unknown ID should return 404."""
    resp = client.delete("/api/events/evt-ghost")
    assert resp.status_code == 404


def test_validation_filter_invalid_range(client):
    """Use-case: event filtering — range with no results should return empty list."""
    resp = client.get("/api/events?start=2020-01-01&end=2020-01-31")
    assert resp.status_code == 200
    assert resp.get_json() == []


# ══════════════════════════════════════════════
# INTEGRATION TEST
# Invokes routes → event_service → data_manager together
# ══════════════════════════════════════════════

def test_integration_create_then_retrieve(client):
    """
    createEvent() then getEventById() — verifies the full pipeline:
    routes.py → event_service.py → data_manager.py (write then read).
    """
    new_event = {
        "title": "Integration Test Event",
        "date": "2026-05-01",
        "start_time": "13:00",
        "end_time": "14:00",
        "building": "Owen",
    }
    create_resp = post_json(client, "/api/events", new_event)
    assert create_resp.status_code == 201
    event_id = create_resp.get_json()["event_id"]

    get_resp = client.get(f"/api/events/{event_id}")
    assert get_resp.status_code == 200
    assert get_resp.get_json()["title"] == "Integration Test Event"


# ══════════════════════════════════════════════
# SYSTEM TEST
# Tests the full app end-to-end in a clean environment
# ══════════════════════════════════════════════

def test_system_full_crud_workflow(client):
    """
    Full CRUD cycle in a clean environment:
    Create → Read → Update → Delete → Confirm gone.
    Simulates the complete workflow a user would trigger via api.js.
    """
    # Create
    create_resp = post_json(client, "/api/events", {
        "title": "System Test Event",
        "date": "2026-08-01",
        "start_time": "11:00",
        "end_time": "12:00",
        "building": "Bexell",
    })
    assert create_resp.status_code == 201
    event_id = create_resp.get_json()["event_id"]

    # Read
    read_resp = client.get(f"/api/events/{event_id}")
    assert read_resp.status_code == 200
    assert read_resp.get_json()["title"] == "System Test Event"

    # Update
    update_resp = put_json(client, f"/api/events/{event_id}", {"title": "Updated System Test"})
    assert update_resp.status_code == 200
    assert update_resp.get_json()["title"] == "Updated System Test"

    # Delete
    delete_resp = client.delete(f"/api/events/{event_id}")
    assert delete_resp.status_code == 200

    # Confirm gone
    gone_resp = client.get(f"/api/events/{event_id}")
    assert gone_resp.status_code == 404