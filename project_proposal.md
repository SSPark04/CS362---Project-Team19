Our Teams: 
    
    - Charley Lotspeich
    - Sangwoo(Shawn) Park
    - Brian McCarthy
    - Kyohei Yamaguchi


Ideas:

    - Card game - Brain +1
    - Survival game
    - 2D Platformer
    - Pokemon
    - Puzzle game
    - Balatro but Craps
    - Beaver themed cookie clicker
    - Personal Task Manager with AI Recommendations using API - kyohei, Shawn, Brian +3
    - Open Source software extension - Visual Studio Code extension, Chrome extension - kyohei +1
    - EECS Event Map Web Pag


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
