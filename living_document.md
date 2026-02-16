Our Teams: 
    
    - Charley Lotspeich
    - Sangwoo(Shawn) Park
    - Brian McCarthy
    - Kyohei Yamaguchi


Ideas:

    - Busy Beaver Calender

Languages:

    - Python
    - C++
    - C


1. Team info

Role:
        
    - Charley Lotspeich - Project Researcher
    - Sangwoo(Shawn) Park - Leader
    - Brian McCarthy - Scheduler / Organizer
    - Kyohei Yamaguchi - Quality Assurance Tester
    
    Github Repo: https://github.com/SSPark04/CS362---Project-Team19 


2. Product Description

Abstract

    Many events are held within the OSU EECS department, but students often find it hard to identify their exact locations. 
    To solve this problem, we propose a web service that visualizes event information using a map interface. 
    This service allows users to check event venues quickly and intuitively.   
  

Goal

    Our goal is to provide a visual platform where students can immediately identify EECS events on campus. 
    The system displays the location, time, and event details directly on the university map. 
    This allows students to intuitively find relevant workshops or meetups and helps them manage their schedules more efficiently.
    
    - Current Practice
    Currently, information about EECS events is primarily distributed via email. This traditional method has several drawbacks:
    
    - Lack of Specificity: 
    Text-based emails often fail to provide a clear sense of the event's exact location within the large campus.
    
    - Low Visibility:
    Students must manually search through their inboxes to find event details, making it difficult to get a quick overview of upcoming activities.
    
    - Difficulty in Navigation: 
    Without a visual interface, students cannot intuitively understand the proximity of events to their current location or classrooms.



Novelty

    This project transforms traditional, text-heavy email announcements into a centralized visual dashboard. By mapping event data onto the specific geography of the OSU campus, the service provides a "spatial awareness" of departmental activities that email lists cannot offer.

Effects - OSU Students

    OSU students balance heavy course loads and numerous activities. This system will make it easier for students to discover and attend academic events through a centralized map interface. By seeing exactly where and when events occur in relation to their current location, students can increase their participation in the EECS community and reduce missed opportunities.

Technical Approach
  
    We will develop a web-based platform using a map API (such as Google Maps or OpenStreetMap) as the core interface. The backend will store event data (titles, times, and building locations) which will be rendered as interactive pins on the OSU campus map.

Risk

    The primary risk is the manual data entry and maintenance of event information. To mitigate this, we will design an easy-to-use administrative interface for event organizers to quickly input data, ensuring the map remains up-to-date with minimal effort.

Major Features

    Interactive OSU Map: A visual interface showing all active and upcoming EECS events.
    
    Event Detail Pop-ups: Clicking a map pin reveals the "What, When, and Where" of the event.
    
    Location Pinpointing: Clear markers for building locations and room numbers.
    
    Time-based Filtering: View events happening "Today," "This Week," or by specific time slots.

Optional (Future Extensions)

    AI-Assisted Parsing: Using AI to automatically extract event details from email text to reduce manual entry.
    
    Personalized Recommendations: Suggesting events based on a student's major or interests.
    
    Real-time Navigation Support: Integration with campus walking paths.


3. Use Cases (Functional Requirements)

3.1 Use Case - Charley Lotspeich

    Actors
        - Student
    Triggers
        - Student wants to add a custom event
    Preconditions
        - The web application is accessible and running
        - Student has access to the calendar interface
        - Student is viewing the main calendar page
    Postconditions (success scenario)
        - The custom event is successfully added to the system
        - The event appears on both the calendar view and the OSU campus map
        - A map pin is created at the specified event location
        - Event details (title, time, and location) are stored and viewable
    List of steps (success scenario)
        - Student opens the web app
        - Student selects the option to "add event"
        - System prompts user to enter the event details
        - Student fills in the event details
        - System saves the event data
        - Calendar updates to display the new event
        - Map updates to show a new pin for the event
    Extensions/variations of the success scenario
        - Student edits an existing custom event after creation
        - Student adds an event without a room number and only a building name
        - Student adds a recurring event
        - Student cancels event creation before submission
    Exceptions: failure conditions and scenarios
        - Student doesn't fill the entire form out, system displays an error message highlighting missing inputs
        - Invalid date or time entered, system prevents submission and requests correction
        - Invalid/unknown location, system prompts student to enter a valid campus location

