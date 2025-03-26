from flask import Blueprint, render_template, abort, jsonify
from app.models.harvester import HarvesterData
from datetime import datetime, timedelta

views_bp = Blueprint("views", __name__)

@views_bp.route("/")
def index():
    threshold = timedelta(minutes=5)
    now = datetime.utcnow()
    
    harvesters = HarvesterData.query.order_by(HarvesterData.last_updated.desc()).all()
    
    enriched_harvesters = []
    for h in harvesters:
        status = "Connecté" if now - h.last_updated < threshold else "Déconnecté"
        enriched_harvesters.append({
            "id": h.id,
            "hostname": h.hostname,
            "ip": h.ip,
            "latency": h.latency,
            "nb_machines": h.nb_machines,
            "scan_results": h.scan_results,
            "last_updated": h.last_updated,
            "status": status
        })

    harvesters_count = len(enriched_harvesters)

    return render_template("dashboard.html",
                           harvesters=enriched_harvesters,
                           harvesters_count=harvesters_count)

@views_bp.route("/harvesters_json")
def harvesters_json():
    threshold = timedelta(minutes=5)
    now = datetime.utcnow()
    harvesters = HarvesterData.query.order_by(HarvesterData.last_updated.desc()).all()
    
    enriched = []
    for h in harvesters:
        status = "Connecté" if now - h.last_updated < threshold else "Déconnecté"
        enriched.append({
            "id": h.id,
            "hostname": h.hostname,
            "ip": h.ip,
            "latency": h.latency,
            "nb_machines": h.nb_machines,
            "last_updated": h.last_updated.isoformat(),
            "scan_results": h.scan_results,
            "status": status
        })
    return jsonify(enriched)

@views_bp.route("/harvester/<int:harvester_id>")
def harvester_detail(harvester_id):
    harvester = HarvesterData.query.get(harvester_id)
    if not harvester:
        abort(404)
    
    threshold = timedelta(minutes=5)
    now = datetime.utcnow()
    status = "Connecté" if now - harvester.last_updated < threshold else "Déconnecté"
    
    harvester_data = {
        "id": harvester.id,
        "hostname": harvester.hostname,
        "ip": harvester.ip,
        "latency": harvester.latency,
        "nb_machines": harvester.nb_machines,
        "scan_results": harvester.scan_results,
        "last_updated": harvester.last_updated,
        "status": status
    }
    return render_template("harvester_detail.html", harvester=harvester_data)
