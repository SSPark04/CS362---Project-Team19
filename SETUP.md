# Setup & Deployment Guide

This document describes how a system administrator or developer can deploy and run Busy Beaver Calendar.

## System Requirements

- Python 3.12+
- pip (Python package manager)
- Git

## Dependencies

All Python dependencies are listed in `requirements.txt`:

- **Flask** — Web framework
- **pytest** — Testing framework
- **python-dateutil** — Date parsing utilities

No external database is required. Event data is stored in `data/events.json`.

## Deployment Steps

### 1) Clone the repository

```bash
git clone https://github.com/SSPark04/CS362---Project-Team19.git
cd CS362---Project-Team19
```

### 2) Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .\.venv\Scripts\Activate.ps1  # Windows PowerShell
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Verify tests pass

```bash
pytest tests/ -v
```

All tests should pass before deployment.

### 5) Start the server

For local development:

```bash
python app.py
```

The app runs on `http://127.0.0.1:5000/` with Flask's built-in development server.

For production deployment, use a WSGI server such as gunicorn:

```bash
pip install gunicorn
gunicorn app:app --bind 0.0.0.0:5000
```

## Project Structure

```
CS362---Project-Team19/
├── app.py                  # Flask entry point
├── routes.py               # API endpoint definitions
├── event_service.py        # Business logic (validation, filtering, sorting)
├── event_sort.py           # Event dataclass and sort function
├── data_manager.py         # JSON file read/write operations
├── email_parser.py         # Email text to event parser
├── data/
│   └── events.json         # Event data storage
├── templates/
│   └── index.html          # Main HTML template
├── static/
│   ├── styles.css          # CSS styles
│   ├── images/             # Static images
│   └── js/
│       ├── api.js          # Frontend API helper
│       ├── calendar.js     # Calendar rendering
│       └── map.js          # Map rendering (Leaflet.js)
├── tests/                  # All test files (pytest)
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
├── INSTALL.md              # User installation guide
├── SETUP.md                # This file
└── .github/workflows/
    └── test.yml            # GitHub Actions CI configuration
```

## CI / Continuous Integration

GitHub Actions is configured in `.github/workflows/test.yml`. It runs automatically on:

- Every push to `main`
- Every pull request targeting `main`

The CI workflow installs dependencies and runs `pytest tests/ -v`.

## Event Data

Events are stored in `data/events.json`. Each event has the following fields:

| Field | Type | Required |
|-------|------|----------|
| event_id | string | auto-generated |
| title | string | yes |
| date | string (YYYY-MM-DD) | yes |
| start_time | string (HH:MM) | yes |
| end_time | string (HH:MM) | yes |
| building | string | yes |
| description | string | no |
| room | string | no |
| latitude | number | no |
| longitude | number | no |

## Issue Tracking

We use GitHub Issues for bug tracking and feature requests:

- Repository: https://github.com/SSPark04/CS362---Project-Team19
- Issues: https://github.com/SSPark04/CS362---Project-Team19/issues
