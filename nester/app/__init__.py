from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    # On précise template_folder pour que Flask sache où chercher les HTML
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)

    # Importer et enregistrer les Blueprints
    from app.api.routes import api_bp
    from app.views.routes import views_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(views_bp)

    # Création de la base de données si inexistante
    with app.app_context():
        db.create_all()

    return app