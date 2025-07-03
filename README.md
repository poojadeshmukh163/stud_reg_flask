🎓 Flask-Based Student Registration Web Application
🔍 Project Overview
This is a simple Flask-based web application that allows users to register students using a form. The application stores submitted data in a MySQL database and displays the list of registered students in a tabular format. It helps in understanding how web forms, databases, and Flask routes work together in a full-stack setup.

🛠️ Technology Stack
Frontend: HTML, CSS (with optional Bootstrap)
Backend: Python (Flask)
Database: MySQL
Version Control: Git + GitHub
CI/CD (Optional): Jenkins
Deployment (Optional): AWS EC2
🚀 Setup Instructions
1. Clone the Repository
git clone https://github.com//student-registration-flask.git cd student-registration-flask

2. Set Up Virtual Environment
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

3. Configure MySQL Database
1. Login to MySQL:
mysql -u root -p

2. Create a database:
CREATE DATABASE student_db;

4. Run the Flask App
python app.py

Open your browser and go to http://localhost:5000

🌐 Live Deployment (Optional)
If hosted on EC2, visit:

http://your-ec2-public-ip:5000
