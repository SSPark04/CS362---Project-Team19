# Busy Beaver Calendar – Developer Guide

## Getting the Source Code

Clone the repository from GitHub:

    git clone https://github.com/SSPark04/CS362---Project-Team19.git
    cd CS362---Project-Team19
    git checkout main

---

## Project Directory Structure

The repository is organized as follows:

### Backend

- **app.py** – Flask application entry point and server configuration
- **routes.py** – REST API endpoint definitions
- **event_service.py** – Core business logic for event validation and filtering
- **event_sort.py** – Event dataclass and sort function (used by event_service.py)
- **data_manager.py** – Handles reading and writing event data to JSON storage
- **data/events.json** – Event data storage (5 sample events included)

### Frontend

- **templates/** – HTML templates for the web interface
- **static/** – Frontend assets (CSS, images, and JavaScript files)
- **static/js/** – Frontend JavaScript (future: api.js, calendar.js, map.js)

### Testing

- **tests/** – pytest test cases for backend logic and API endpoints (55 tests total)

### Documentation

- **docs/** – User Manual, Developer Guide, and implementation plan
- **docs/reports/** – Weekly progress reports

### Project Configuration

- **requirements.txt** – Python dependencies (Flask, pytest)
- **README.md** – Project overview and quick-start instructions

---

## Build Instructions

### Prerequisites

- Python 3.x
- Pip

### Install Dependencies

    pip install -r requirements.txt
    python app.py
### Testing Instructions
- Naming convention: Include Type of test(unit,stress,implementation, ect), program being tested, and the test number if it's a part of a suite.
- A test harness should be used to make running a lot of tests easier. Not every section needs a test harness. One section that should have a test harness is the event sorter. 
        Another that should have one is the auto event updater for the map and calendar.
- Tests are implemented using pytest and located in the tests/ directory.
- To run all tests:
   - pytest


## Adding New Tests

- All test files must be placed in the `tests/` directory.
- Test files should follow the naming pattern:
  - `test_<feature>.py`
  - Example: `test_events.py`

Each test should:

- Clearly describe its purpose
- Be independent of other tests
- Use meaningful assertion messages where applicable

When adding new features, corresponding tests must be added.

### Release Process
 - For the releases of the website we need to update the version number to 1.0. As this is the full version of our site and the first time it is pushed out.
 - Sanity checking will be used after each update and release of the product. It makes no sense to go through with and update to add a feature if doing so breaks the whole program. This test won't be as rigorous as normal     testing. However it should be able to catch most functionality mistakes.

---


## API Reference

Base URL: `http://localhost:5000`

### GET /api/events

Returns all events. Optional query params:

- `?filter=today` or `?filter=week`
- `?start=YYYY-MM-DD&end=YYYY-MM-DD`
- `?sort=title|date|start_time`
- `?order=asc|desc` (default: asc)

### GET /api/events/\<event_id\>

Returns a single event or 404.

### POST /api/events

Creates a new event. `event_id` is auto-generated.

Required fields: `title`, `date` (YYYY-MM-DD), `start_time` (HH:MM), `end_time` (HH:MM), `building`

Optional fields: `description`, `room`, `latitude`, `longitude`

Example request body:

```json
{
  "title": "Python Workshop",
  "date": "2026-03-01",
  "start_time": "10:00",
  "end_time": "11:30",
  "building": "KEC"
}
```

Returns `201` with the created event (including generated `event_id`).

### PUT /api/events/\<event_id\>

Updates an event. Send only the fields you want to change. Returns `200` or `404`.

### DELETE /api/events/\<event_id\>

Deletes an event. Returns `200` or `404`.

### Error Responses

- `400` — Missing/invalid fields or non-JSON body
- `404` — Event not found
- `500` — Server error

---

## Event JSON Format

```json
{
  "event_id": "evt-a3f8c210",
  "title": "Learn from an Alum",
  "description": "Alumni sharing experience.",
  "date": "2026-02-02",
  "start_time": "14:00",
  "end_time": "15:30",
  "building": "KEC",
  "room": "1007",
  "latitude": 0,
  "longitude": 0
}
```

---

## Testing API Locally

Make sure the server is running first (`python app.py`).

### PowerShell

    Invoke-RestMethod http://localhost:5000/api/events
    Invoke-RestMethod "http://localhost:5000/api/events?sort=title"

Note: PowerShell's `curl` is an alias for `Invoke-WebRequest` and shows a security warning. Use `Invoke-RestMethod` instead.

### Bash

    curl http://localhost:5000/api/events
    curl -X POST http://localhost:5000/api/events \
      -H "Content-Type: application/json" \
      -d '{"title":"Test","date":"2026-03-01","start_time":"10:00","end_time":"11:00","building":"KEC"}'

---

## Using API from Frontend JS

JS files in `static/js/` call the API via `fetch()`. No Python imports needed — just the URL.

```javascript
// Get all events
var response = await fetch("/api/events");
var events = await response.json();

// Create an event
await fetch("/api/events", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({title: "New Event", date: "2026-03-01", ...})
});
```

Load scripts in `templates/index.html`:

```html
<script src="{{ url_for('static', filename='js/api.js') }}"></script>
<script src="{{ url_for('static', filename='js/calendar.js') }}"></script>
<script src="{{ url_for('static', filename='js/map.js') }}"></script>
```
