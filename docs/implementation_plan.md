# Implementation Plan — Busy Beaver Calendar

## 1. Current State (Completed)

- Flask base application is set up and running
  - `app.py` — Flask entry point with API Blueprint registration
  - `templates/index.html` — Main page template (converted from mock_web_page)
  - `static/styles.css` — Styling
  - `static/images/` — Image assets
  - `requirements.txt` — Python dependencies (`Flask==3.1.3`, `pytest==9.0.2`)
  - `.gitignore` — Excludes `venv/`, `__pycache__/`, `.pytest_cache/`, etc.
- Full backend is implemented and tested (55 tests passing)
  - `data_manager.py` — JSON CRUD with atomic writes
  - `event_service.py` — Validation, date filtering, sorting
  - `routes.py` — REST API endpoints (Flask Blueprint)
  - `data/events.json` — Sample event data (5 events)
  - `tests/` — Unit and integration tests for all backend modules
- The dev server runs at `http://127.0.0.1:5000`
- Documents and reports organized under `docs/` and `docs/reports/`

---

## 2. Project Structure (Target)

```
CS362---Project-Team19/
├── app.py                     # Flask init + Blueprint registration
├── routes.py                  # REST API endpoint definitions
├── event_service.py           # Business logic (filter, sort, validate)
├── event_sort.py              # Event dataclass and sort logic (moved from EventSorter/)
├── data_manager.py            # JSON file CRUD operations
├── email_parser.py            # Parse event info from Outlook emails (future)
├── requirements.txt           # Flask, pytest
├── .gitignore
│
├── data/
│   └── events.json            # Event data storage (5 sample events)
│
├── templates/
│   └── index.html             # Main page (Jinja2 template)
│
├── static/
│   ├── styles.css
│   ├── js/
│   │   ├── api.js             # Fetch wrapper for backend API calls (future)
│   │   ├── map.js             # Map rendering (Leaflet.js) (future)
│   │   └── calendar.js        # Calendar display + date filtering (future)
│   └── images/
│       ├── event-map.png
│       └── mock_website.png
│
├── tests/
│   ├── __init__.py
│   ├── test_data_manager.py   # 16 tests
│   ├── test_event_service.py  # 24 tests
│   └── test_routes.py         # 15 tests
│
├── docs/
│   ├── Developer_Guide.md
│   ├── User_Manual.md
│   ├── implementation_plan.md
│   ├── living_document.md
│   ├── Project_SlideShow.pdf
│   └── reports/
│       ├── Progress_Report-Week*.md
│
└── mock_web_page/             # Original static mock (reference only)
```

---

## 3. Event Data Schema

Each event in `data/events.json` follows this structure (defined in living document section 7.4):

```json
{
  "event_id": "evt-001",
  "title": "Learn from an Alum",
  "description": "Alumni sharing industry experience",
  "date": "2026-02-02",
  "start_time": "14:00",
  "end_time": "15:30",
  "building": "KEC",
  "room": "1007",
  "latitude": 0,
  "longitude": 0
}
```

- `event_id` — Unique identifier (string)
- `title` — Event name (string, required)
- `description` — Brief description (string, optional)
- `date` — ISO format `YYYY-MM-DD` (string, required)
- `start_time` / `end_time` — 24-hour format `HH:MM` (string, required)
- `building` — Building name or abbreviation (string, required)
- `room` — Room number (string, optional)
- `latitude` / `longitude` — Coordinates for map pin (float, required)

---

## 4. REST API Endpoints

All endpoints are prefixed with `/api`.

- **GET /api/events**
  - Returns all events as a JSON array
  - Supports optional query parameters:
    - `?filter=today` — Events happening today
    - `?filter=week` — Events this week
    - `?start=YYYY-MM-DD&end=YYYY-MM-DD` — Custom date range
    - `?sort=title|date|start_time` — Sort by field
    - `?order=asc|desc` — Sort order (default: asc)
  - Response: `200` with `[{event}, {event}, ...]`

- **GET /api/events/\<event_id\>**
  - Returns a single event by ID
  - Response: `200` with `{event}` or `404` if not found

- **POST /api/events**
  - Creates a new event
  - Request body: JSON object matching the schema above (without `event_id`; server generates it)
  - Response: `201` with the created `{event}`

- **PUT /api/events/\<event_id\>**
  - Updates an existing event
  - Request body: JSON object with fields to update
  - Response: `200` with the updated `{event}` or `404` if not found

- **DELETE /api/events/\<event_id\>**
  - Deletes an event by ID
  - Response: `200` with `{"message": "deleted"}` or `404` if not found

---

## 5. File Responsibilities (What Goes Where)

### Backend

- **`app.py`**
  - Creates the Flask app instance
  - Registers the API Blueprint from `routes.py`
  - Serves the main page (`/` → `index.html`)

- **`routes.py`**
  - Defines all `/api/...` endpoints as a Flask Blueprint
  - Receives HTTP requests, calls `event_service.py`, returns JSON responses
  - Does NOT contain business logic or direct file I/O

- **`event_service.py`**
  - Contains all business logic
  - Validates event data before saving
  - Filters events by date range
  - Sorts events by importing and using `event_sort.py` (Event dataclass + sort logic)
  - Converts between event dicts and Event dataclass objects via `dict_to_event()`
  - Calls `data_manager.py` for data access

- **`event_sort.py`** (moved from `EventSorter/Event_sort.py`)
  - Defines the `Event` dataclass (name, date, time, tags)
  - Provides `sort_events()` function for sorting Event objects by name, date, time, or tags
  - Used internally by `event_service.py`