3.2 Use Case - Sangwoo(Shawn) Park

    Actors
        - Student
    Triggers
        - Student clicks an event pin on the map
    Preconditions
        - Event data is loaded
    Postconditions (success scenario)
        - Event details are displayed
    List of steps (success scenario)
        1. Student clicks map pin
        2. System retrieves event data
        3. System displays popup with details
        
        Extensions: Student opens the full detail page
        Exceptions: If event data is missing, show an error message

3.3 Use Case - Brian McCarthy

    Actors
        - students
    Triggers
        - student wants to see were an event is located
    Preconditions
        -The website is up and running
        -the event is pinned on tracked
    Postconditions (success scenario)
        -the events locaation will be displayed on the OSU campus map
    List of steps (success scenario)
        1. student open the website
        2. the student has the event they want tracked
        3. the student goes to the map page
        4. the event they want is tracked on the map.
    Extensions/variations of the success scenario
        - The student looks to see what events are going on at a certain building
    Exceptions: failure conditions and scenarios
        - Invalid event
        - Server Failure
        -the event is cancled
    

3.4 Use Case - Kyohei Yamaguchi

    Actors
        - Student (tester)
        - Busy Beaver Calendar System
    
    Triggers
        Student wants to filter events by a specific date range to find upcoming events.
    
    Preconditions
        - The web application is accessible and running
        - Event data has been loaded into the system
        - Student has access to the calendar interface
    
    Postconditions (success scenario)
        - Events within the selected date range are displayed on both the calendar and map
        - All filtered events show correct information (title, time, location)
        - Map pins are updated to show only filtered events
    
    List of steps (success scenario)
        1. Student opens the Busy Beaver Calendar web page
        2. Student navigates to the calendar view
        3. Student selects a date range filter (e.g., "This Week" or custom range)
        4. System filters events based on the selected date range
        5. Calendar displays only events within the selected range
        6. Map updates to show pins only for filtered events
        7. Student verifies that all displayed events match the date range criteria
    
    Extensions/variations of the success scenario
        - Student filters by location instead of date range
        - Student combines multiple filters (date + location)
        - Student clicks on a filtered event pin to view detailed information
        - Student switches between different time filter presets (Today, This Week, This Month)
    
    Exceptions: failure conditions and scenarios
        - Invalid date range selected (end date before start date): System displays error message and does not apply filter
        - No events found in selected range: System displays "No events found" message
        - System error during filtering: Error message displayed, default view (all events) is shown
        - Network connection lost: System shows connection error and maintains last successfully loaded state


4. Non-functional Requirements

4.1 Scalability

    The system should be able to handle at least 100 concurrent users viewing the calendar and map simultaneously. The application should support displaying up to 500 events at once     without significant performance degradation. Event data should load within 2 seconds on standard internet connections.

4.2 Usability

    The interface should be intuitive enough for students to use without training. All interactive elements (calendar, map pins, filters) should be clearly labeled and responsive. The system should work on both desktop and mobile browsers, with a mobile-friendly layout. Users should be able to find and view event details within 3 clicks from the main page.

4.3 Security and Privacy

    The system should not store or require personal user information beyond what is necessary for basic functionality. Event data should be publicly viewable but protected against unauthorized modification. All user inputs should be sanitized to prevent injection attacks. The system should use HTTPS for all communications.


5. External Requirements

5.1 Error Handling and Robustness
    
    The system must handle invalid user inputs gracefully (e.g., invalid date ranges, malformed search queries) by displaying clear error messages without crashing. If the map API fails to load, the system should display a fallback message and still show event information in list format. Missing or incomplete event data should not break the entire application - partial information should be displayed when available.

