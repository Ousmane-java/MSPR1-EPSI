from app import db
from datetime import datetime

class HarvesterData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(128))
    ip = db.Column(db.String(45))
    latency = db.Column(db.String(64))
    nb_machines = db.Column(db.Integer)
    scan_results = db.Column(db.Text)
    version = db.Column(db.String(10))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)