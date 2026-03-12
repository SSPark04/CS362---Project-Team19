# Busy Beaver Calendar v1.0

## What's Included

Busy Beaver Calendar is a web application for viewing OSU-related events on a calendar and interactive map.

### Features

- **Calendar view** with monthly grid and event dots
- **Event list** with date, title, and location
- **Interactive map** (Leaflet.js + OpenStreetMap) with event pins and popups
- **Date filtering** — All, Today, Week, and custom date range
- **Map auto-zoom** — Map adjusts to fit filtered event pins
- **User location** — Shows your current position as a red dot on the map
- **REST API** — Full CRUD endpoints for events (`/api/events`)
- **Email parser** — Extracts event data from email text

### API Endpoints
- GET /api/events — Retrieve all events (supports filter, start, end, sort, order parameters)
- GET /api/events/<event_id> — Retrieve a single event by ID
- POST /api/events — Create a new event

### Test Suite

- 70+ automated tests (unit, integration, validation, system)
- CI via GitHub Actions — runs on every push and PR to main

## How to Run

```bash
git clone https://github.com/SSPark04/CS362---Project-Team19.git
cd CS362---Project-Team19
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## Known Issues

See [open issues](https://github.com/SSPark04/CS362---Project-Team19/issues) for current bugs and planned improvements.
