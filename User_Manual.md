# Busy Beaver Calendar – User Manual

## High-Level Description
Busy Beaver Calendar is a web-based application for OSU EECS students to visualize EECS events on an interactive map. The system aggregates EECS events such as career events, meetups, and seminars from weekly email, and displays them on a campus map. This tool allows students to quickly identify where and when events are happening relative to their current location, helping them manage their schedule and engage more effectively with the EECS community. 

---

## Installation (Local)

### Prerequisites:
* Python: Version 3.10 or higher.
* pip: Python package manager (latest version recommended).
* Git: To clone the repository.
* Web Browser: Chrome, Firefox, or Safari.
* Database: No external database installation (like MySQL/PostgreSQL) is required. The system uses a JSON-based storage (data/events.json) which is included in the repository.

### Installation Steps
1. Clone the Repository:
   ```bash
   git clone https://github.com/SSPark04/CS362---Project-Team19
   cd CS362---Project-Team19
   ```

2. Create a Virtual Environment:
   It is highly recommended to use a virtual environment to avoid library conflicts.
   ```bash
   python -m venv venv
   # To activate:
   # Windows: venv\Scripts\activate
   # macOS/Linux: source venv/bin/activate
   ```

3. Install Dependencies:
   Install all required libraries using the provided requirements file:
   ```bash
   pip install -r requirements.txt
   ```

4. Environment Configuration:
   Create a .env file in the root directory and add your API keys (e.g., Map provider keys) if applicable.

---

## Installation (AWS)

Docs: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

### Prerequisites:
* AWS account
* EC2 Instance (Linux is recommended)
* Python >= 3.10
* Nginx

### How to run server step-by-step Setup
1. Create Instance:
   Go to this site and create instance: https://www.geeksforgeeks.org/devops/amazon-ec2-creating-an-elastic-cloud-compute-instance/

2. Connect to your instance:
   Open your terminal (search terminal on your device) and type following command:
   ```bash
   chmod 400 my-key.pem
   ssh -i "my-key.pem" ubuntu@<your public ip address> 
   ```
   For more information please read Steps to Connect Terminal Using SSH-Key section in the following page:
   https://www.geeksforgeeks.org/devops/amazon-ec2-creating-an-elastic-cloud-compute-instance/ 

3. In your AWS Linux Terminal:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y python3-pip python3-venv nginx git
   ```

4. Clone repository:
   ```bash
   git clone https://github.com/SSPark04/CS362---Project-Team19
   cd CS362---Project-Team19
   ```

5. Python env setting:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install gunicorn
   ```

---

## How to Run the Software

### Local:
1. Start the local server:
   ```bash
   python app.py
   ```
2. Access following URL:
   http://127.0.0.1:<opened port> (usually 3000 / 5000 / 8000)
3. Stop the system:
   Ctrl + C

### AWS:
1. Configure Nginx (Web Server):
   Create a config file at /etc/nginx/sites-available/eventmap:
   ```nginx
   server {
       listen 80;
       server_name your-aws-public-ip;
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
       }
   }
   ```

2. Enable and restart:
   ```bash
   sudo ln -s /etc/nginx/sites-available/eventmap /etc/nginx/sites-enabled
   sudo systemctl restart nginx
   ```

3. Run the application:
   ```bash
   gunicorn --bind 127.0.0.1:8000 app:app --daemon
   ```
---
### How to Use the Software
   1. The user will need to create/login into an account.
   2. Once successfully logged in the user will be able to see their events displayed
   3. They may need to provide an OSU email address(this is a work in progress and isn’t fully decided in the group)
   4. The user can view the map to see where events are going on
   5. The user can search for events in the event sorter. This is done either by entering the name of an event in which case it will be displayed, searching using tags, dates, or even time. This can also be done to hide certain events.
   6. The user's profile will be saved automatically so they don’t have to re-enter information.
   7. The user can log out or just close the website. (Account system is work in progress)

---
---
## Bug Reporting

- If a bug is found, it can be reported through the project issue tracker on GitHub
- Submit a separate report for each issue and check that it isn't an already existing issue
- Provide a clear summary describing the problem
- Step-by-step instructions on how to reproduce the bug
- Include the desired result and the actual result
- Provide environment details (OS, browser, etc.)
- If available, provide screenshots and error messages.


---

## Known Bugs / Limitations

### Limitations
- Only showing OSU EECS events.
- Map limited to the OSU Corvallis campus.
- Can only be accessed on a desktop and not on a mobile device.

### Known Bugs
- None currently, will update when they become known.
