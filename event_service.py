"""
event_service.py
Business logic for events: validation, filtering, and sorting.
"""

from datetime import datetime, timedelta, date, time
import traceback
import data_manager
from event_sort import Event, sort_events as sort_event_objects


# Required fields when creating a new event
REQUIRED_FIELDS = ["title", "date", "start_time", "end_time", "building"]


def validate_event(event_data):
    """
    Check that event_data has all required fields and valid formats.
    Returns a tuple: (is_valid, error_message)
        - (True, "") if valid
        - (False, "reason") if invalid
    """
    # Check required fields
    for field_name in REQUIRED_FIELDS:
        if field_name not in event_data:
            return (False, "Missing required field: " + field_name)
        if str(event_data[field_name]).strip() == "":
            return (False, "Field cannot be empty: " + field_name)

    # Check date format (YYYY-MM-DD)
    try:
        datetime.strptime(event_data["date"], "%Y-%m-%d")
    except ValueError as e:
        print("Validation error (date):")
        traceback.print_exc()
        return (False, "Invalid date format. Use YYYY-MM-DD.")

    # Check time format (HH:MM)
    try:
        datetime.strptime(event_data["start_time"], "%H:%M")
    except ValueError as e:
        print("Validation error (start_time):")
        traceback.print_exc()
        return (False, "Invalid start_time format. Use HH:MM.")

    try:
        datetime.strptime(event_data["end_time"], "%H:%M")
    except ValueError as e:
        print("Validation error (end_time):")
        traceback.print_exc()
        return (False, "Invalid end_time format. Use HH:MM.")

    # Check that end_time is after start_time
    start = datetime.strptime(event_data["start_time"], "%H:%M")
    end = datetime.strptime(event_data["end_time"], "%H:%M")
    if end <= start:
        return (False, "end_time must be after start_time.")

    return (True, "")


def get_all_events():
    """
    Return all events from the data file.
    """
    return data_manager.load_events()


def get_event(event_id):
    """
    Return a single event by ID, or None if not found.
    """
    return data_manager.get_event_by_id(event_id)


def create_event(event_data):
    """
    Validate and create a new event.
    Returns a tuple: (event_or_none, error_message)
        - (event, "") on success
        - (None, "reason") on failure
    """
    is_valid, error = validate_event(event_data)
    if not is_valid:
        return (None, error)

    new_event = data_manager.add_event(event_data)
    return (new_event, "")


def update_event(event_id, updated_fields):
    """
    Update an event. If the update includes validated fields, re-validate.
    Returns a tuple: (event_or_none, error_message)
    """
    # Check that the event exists
    existing = data_manager.get_event_by_id(event_id)
    if existing is None:
        return (None, "Event not found.")

    # Build what the event would look like after the update
    merged = dict(existing)
    for key in updated_fields:
        merged[key] = updated_fields[key]

    # Validate the merged result
    is_valid, error = validate_event(merged)
    if not is_valid:
        return (None, error)

    result = data_manager.update_event(event_id, updated_fields)
    return (result, "")


def delete_event(event_id):
    """
    Delete an event by ID.
    Returns True if deleted, False if not found.
    """
    return data_manager.delete_event(event_id)


def filter_events_by_date(filter_type, start_date=None, end_date=None):
    """
    Filter events by date.
    filter_type: "today", "week", or "range"
    For "range", provide start_date and end_date as "YYYY-MM-DD" strings.
    Returns a list of matching events.
    """
    events = data_manager.load_events()
    today = datetime.today().date()

    if filter_type == "today":
        target = today.strftime("%Y-%m-%d")
        results = []
        for event in events:
            if event["date"] == target:
                results.append(event)
        return results

    elif filter_type == "week":
        # Monday of this week
        monday = today - timedelta(days=today.weekday())
        sunday = monday + timedelta(days=6)

        monday_str = monday.strftime("%Y-%m-%d")
        sunday_str = sunday.strftime("%Y-%m-%d")

        results = []
        for event in events:
            if monday_str <= event["date"] <= sunday_str:
                results.append(event)
        return results

    elif filter_type == "range":
        if start_date is None or end_date is None:
            return []
        if start_date > end_date:
            return []

        results = []
        for event in events:
            if start_date <= event["date"] <= end_date:
                results.append(event)
        return results

    else:
        return events


def dict_to_event(event_dict):
    """
    Convert an event dict to an Event dataclass object
    for use with event_sort.sort_events().
    Maps: title -> name, date -> date, start_time -> time
    """
    name = event_dict.get("title", "")

    date_str = event_dict.get("date", "1970-01-01")
    parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()

    time_str = event_dict.get("start_time", "00:00")
    parsed_time = datetime.strptime(time_str, "%H:%M").time()

    return Event(name=name, date=parsed_date, time=parsed_time)


def sort_events(events, sort_by, reverse=False):
    """
    Sort a list of event dicts by a given field.
    Uses event_sort.sort_events() (from Event_sort.py) internally.
    sort_by: "title", "date", or "start_time"
    reverse: True for descending order
    Returns a new sorted list of dicts.
    """
    if sort_by not in ("title", "date", "start_time"):
        return list(events)

    # Map our field names to Event_sort.py field names
    sort_key_map = {
        "title": "name",
        "date": "date",
        "start_time": "time",
    }
    event_sort_key = sort_key_map[sort_by]

    # Convert dicts to Event objects, keeping track of original dicts
    event_pairs = []
    for event_dict in events:
        event_obj = dict_to_event(event_dict)
        event_pairs.append((event_obj, event_dict))

    # Extract just the Event objects for sorting
    event_objects = [pair[0] for pair in event_pairs]

    # Sort using Event_sort.py
    sorted_objects = sort_event_objects(event_objects, by=event_sort_key, reverse=reverse)

    # Map sorted Event objects back to original dicts
    # Build a lookup: Event object id -> original dict
    obj_to_dict = {}
    for event_obj, event_dict in event_pairs:
        obj_to_dict[id(event_obj)] = event_dict

    sorted_dicts = []
    for sorted_obj in sorted_objects:
        sorted_dicts.append(obj_to_dict[id(sorted_obj)])

    return sorted_dicts
