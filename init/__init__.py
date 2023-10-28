from flask import Flask
from flask_sqlalchemy import SQLAlchemy
"""
Initializing the app, db and connecting the routes to the app 
"""
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg:///adopt_db"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    app.config["SECRET_KEY"] = "f45#$%fhskdjfhsd@#$@%^$5sdfkashdf"
    
    from routes import app_routes
    app.register_blueprint(app_routes)
    
    return app
