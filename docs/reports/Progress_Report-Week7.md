# Week 7: Implementation Kickoff

## Team Report

---

## Goals planned for this week

- Deliver the Mid-term project presentation  
- Pitch our core concept  

---

## Team progress and issues

- **what team did:** Conducted sync meetings to align on the overall project scope and finalized the presentation structure  
- **what worked:** Internal communication significantly improved; the team is now more cohesive  
- **what team learned:** Discovered more efficient ways to delegate tasks based on individual strengths  
- **where team had trouble and where the team is stuck:** Re-establishing momentum was challenging after the temporary absence of three members in Week 4, but we successfully regained our pace  

---

## Goals planned for next week (Higher-level team tasks)

- Complete MVP implementation (backend API, frontend integration, email parsing) in 5 days  
- Reach prototype stage if possible, with basic end-to-end functionality  
- Write unit tests for each implemented feature  

---

# Contributions of Individual Team Members

---

## Team Member 1: Kyohei Yamaguchi

### Goals planned for this week

- Set up Flask base application and project structure  
- Create implementation plan and task assignments for the team  

### Team progress and issues

- **what team member did:**  
  - Built the Flask skeleton (app.py, templates/, static/) and converted the static mock page into a Flask-served application  
  - Created a detailed implementation plan (docs/implementation_plan.md) covering project structure, API design, file responsibilities, and task assignments  
  - Implemented the full backend data layer: data_manager.py (JSON CRUD with atomic writes) and event_service.py (validation, date filtering, sorting)  
  - Implemented routes.py as a Flask Blueprint with all REST API endpoints (GET, POST, PUT, DELETE for /api/events)  
  - Updated app.py to register the API Blueprint  
  - Wrote 55 unit and integration tests across 3 test files (test_data_manager.py, test_event_service.py, test_routes.py), all passing  
  - Created sample event data in data/events.json following the living document schema  
  - Organized project directory structure: moved reports and documents into docs/, created static/js/ for future frontend JS  
  - Set up .gitignore, requirements.txt, and pytest configuration  
- **what worked:** Implementing data_manager.py and event_service.py first made it easy to build routes.py on top; Flask's test client made API integration testing straightforward  
- **what team member learned:** Flask Blueprint pattern for modular route registration, atomic file writes for safe JSON storage, and how to structure pytest fixtures with temporary directories to avoid touching real data  
- **where stuck:** Backend is fully complete; now waiting for frontend (Charley) and email parsing (Brian) to integrate with the API  

### Goals planned for next week (Lower-level individual tasks)

- Conduct integration testing once frontend connects to API endpoints  
- Write additional edge-case tests if new features are added  
- Begin usability test checklist for frontend features  
- Support team members with API usage questions  

---

## Team Member 2: Brian McCarthy

### Goals planned for this week

- Finished eevent sorter  
- Finished Email parser  
- Add test suits for both  

### Team progress and issues

- **what team member did:** Built the event sorter and email parser functionality  
- **what worked:** I found that the documention we laid out was helpfull in implementing this. 
- **what team member learned:** How to integrate smaller level functionality into a larger project  

### Goals planned for next week (Lower-level individual tasks)

- Finnish automatic email update 3 days 
- Deing more test for the email and other function to get ready fo intial build 4 days
  

---

## Team Member 3: Sangwoo Park

### Goals planned for this week

- Help kick off implementation phase  
- Review architecture/design and assist with technical integration (Flask + overall system flow)  

### Team progress and issues

- **what team member did:**  
  - Created a new branch 'feature/api-call' to implement frontend API integration without affecting the main branch
  - Implemented `static/js/api.js`: a fetch-based helper module covering all rest endpoints with support for date filtering and sorting options  
  - Implemented `static/js/map.js`: integrated Leaflet.js with OpenStreetMap to render an interactive OSU campus map and place event pins using latitude/longitude from the backend  
  - Implemented `static/js/calendar.js`: dynamic calendar grid rendering and event list population using live API data, with All/Today/This Week filter support  
  - Updated `templates/index.html` to load Leaflet CDN and connect all JS modules  
  - Updated `data/events.json` with real OSU building coordinates (KEC, MU, GLK) for accurate map pin placement  
  - Set up a Python virtual environment (`venv`) with `requirements.txt` for consistent local development  
  - Verified end-to-end functionality: API calls returning 200, map pins rendering correctly with popup details on click  
- **what worked:** Building `api.js` as a shared module made it straightforward to reuse across `map.js` and `calendar.js`; Leaflet.js integrated cleanly with minimal configuration  
- **what team member learned:** How to structure ES module imports in a Flask-served static environment, and how Leaflet.js handles map tile rendering and marker popups  
- **where stuck:** Map pin coordinates required manual lookup per building; a geocoding integration (e.g. Nominatim) could automate this in a future iteration  

### Goals planned for next week (Lower-level individual tasks)

- Conduct integration testing once Charley connects the calendar/event list UI to the live API  
- Support team members with API usage and JS module questions  
---

## Team Member 4: Charley Lotspeich

### Goals planned for this week

- Contribute to core feature slides and architecture discussion  
- Help finalize presentation content  

### Team progress and issues

- Worked on core feature and architecture slides (Slides 8–9)  
- Helped refine system features including map interaction, calendar view, and filtering logic  
- Participated in discussions about client-server architecture and REST API design  

### Goals planned for next week (Lower-level individual tasks)

- Begin assigned implementation tasks  
