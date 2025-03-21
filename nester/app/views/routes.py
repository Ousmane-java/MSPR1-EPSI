from flask import Blueprint, render_template
from app.models.harvester import HarvesterData

views_bp = Blueprint("views", __name__)

@views_bp.route("/")
def index():
    # Récupère les enregistrements en base, triés par date
    harvesters = HarvesterData.query.order_by(HarvesterData.last_updated.desc()).all()
    return render_template("dashboard.html", harvesters=harvesters)