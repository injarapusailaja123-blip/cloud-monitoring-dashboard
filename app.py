from flask import Flask, jsonify
import random
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def dashboard():
    return """
    <html><head><title>Cloud Monitoring Dashboard</title>
    <style>
    body{font-family:Arial;background:#0f172a;color:white;padding:15px}
    h1{text-align:center;color:#38bdf8}
    .cards{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
    .card{background:#1e293b;padding:15px;border-radius:12px;width:140px;text-align:center}
    .alert{text-align:center;padding:12px;border-radius:10px;margin:15px;font-weight:bold}
    .success{background:#14532d}.warning{background:#854d0e}.danger{background:#991b1b}
    table{width:100%;background:#1e293b;border-radius:10px;border-collapse:collapse}
    th,td{padding:10px;border-bottom:1px solid #334155}
    </style></head>
    <body>
    <h1>CLOUD MONITORING DASHBOARD</h1>
    <p style="text-align:center">AWS CloudWatch | Region: ap-south-1 | Author: Injarapu Sailaja</p>
    <div id="alertBox" class="alert success">Loading...</div>
    <div class="cards">
    <div class="card"><p>CPU</p><h2 id="cpu">--%</h2></div>
    <div class="card"><p>Memory</p><h2 id="memory">--%</h2></div>
    <div class="card"><p>Disk</p><h2 id="disk">--%</h2></div>
    <div class="card"><p>Network</p><h2 id="network">--</h2></div>
    </div>
    <h2 style="text-align:center">Monitored Services</h2>
    <table><tr><th>Service</th><th>Type</th><th>Status</th></tr>
    <tr><td>EC2 - Web Server</td><td>EC2</td><td>Running</td></tr>
    <tr><td>RDS - Database</td><td>RDS</td><td>Running</td></tr>
    <tr><td>S3 - Bucket</td><td>S3</td><td>Running</td></tr>
    </table>
    <p style="text-align:center">Last Updated: <span id="time">--</span></p>
    <script>
    function loadData(){
    fetch('/api/metrics').then(r=>r.json()).then(d=>{
    document.getElementById('cpu').innerText=d.cpu+'%';
    document.getElementById('memory').innerText=d.memory+'%';
    document.getElementById('disk').innerText=d.disk+'%';
    document.getElementById('network').innerText=d.network;
    document.getElementById('time').innerText=d.time;
    let box=document.getElementById('alertBox');
    if(d.cpu>80){box.innerText='HIGH CPU ALERT!';box.className='alert danger';}
    else if(d.cpu>65){box.innerText='Warning - CPU is High';box.className='alert warning';}
    else{box.innerText='All Systems Healthy';box.className='alert success';}
    });}
    loadData(); setInterval(loadData,5000);
    </script></body></html>
    """
@app.route('/api/metrics')
def metrics():
    return jsonify({"cpu":random.randint(20,95),"memory":random.randint(30,85),"disk":random.randint(40,75),"network":random.randint(100,900),"time":datetime.now().strftime("%H:%M:%S")})
if __name__=='__main__':
    app.run(debug=True)