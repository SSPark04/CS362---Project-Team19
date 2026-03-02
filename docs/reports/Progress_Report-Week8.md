# Week 8: Testing & CI Setup

## Team Report

---

## Goals planned for this week

- Set up GitHub Actions CI with pytest  
- Add unit, validation, integration, and system tests  
- Connect frontend JS to backend API  
- Integrate email parser into the app  

---

## Team progress and issues

- **what team did:** Set up CI with GitHub Actions, added tests across all modules, connected frontend calendar/map to the backend API, updated index.html to be fully dynamic  
- **what worked:** GitHub Actions detected the YAML file automatically and ran all tests on every push and PR without extra setup  
- **what team learned:** How to configure CI pipelines, how to write different types of tests (unit, validation, integration, system), and how to debug CI failures remotely  
- **where team had trouble and where the team is stuck:** email_parser is not yet connected to the API — need to decide whether to add a browser form or auto-fetch via Microsoft Graph API  

---

## Goals planned for next week (Higher-level team tasks)

- Connect email_parser to the app (add /api/parse-email endpoint or admin page)  
- Fix remaining CI test failures (email_parser whitespace issue)  
- Add more test coverage and finalize documentation  

---

# Contributions of Individual Team Members

---

## Team Member 1: Kyohei Yamaguchi

### Goals planned for this week

- Set up GitHub Actions CI for automated testing  
- Add user location feature to the map  
- Update Developer Guide and User Manual  

### Team progress and issues

- **what team member did:**  
  - Created `.github/workflows/test.yml` to set up GitHub Actions CI — runs `pytest tests/ -v` on every push and PR to main  
  - Added user geolocation to `static/js/map.js` — shows the user's current location as a red dot on the map using the browser Geolocation API  
  - Updated `docs/Developer_Guide.md` — added Architecture, API Reference, Event JSON Format, Testing API Locally, and Using API from Frontend JS sections  
  - Updated `docs/User_Manual.md` — added latitude/longitude placeholder note to Limitations  
  - Updated `docs/implementation_plan.md` — updated directory structure to reflect current state (event_sort.py, docs/, tests/)  
  - Added CI section to living document (test automation infrastructure, CI service comparison, triggers, build steps)  
- **what worked:** GitHub Actions required zero external setup — just a YAML file in the repo and it started running automatically  
- **what team member learned:** How to configure GitHub Actions workflows, how Leaflet.js handles custom marker icons, and browser Geolocation API usage  
- **where stuck:** email_parser needs a way to be called from the app (API endpoint or admin page) — waiting for team decision  

### Goals planned for next week (Lower-level individual tasks)

- Help connect email_parser to the app (add endpoint or admin page)  
- Add validation and system tests  
- Final documentation cleanup before submission  

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
