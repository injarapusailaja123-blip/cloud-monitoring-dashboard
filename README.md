
# Codtech Intern Task 3 - Cloud Monitoring Dashboard

**Name:** Injarapu Sailaja
**Intern ID:** CITS9613
**Domain:** Cloud Computing
**Task:** Task 3

## Objective
AWS CloudWatch lanti Dashboard ni create cheyadam. Cloud lo unna EC2, RDS, S3 services ni live monitor cheyadam.

## Tools Used
Python, Flask, HTML, CSS, JavaScript, AWS CloudWatch Concept

## Features
- 4 Live Cards: CPU Usage, Memory, Disk, Network
- API: /api/metrics - Prathi 5 seconds ki data update avuthundi
- Alert System:
    - CPU < 65% = Green - All Systems Healthy
    - CPU 65% - 80% = Orange - Warning - CPU is High
    - CPU > 80% = RED - HIGH CPU ALERT!
- Monitored Services: EC2 Web Server, RDS Database, S3 Bucket - All Running
- Region: ap-south-1 (Mumbai)

## How to Run
pip install flask
python app.py
Browser lo open cheyandi: http://127.0.0.1:5000

## Results
- Normal State: CPU 50% - Green - All Systems Healthy
- Warning State: CPU 79% - Orange - Warning
- Alert State: CPU 93% - RED - HIGH CPU ALERT!

## Conclusion
Ee project valla Cloud Monitoring ela chestharo, CloudWatch Alarms ela work avuthayo nerchukunnanu. Real-time monitoring valla server down avvakunda mundu gaane alert vasthundi.