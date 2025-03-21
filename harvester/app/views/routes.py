from flask import Blueprint, render_template, jsonify
from app.core.network import scan_network
from app.core.system_info import get_ip_hostname, get_latency
from config import Config
import requests

views_bp = Blueprint("views", __name__)

@views_bp.route("/")
def dashboard():
    # Affiche la page d’accueil Harvester
    ip, hostname = get_ip_hostname()
    latency = get_latency()
    data = {
        "hostname": hostname,
        "ip": ip,
        "latency": latency,
        "nb_machines": 0,
        "scan": [],
        "version": Config.VERSION
    }
    return render_template("dashboard.html", data=data)

@views_bp.route("/scan", methods=["GET"])
def scan_network_route():
    # Lance le scan, renvoie JSON
    scan_results = scan_network()
    return jsonify(scan_results)

@views_bp.route("/send", methods=["POST"])
def send_to_server():
    # Scanne puis envoie au Nester
    ip, hostname = get_ip_hostname()
    latency = get_latency()
    scan = scan_network()
    
    payload = {
        "hostname": hostname,
        "ip": ip,
        "latency": latency,
        "nb_machines": len(scan),
        "scan": scan,
        "version": Config.VERSION
    }
    try:
        r = requests.post(Config.SERVER_URL, json=payload)
        return jsonify({"status": "success", "response": r.json()})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})