5.2 Deployment and Accessibility

    The web application must be deployed on a publicly accessible server with a stable URL that can be shared with OSU students and faculty. The application should be accessible 24/7 with minimal downtime. The deployment should include clear instructions for accessing the service, and the URL should be documented in the project repository.

5.3 Buildability and Documentation
    
    All source code must be available in the GitHub repository with clear instructions for building and running the application locally. Documentation should include: setup instructions, required dependencies, environment variables, API keys configuration, and how to run the development server. New developers should be able to set up and run the project within 30 minutes by following the documentation.

5.4 Scope and Resource Management
   
    The project scope must be achievable by a team of 4 members within one academic quarter. Core features (calendar view, map display, event filtering) will be prioritized over optional features (AI parsing, personalized recommendations). The team will focus on delivering a functional minimum viable product (MVP) that demonstrates all major features before considering extensions.


6. Team Process Description

6. Team Process Description (Expanded)

6.1 Software Toolset

    - Programming Language: Python 3.x
    - Web Framework: Flask (lightweight and flexible for our MVP)
    - Database:Json
    - Frontend: HTML5, CSS3, JavaScript
    - Map Integration: OSU Campus Map API / Google Maps API / OpenStreetMap
    - Version Control: Git, GitHub
    - Testing Framework: pytest (for unit testing)
    - Package Management: pip, requirements.txt
    - Development Tools: VS Code / PyCharm, Postman (for API testing)
    - Deployment: Local

6.2 Team Member Roles and Responsibilities

To align with standard technical roles in software engineering, the team responsibilities are defined as follows:

- Sangwoo (Shawn) Park – Backend Developer / Software Architect
  Responsible for overall system architecture, backend API design and implementation using Flask, data schema definition, and integration between frontend and backend components.

- Charley Lotspeich – Frontend Developer / UI Designer
  Responsible for designing and implementing the user interface, including the interactive map and calendar views, frontend logic in JavaScript, and ensuring responsive usability.

- Brian McCarthy – DevOps / Project Manager  
  Responsible for managing the project timeline, coordinating team communication, maintaining the GitHub repository, and supporting deployment and environment setup.

- Kyohei Yamaguchi – QA Engineer / Test Engineer  
  Responsible for designing test cases, implementing automated unit tests, conducting integration and usability testing, and managing bug tracking through GitHub Issues.

Each role represents a standard technical position commonly found in software development teams, and responsibilities are assigned based on individual strengths while ensuring balanced contributions across architecture, implementation, testing, and project coordination.


6.3 Development Schedule and Milestones

| Task | Owner | Estimated Effort | Dependencies |
|------|-------|------------------|--------------|
| Finalize system architecture and API contracts | Sangwoo | 0.5 person-week | Requirements finalized |
| Frontend UI (map + calendar views) | Charley | 1 person-week | API contracts |
| Backend event APIs and JSON data layer | Sangwoo | 1 person-week | Architecture |
| Event filtering and integration | Brian | 0.5 person-week | Backend + Frontend |
| Integration testing and bug fixing | Kyohei | 0.5 person-week | Core features complete |
| Usability testing and feedback incorporation | Kyohei | 0.5 person-week | Integrated system |
| Documentation (user/admin/developer guides) | All | 0.5 person-week | Features stabilized |

Major milestones include architecture finalization, core feature implementation, system integration, testing, and documentation. Each task depends on completion of preceding components to ensure a structured development flow.



