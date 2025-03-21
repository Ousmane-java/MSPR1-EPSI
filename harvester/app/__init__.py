from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import et enregistrement des routes
    from .views.routes import views_bp
    app.register_blueprint(views_bp)

    return app