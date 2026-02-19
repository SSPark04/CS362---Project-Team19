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
- **data_manager.py** – Handles reading and writing event data to JSON storage

### Frontend

- **templates/** – HTML templates for the web interface
- **static/** – Frontend assets (JavaScript and CSS files)

### Testing

- **tests/** – pytest test cases for backend logic and API endpoints

### Documentation

- **docs/** – User Manual and Developer Guide

### Project Configuration

- **requirements.txt** – Python dependencies
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
    - A test harness should be used to make running a lot of tests easier. Not every section needs a test harness. One section that should have a test harness is the event sorter. Another that should have one is the euro         event updater for the map and calendar.


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