- **`data_manager.py`**
  - Reads and writes `data/events.json`
  - Provides functions: `load_events()`, `save_events()`, `get_event_by_id()`, `add_event()`, `update_event()`, `delete_event()`
  - Uses atomic writes (write to temp file, then rename) to prevent corruption

- **`email_parser.py`**
  - Parses event information from email text (subject + body)
  - Returns a dict matching the event schema
  - MVP: accepts raw text input
  - Future: integrates with Microsoft Graph API for automatic email retrieval

### Frontend

- **`static/js/api.js`**
  - Provides helper functions that wrap `fetch()` calls
  - All other JS files use this instead of calling `fetch()` directly
  - Example functions: `getEvents()`, `createEvent(data)`, `deleteEvent(id)`

- **`static/js/calendar.js`**
  - Renders the calendar dynamically using data from `api.js`
  - Handles date clicks and filter changes
  - Updates the calendar view when filters are applied

- **`static/js/map.js`**
  - Initializes a Leaflet.js map centered on OSU campus
  - Renders event pins using latitude/longitude from event data
  - Shows a popup with event details when a pin is clicked

- **`templates/index.html`**
  - Loads all three JS files (`api.js`, `calendar.js`, `map.js`)
  - Contains container elements (`<div id="calendar">`, `<div id="map">`, etc.) that JS populates dynamically

### Data

- **`data/events.json`**
  - The single source of truth for all event data
  - An array of event objects
  - Read by `data_manager.py`, never accessed directly by other files

### Tests

- **`tests/test_data_manager.py`** — Tests JSON CRUD operations
- **`tests/test_event_service.py`** — Tests filtering, sorting, validation
- **`tests/test_routes.py`** — Tests API endpoints using Flask's test client

---

## 6. How Files Reference Each Other

- `routes.py` imports from `event_service.py`
- `event_service.py` imports from `data_manager.py`
- `data_manager.py` reads/writes `data/events.json`
- Frontend JS files call `/api/...` endpoints via `fetch()`

---

## 7. Task Assignments

### Sangwoo (Backend Developer / Architect)

- Create `data/events.json` with 3-5 sample events
- Implement `data_manager.py` (all CRUD functions)
- Implement `event_service.py` (integrate `EventSorter/Event_sort.py`, add filtering and validation)
- Implement `routes.py` (all API endpoints listed in section 4)
- Update `app.py` to register the API Blueprint

### Charley (Frontend Developer / UI Designer)

- Create `static/js/api.js` (fetch wrapper)
- Create `static/js/calendar.js` (dynamic calendar rendering)
- Create `static/js/map.js` (Leaflet.js map with event pins)
- Update `templates/index.html` to load JS files and add dynamic container elements
- Update `static/styles.css` as needed for map and new UI elements

### Brian (DevOps / Outlook Integration)

- Collect 10-20 sample EECS event emails and identify common patterns
- Implement `email_parser.py` to extract event data from email text
- Research Microsoft Graph API for future automatic email retrieval
- Maintain GitHub repository, coordinate merges, support deployment

### Kyohei (QA Engineer)

- Write unit tests in `tests/` for each backend module
- Conduct integration testing after features are merged
- Create usability test checklists
- Track bugs via GitHub Issues

---

## 8. Implementation Order

### Phase 1 — Data Layer (COMPLETED)

- `data/events.json` created with 5 sample events
- `data_manager.py` implemented with all CRUD functions and atomic writes
- 16 unit tests passing (test_data_manager.py)

### Phase 2 — API Layer (COMPLETED)

- `event_service.py` implemented with validation, date filtering, and sorting
- `routes.py` implemented as Flask Blueprint with all REST endpoints
- `app.py` updated to register the Blueprint
- 24 unit tests (test_event_service.py) + 15 integration tests (test_routes.py) passing

### Phase 3 — Frontend (Can start now — API is ready)

- Charley creates all JS files and updates the template
- Charley can use mock data or a running local server to test
- Brian starts collecting email samples and building the parser

### Phase 4 — Email Integration

- Brian completes `email_parser.py`
- Integration with `data_manager.py` to save parsed events
- Future: Microsoft Graph API for automatic retrieval

---

## 9. Outlook Email Integration — Approach

### MVP (Manual)

- Export EECS event emails as text or `.msg` files
- Run `email_parser.py` to extract event details using regex / pattern matching
- Parsed events are saved to `data/events.json` via `data_manager.py`

### Post-MVP (Automatic via Microsoft Graph API)

- Register an app in Azure AD (using OSU account)
- Implement OAuth2 login flow
- Use Graph API to fetch emails:
  - `GET https://graph.microsoft.com/v1.0/me/messages?$filter=from/emailAddress/address eq 'eecs@oregonstate.edu'`
- Parse email body with `email_parser.py`
- Save extracted events automatically

### Key Decision Point

- The difficulty of email parsing depends entirely on how consistent the email format is
- Collect real samples first, then decide the parsing strategy
- If formats vary too much, consider a simple admin form for manual event entry as the primary workflow

---

## 10. Getting Started (For New Contributors)

```bash
# Clone the repository
git clone https://github.com/SSPark04/CS362---Project-Team19.git
cd CS362---Project-Team19

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate     # Windows (PowerShell)

# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py

# Open in browser
# http://127.0.0.1:5000

# Run all tests
python -m pytest tests/ -v
```
