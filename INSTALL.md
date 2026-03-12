# Installation & Usage Guide

Busy Beaver Calendar is a Flask web application. Follow the steps below to install and run it on your machine.
or You can access the live version at: https://cs362-project-team19.onrender.com

## Prerequisites

- Python 3.12 or higher
- Git
- A modern web browser (Chrome, Firefox, Safari, Edge)

## 1) Clone the repository

```bash
git clone https://github.com/SSPark04/CS362---Project-Team19.git
cd CS362---Project-Team19
```

## 2) Create and activate a virtual environment

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3) Install dependencies

```bash
pip install -r requirements.txt
```

## 4) Run the application

```bash
python app.py
```

The server starts at:

```
http://127.0.0.1:5000/
```

Open this URL in your browser.

## How to Use

1. **View events** — The calendar and event list load automatically on the main page.
2. **Filter by date** — Click `All`, `Today`, or `Week`, or enter a custom date range and click `Apply Range`.
3. **View on map** — Event locations appear as blue pins on the interactive map. Click a pin to see event details.
4. **Your location** — If your browser supports geolocation, a red dot shows your current position on the map.

## Troubleshooting

- **pip not found (Windows):** Recreate the venv with `python -m venv .venv --without-pip`, activate it, then run `python -m ensurepip` followed by `pip install -r requirements.txt`.
- **pytest not recognized (macOS):** Use `python -m pytest` instead of `pytest`.
- **Page does not load:** Make sure the Flask server is running (`python app.py`) and you are accessing `http://127.0.0.1:5000/` in the browser, not opening the HTML file directly.

## Running Tests

```bash
pytest tests/ -v
```

Or if `pytest` is not recognized:

```bash
python -m pytest tests/ -v
```
