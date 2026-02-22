"""
data_manager.py
Handles reading and writing event data to data/events.json.
"""

import json
import os
import uuid


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
EVENTS_FILE = os.path.join(DATA_DIR, "events.json")


def load_events():
    """
    Read all events from the JSON file and return them as a list.
    """
    if not os.path.exists(EVENTS_FILE):
        return []

    with open(EVENTS_FILE, "r", encoding="utf-8") as f:
        events = json.load(f)

    return events


def save_events(events):
    """
    Write the full list of events to the JSON file (atomic write).
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    temp_file = EVENTS_FILE + ".tmp"

    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2, ensure_ascii=False)

    # Atomic rename: replace the old file with the new one
    if os.path.exists(EVENTS_FILE):
        os.remove(EVENTS_FILE)
    os.rename(temp_file, EVENTS_FILE)


def generate_event_id():
    """
    Generate a unique event ID.
    """
    return "evt-" + uuid.uuid4().hex[:8]


def get_event_by_id(event_id):
    """
    Find and return a single event by its event_id.
    Returns None if not found.
    """
    events = load_events()

    for event in events:
        if event["event_id"] == event_id:
            return event

    return None


def add_event(event_data):
    """
    Add a new event to the JSON file.
    event_data is a dict without event_id (we generate it here).
    Returns the created event with its new event_id.
    """
    events = load_events()

    new_event = event_data.copy()
    new_event["event_id"] = generate_event_id()

    events.append(new_event)
    save_events(events)

    return new_event


def update_event(event_id, updated_fields):
    """
    Update an existing event by its event_id.
    updated_fields is a dict of fields to change.
    Returns the updated event, or None if the event was not found.
    """
    events = load_events()
    found = False

    for i in range(len(events)):
        if events[i]["event_id"] == event_id:
            for key in updated_fields:
                events[i][key] = updated_fields[key]
            found = True
            updated_event = events[i]
            break

    if not found:
        return None

    save_events(events)
    return updated_event


def delete_event(event_id):
    """
    Delete an event by its event_id.
    Returns True if deleted, False if not found.
    """
    events = load_events()

    new_events = []
    found = False

    for event in events:
        if event["event_id"] == event_id:
            found = True
        else:
            new_events.append(event)

    if not found:
        return False

    save_events(new_events)
    return True