6.4 Risk Management

    6.4.1 Risk 1: Event data parsing is hard
        Likelihood: Medium
        Impact: High
        Evidence: Current practice distributes EECS event info via email, which varies in format and may lack structured location details (room/building). Our optional “AI-assisted parsing” is not part of the MVP, so acquisition may remain manual.        
        Mitigation Steps: 
            - Define an MVP input format (title, date/time, building, optional room).
            - Start with manual entry for MVP; evaluate feasibility of simple rule-based parsing later (regex/templates).
            - Collect 10–20 real EECS emails early to estimate parsing complexity.
        Detection Plan: Track time spent per event entry during the first week of implementation; log issues when email details are missing/ambiguous.
        Mitigation Plan: 
            - Keep manual admin entry as the primary workflow for MVP. 
            - If a room cannot be reliably extracted, store building-only and display a “room unknown” label.
        Changes since Requirements: Requirements mentioned optional AI-assisted parsing; for MP3 planning, we treat parsing automation as post-MVP and design a manual admin workflow as the reliable baseline.

    6.4.2 Risk 2: Map API integration issues
        Likelihood: Medium
        Impact: High
        Evidence: The core UI depends on an external map API (Google Maps, OSU map). API keys, usage limits, or incomplete campus location data can block correct pin rendering.
        Mitigation Steps:
            - Prototype pins + popups early (already started via mock page branch per team chat).
            - Choose one map provider for MVP and document key setup in README.
            - Prefer OSM/Leaflet if we want to reduce key/rate-limit risk.
        Detection Plan: 
            - Automated smoke test: “map loads + one known building pin appears” on every merge to main.
            - Monitor console/network errors for map tile/API failures.
        Mitigation Plan:
            - Provide a fallback list view of events if map fails to load (requirement-aligned robustness).
            - Temporarily pin only building-level locations instead of geocoding.
        Changes since Requirements:
            - Architecture now explicitly plans a fallback list behavior if the map API fails, to prevent total feature loss. 
    
    6.4.3 Risk 3: Data integrity issue cause by Data storage approach
        Likelihood: Low
        Impact: Medium
        Evidence: Current we use JSON as the database. JSON file writes can cause data corruption if multiple admins edit simultaneousl.
        Mitigation Steps:
            - Limit write access to an “admin” role for MVP; reads are public.
            - Implement atomic writes (write temp file then rename) and basic validation.
            - If event count grows, measure load time and consider moving to SQLite/Postgres.
        Detection Plan: Add validation on load (schema check) and log failures.
        Mitigation Plan: Freeze writes during demo if needed
        Changes since Requirements: Requirements emphasized scalability. We can separate concerns, we constrain writers and add atomic-write safeguards to keep JSON viable for MVP.
    
    6.4.4 Risk 4: Frontend and backend integration issues
        Likelihood: Medium
        Impact: Medium
        Evidence: Frontend and backend are developed separately and may have mismatched API expectations.
        Mitigation Steps: Define API contracts early and test endpoints with Postman.
        Detection Plan: Integration testing after each major feature merge.
        Mitigation Plan: Fix mismatched endpoints and temporarily reduce feature scope if needed.
        Changes since Requirements: Integration risk became clearer after mock UI development.

6.5 External Feedback Process

    In this project, external feedback will be collected throughout development through various channels. Initial feedback is received from fellow students through discussions or informal demonstrations during class, and opinions are collected based on the usability and intuition of the map-based interface and calendar functions. In addition, technical feedback on the system architecture and overall design is received from the TA and the professor in charge during the milestone review process. Simple usability tests are conducted with users outside the project team. Participants are asked to perform basic tasks such as finding events, applying date filters, and checking detailed event information, while any confusion or inconvenience occurring during the process is recorded. All collected feedback is shared in team meetings and organized into actionable items and managed as GitHub Issues. Problems that seriously hinder usability or core feedback related to design are immediately addressed, and low-priority improvements are processed in stages, taking into account the project schedule and scope.

