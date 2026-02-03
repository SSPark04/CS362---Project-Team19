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

6.2 Team Member Roles and Justification

    - Charley Lotspeich (Project Researcher): Responsible for researching map APIs, event data formats, and best practices for calendar interfaces. Charley's research role ensures we make informed technical decisions and understand user needs.
    - Sangwoo(Shawn) Park (Leader): Coordinates team efforts, makes final decisions on technical approaches, and ensures project milestones are met. As leader, Shawn will facilitate communication and resolve conflicts.
    - Brian McCarthy (Scheduler/Organizer): Manages the project timeline, tracks progress, and organizes team meetings. Brian's organizational role ensures the team stays on schedule and all members are aware of deadlines.
    - Kyohei Yamaguchi (Quality Assurance Tester): Designs and executes test cases, identifies bugs, and verifies that all features work as expected. Kyohei's QA role ensures the final product is reliable and user-friendly.

6.3 Development Schedule and Milestones
    [TODO: Identify milestones (external and internal), define tasks along with effort estimates (at granularity no coarser than 1-person-week units), and identify dependences among them. Use a table format.]

6.4 Risk Management
    6.4.1 Risk 1: [TODO: Risk name]
        Likelihood: [TODO: high/medium/low]
        Impact: [TODO: high/medium/low]
        Evidence: [TODO: Evidence upon which you base your estimates]
        Mitigation Steps: [TODO: Steps you are taking to reduce the likelihood or impact]
        Detection Plan: [TODO: Plan for detecting the problem]
        Mitigation Plan: [TODO: Mitigation plan should it occur]
        Changes since Requirements: [TODO: How this has changed since Requirements document]
    
    6.4.2 Risk 2: [TODO: Risk name]
        Likelihood: [TODO: high/medium/low]
        Impact: [TODO: high/medium/low]
        Evidence: [TODO: Evidence upon which you base your estimates]
        Mitigation Steps: [TODO: Steps you are taking to reduce the likelihood or impact]
        Detection Plan: [TODO: Plan for detecting the problem]
        Mitigation Plan: [TODO: Mitigation plan should it occur]
        Changes since Requirements: [TODO: How this has changed since Requirements document]
    
    6.4.3 Risk 3: [TODO: Risk name]
        Likelihood: [TODO: high/medium/low]
        Impact: [TODO: high/medium/low]
        Evidence: [TODO: Evidence upon which you base your estimates]
        Mitigation Steps: [TODO: Steps you are taking to reduce the likelihood or impact]
        Detection Plan: [TODO: Plan for detecting the problem]
        Mitigation Plan: [TODO: Mitigation plan should it occur]
        Changes since Requirements: [TODO: How this has changed since Requirements document]
    
    6.4.4 Risk 4: [TODO: Risk name]
        Likelihood: [TODO: high/medium/low]
        Impact: [TODO: high/medium/low]
        Evidence: [TODO: Evidence upon which you base your estimates]
        Mitigation Steps: [TODO: Steps you are taking to reduce the likelihood or impact]
        Detection Plan: [TODO: Plan for detecting the problem]
        Mitigation Plan: [TODO: Mitigation plan should it occur]
        Changes since Requirements: [TODO: How this has changed since Requirements document]
    
    6.4.5 Risk 5: [TODO: Risk name]
        Likelihood: [TODO: high/medium/low]
        Impact: [TODO: high/medium/low]
        Evidence: [TODO: Evidence upon which you base your estimates]
        Mitigation Steps: [TODO: Steps you are taking to reduce the likelihood or impact]
        Detection Plan: [TODO: Plan for detecting the problem]
        Mitigation Plan: [TODO: Mitigation plan should it occur]
        Changes since Requirements: [TODO: How this has changed since Requirements document]

6.5 External Feedback Process
    [TODO: Describe how external feedback is collected and incorporated]

6.6 Test Plan & Bugs
    6.6.1 Testing Strategy
        Unit Testing: [TODO: Describe unit testing strategy]
        System/Integration Testing: [TODO: Describe system/integration testing strategy]
        Usability Testing: [TODO: Describe usability testing strategy]
    
    6.6.2 Test Suites
        [TODO: Describe specific test suites identified to capture the requirements]
    
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
    [TODO: Provide an overview of the system architecture]

7.2 Major Components
    [TODO: Identify and describe the major software components and their functionality at a conceptual level]

7.3 Component Interfaces
    [TODO: Specify the interfaces between components]

7.4 Data Storage
    [TODO: Describe in detail what data your system stores, and how. If it uses a database, give the high level database schema. If not, describe how you are storing the data and its organization.]

7.5 Architectural Assumptions
    [TODO: If there are particular assumptions underpinning your chosen architecture, identify and describe them]

7.6 Architectural Decisions
    7.6.1 Decision 1: [TODO: Architecture decision]
        Alternative: [TODO: Describe alternative]
        Pros: [TODO: Pros of alternative]
        Cons: [TODO: Cons of alternative]
        Rationale: [TODO: Why we chose our approach]
    
    7.6.2 Decision 2: [TODO: Architecture decision]
        Alternative: [TODO: Describe alternative]
        Pros: [TODO: Pros of alternative]
        Cons: [TODO: Cons of alternative]
        Rationale: [TODO: Why we chose our approach]


8. Software Design

8.1 Component 1: [TODO: Component name]
    8.1.1 Packages/Classes/Units
        [TODO: What packages, classes, or other units of abstraction form this component?]
    
    8.1.2 Responsibilities
        [TODO: What are the responsibilities of each of those parts of the component?]

8.2 Component 2: [TODO: Component name]
    8.2.1 Packages/Classes/Units
        [TODO: What packages, classes, or other units of abstraction form this component?]
    
    8.2.2 Responsibilities
        [TODO: What are the responsibilities of each of those parts of the component?]

8.3 Component 3: [TODO: Component name]
    8.3.1 Packages/Classes/Units
        [TODO: What packages, classes, or other units of abstraction form this component?]
    
    8.3.2 Responsibilities
        [TODO: What are the responsibilities of each of those parts of the component?]

[Note: Add more components as needed]


9. Coding Guidelines

9.1 Python
    Guideline: PEP 8 -- Style Guide for Python Code (https://pep8.org/)
    

9.2 [TODO: Additional languages if any]
    Guideline: [TODO: Link to pre-existing coding style guideline]
    Rationale: [TODO: Briefly state why you chose this guideline]
    Enforcement: [TODO: How you plan to enforce this guideline]
