# Week 9: Beta Testing & Issue Tracking

## Team Report

---

## Goals planned for this week

- Conduct in-class beta testing (ICE-4) and collect feedback  
- Create GitHub issues from beta testing feedback  
- Continue email_parser integration planning  
- Improve test coverage across all modules  

---

## Team progress and issues

- **what team did:** Conducted beta testing in class — two external testers (Connor Allen, Lon Danna) tested the app and provided detailed feedback. Created 6 GitHub issues (#9–#14) from their reports covering installation, documentation, UI, and map improvements.  
- **what worked:** The beta test script in the README guided testers smoothly through Use Case 3.4; both testers confirmed filter functionality works correctly across calendar, event list, and map.  
- **what team learned:** External users revealed setup friction (pip not bundled in venv on some machines, pytest path issues on macOS) that the team had not encountered internally. Error message visibility was flagged by both testers independently.  
- **where team had trouble and where the team is stuck:** email_parser integration is still pending a team decision on the invocation method (browser form vs auto-fetch). Hosting on OSU servers was suggested but not yet evaluated.  

---

## Goals planned for next week (Higher-level team tasks)

- Fix beta testing issues (#9–#14): error message visibility, map auto-zoom, documentation updates  
- Finalize email_parser integration  
- Add validation and system tests for full coverage  
- Final documentation cleanup for submission  

---

# Contributions of Individual Team Members

---

## Team Member 1: Kyohei Yamaguchi

### Goals planned for this week

- Review beta testing feedback and create GitHub issues  
- Plan bug fixes from ICE-4 feedback for next week  
- Continue improving documentation and test coverage  

### Team progress and issues

- **what team member did:**  
  - Reviewed beta testing feedback from Connor Allen and Lon Danna (ICE-4)  
  - Created 6 GitHub issues (#9–#14) from beta tester reports:  
    - #9: venv setup fails when pip is not bundled (bug)  
    - #10: pytest command fails on macOS — need `python -m pytest` (documentation)  
    - #11: Add app screenshot to README (enhancement)  
    - #12: Error messages for date filter not visible enough (bug)  
    - #13: Map should auto-zoom to fit filtered pins (enhancement)  
    - #14: Consider hosting on OSU servers (enhancement)  
  - Categorized issues with appropriate labels (bug, documentation, enhancement)  
- **what worked:** Using `gh issue create` via CLI made issue creation fast and consistent with proper labels and descriptions  
- **what team member learned:** How to translate beta tester feedback into actionable GitHub issues with clear reproduction steps  
- **where stuck:** No blockers — bug fixes are planned for next week  

### Goals planned for next week (Lower-level individual tasks)

- Fix issues #9, #10, #12, #13 (README troubleshooting, error message styling, map auto-zoom)  
- Add validation and system tests  
- Final documentation cleanup  

---

## Team Member 2: Brian McCarthy

### Goals planned for this week


### Team progress and issues


### Goals planned for next week (Lower-level individual tasks)


---

## Team Member 3: Sangwoo Park

### Goals planned for this week


### Team progress and issues


### Goals planned for next week (Lower-level individual tasks)


---

## Team Member 4: Charley Lotspeich

### Goals planned for this week


### Team progress and issues


### Goals planned for next week (Lower-level individual tasks)

