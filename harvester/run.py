import os
from flask import Flask

def create_app():
    # On construit le chemin absolu vers "harvester/app/templates"
    template_path = os.path.join(
        os.path.dirname(__file__),  # Chemin du fichier run.py
        "app",                      # Sous-dossier "app"
        "templates"                # Sous-dossier "templates"
    )

    app = Flask(
        __name__,
        template_folder=template_path
    )

    # Importer et enregistrer ton blueprint
    from app.views.routes import views_bp
    app.register_blueprint(views_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