6.6 Test Plan & Bugs

    6.6.1 Testing Strategy
        Unit Testing:
        
            - Unit tests will be implemented for backend logic focus on core functionalities such as create event, data validation, filtering by date, and JSON file read/write operations. This will make individual functions behave correctly in isolation.
            - System/Integration Testing: System testing will verify end-to-end functionality across the frontend, backend, and map interface. This includes testing API endpoints, confirming that events created in the backend appear correctly on the map and calendar, and validating that filters update both views consistently. Postman and manual API calls will be used to test backend endpoints, while browser-based testing will verify frontend integration.
            - Usability Testing: Usability testing will be conducted through simple walkthrough sessions with users outside the project team. Participants will be asked to complete basic tasks such as locating an event, applying date filters, and viewing event details. Observed issues or user confusion will be documented and converted into GitHub Issues for tracking and resolution.
    
    6.6.2 Test Suites
        The following test suites will be created to capture core system requirements:
            - Event Management Tests: Verify that events can be created, edited, stored in JSON, and retrieved correctly through backend APIs.
            - Map Rendering Tests: Confirm that event locations are displayed as pins on the map and that clicking a pin shows the correct event details.
            - Filtering Tests: Ensure that date-based filters (e.g., Today, This Week, custom range) correctly update both the calendar view and map pins.
            - API Endpoint Tests: Test backend endpoints for event creation, retrieval, and filtering using Postman or automated pytest requests.
            - Usability Walkthrough Checklist: A manual checklist covering basic user flows such as viewing events, filtering by date, and accessing event details.

    
    6.6.3 Bug Tracking
        We will use GitHub Issues to track all bugs discovered during development, testing, and user feedback. Our bug tracking strategy includes:
        
        - Issue Templates: We will create issue templates for bug reports that include fields for:
          * Description of the bug
          * Steps to reproduce
          * Expected vs. actual behavior
          * Environment (browser, OS, etc.)
          * Screenshots if applicable
        
        - Labeling System: Bugs will be labeled with:
          * Priority (high/medium/low)
          * Component affected (frontend/backend/database/map integration)
          * Status (open/in-progress/resolved)
        
        - Assignment: Bugs will be assigned to team members based on their roles and expertise
        
        - Milestone Tracking: Critical bugs will be linked to project milestones to ensure timely resolution
        
        - Testing Integration: Bugs discovered during testing will be logged as GitHub Issues with links to relevant test cases

6.7 Documentation Plan
    We plan to deliver the following documentation with the system:
    
    - User Guide: Step-by-step instructions for end users on how to:
      * View events on the map
      * Filter events by date and location
      * View event details
      * Use the calendar interface
    
    - Administrator Guide: Instructions for administrators on how to:
      * Add new events to the system
      * Update existing events
      * Manage event data
      * Configure system settings
    
    - Developer Guide: Technical documentation including:
      * System architecture overview
      * API documentation
      * Database schema
      * Setup and installation instructions
      * Contributing guidelines
    
    - README.md: Quick start guide with:
      * Project overview
      * Installation instructions
      * Dependencies
      * How to run the application locally
    
    - In-app Help: Contextual help menus and tooltips within the web application interface


7. Software Architecture

7.1 System Overview

    - The system follows a simple client-server architecture. The frontend is a web-based user interface implemented using HTML, CSS, and JavaScript, which communicates with a Flask backend through RESTful APIs. The backend handles business logic, event management, and data access. Event data is stored in JSON files on the server. A third-party map service (Google Maps or OpenStreetMap) is used to visualize event locations on the OSU campus.
    - Users interact with the system through a browser to view events on a map and calendar interface. Administrators can add or modify events through backend endpoints. The backend retrieves event data from JSON storage and provides it to the frontend, which renders map pins and calendar entries accordingly.


7.2 Major Components

    - Frontend (Web Client): Responsible for displaying the interactive map and calendar interface. It allows users to view events, apply filters, and click map pins to see event details.
    - Backend (Flask Server): Handles application logic, processes requests from the frontend, manages event data, and exposes REST APIs for creating, retrieving, and filtering events.
    - Data Layer (JSON Storage): Stores event information such as title, date/time, building, room, and coordinates. The backend reads from and writes to these JSON files.
    - Map Service (External API): Provides map tiles and geolocation support used to display OSU campus locations and event pins.


7.3 Component Interfaces

    Frontend communicates with the backend through RESTful HTTP APIs using JSON. 
    The backend reads and writes event data from JSON files. 
    The frontend uses an external map API to render locations based on data provided by the backend.
    
