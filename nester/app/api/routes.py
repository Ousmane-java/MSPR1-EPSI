from flask import Blueprint, request, jsonify
from app import db
from app.models.harvester import HarvesterData
import json
from datetime import datetime

api_bp = Blueprint("api", __name__)  # <-- IMPORTANT

@api_bp.route("/report", methods=["POST"])
def report():
    data = request.get_json()
    if not data:
        return jsonify({"error": "no data"}), 400

    entry = HarvesterData(
        hostname=data["hostname"],
        ip=data["ip"],
        latency=data["latency"],
        nb_machines=data["nb_machines"],
        scan_results=json.dumps(data["scan"]),
        version=data["version"],
        last_updated=datetime.utcnow()
    )
    db.session.add(entry)
    db.session.commit()

    return jsonify({"message": "Saved"}), 201