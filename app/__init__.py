from flask import Flask
from .extensions import db, migrate  # Assuming you've initialized db and migrate in extensions.py
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration

    db.init_app(app)  # Initialize SQLAlchemy
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    # Import and register the Blueprint
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