7.4 Data Storage

    - Each event record contains fields such as:

        - event_id
        - title
        - description
        - date
        - start_time
        - end_time
        - building
        - room (optional)
        - latitude
        - longitude

 
7.5 Architectural Assumptions

    - The architecture assumes a relatively small number of concurrent users typical of a departmental tool. Most users will only read event data, while write operations are limited to administrators. It is assumed that users have access to a modern web browser and an active internet connection. The system also assumes availability of the external map API. If the map service becomes unavailable, event data can still be displayed in list format as a fallback. The MVP prioritizes simplicity and rapid development over large-scale scalability, with the understanding that the storage layer can later be replaced by a relational database if needed.

7.6 Architectural Decisions

    7.6.1 Decision 1: Use Flask with a lightweight frontend
    
    Alternative:
    Use a full frontend framework such as React.
    
    Pros of alternative:
    - Better support for complex UI state management
    - Easier to scale frontend features in larger applications
    
    Cons of alternative:
    - Higher development complexity
    - Longer setup time and learning curve for the team
    
    Rationale:
    We chose Flask with a lightweight frontend to prioritize rapid MVP development and simplicity. This approach allows the team to focus on core functionality (map display, event filtering, and data management) without introducing unnecessary framework overhead.

    
    7.6.2 Decision 2: Use JSON file storage instead of a relational database
        Alternative:
        Use a relational database such as PostgreSQL or SQLite.
        
        Pros of alternative:
        - Better support for concurrent writes
        - More powerful querying capabilities
        - Improved scalability
        
        Cons of alternative:
        - Additional setup and configuration overhead
        - Increased project complexity for an MVP
        
        Rationale:
        JSON storage was selected to keep the architecture simple and lightweight for the MVP. Given the expected small number of administrators and limited data volume, JSON provides sufficient functionality while allowing faster development. The storage layer can be replaced with a database in future iterations if scalability becomes a concern.
        


8. Software Design

        8.1 Component 1: Backend
    
            8.1.1 Packages/Classes/Units
                - app.py: Initializes the Flask application and registers routes.
                - routes.py: Defines API endpoints for retrieving, creating, and filtering events.
                - event_service.py: Contains business logic related to event processing.
                - data_manager.py: Handles reading and writing event data to JSON storage.
            8.1.2 Responsibilities
                - app.py configures the Flask server and application settings.
                - routes.py exposes RESTful endpoints used by the frontend.
                - event_service.py validates input data and applies filtering logic.
                - data_manager.py manages persistent storage by loading and saving JSON files.


        8.2 Component 2: Frontend

            8.2.1 Packages/Classes/Units
                - index.html: Main entry point for the web interface.
                - styles.css: Defines layout and visual styling.
                - map.js: Handles map initialization, marker rendering, and user interactions.
                - calendar.js: Manages calendar display and date-based filtering.
                - api.js: Contains helper functions for communicating with backend APIs.
    
        
            8.2.2 Responsibilities
                - index.html provides the overall structure of the user interface.
                - styles.css controls visual presentation and responsiveness.
                - map.js initializes the map, displays event pins, and handles pin click behavior.
                - calendar.js renders the calendar view and applies date filters.
                - api.js sends requests to backend endpoints and processes returned JSON data.

[Note: Add more components as needed]


9. Coding Guidelines

        9.1 Python
            Guideline: PEP 8 -- Style Guide for Python Code (https://pep8.org/)
            
        
        9.2 JavaScript
        
            Guideline:
            Airbnb JavaScript Style Guide (https://airbnb.io/javascript/)
            
            Rationale:
            The Airbnb JavaScript Style Guide is an industry-standard guideline that promotes clean, maintainable, and consistent JavaScript code, especially for frontend development.
            
            Enforcement:
            We will use ESLint with the Airbnb configuration to automatically detect style issues. All pull requests will be reviewed to ensure compliance with the guideline.

