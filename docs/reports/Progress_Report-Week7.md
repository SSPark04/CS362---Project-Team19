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

- Finish slides  
- Review Week 7 materials  
- Start creating skeleton code  

### Team progress and issues

- **what team member did:** Finished slides on risk  
- **what worked:** Completing slides and memorizing presentation sections  
- **what team member learned:** How to present a more technical presentation  

### Goals planned for next week (Lower-level individual tasks)

- Start implementing login system in 5 days  
- Review Outlook and email integration in 6 days  

---

## Team Member 3: Sangwoo Park

### Goals planned for this week

- Finalize presentation slides and technical explanations  
- Refine system architecture and design documentation  

### Team progress and issues

- Organized presentation content and finalized core features  
- Led architecture and design sections in the living document  
- Participated in meetings to divide roles and establish implementation plans  
- Learned more about software architecture patterns and system modularity  

### Goals planned for next week (Lower-level individual tasks)

- Help kick off implementation phase  
- Review architecture/design and assist with technical integration (Flask + overall system flow)  

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
