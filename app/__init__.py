# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # Importar y registrar los blueprints de rutas aquí
    from app.routes import main_routes
    app.register_blueprint(main_routes)

    return app
