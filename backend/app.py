import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from backend.db_extension import db

from backend.models.entities.binder import Binder
from backend.models.entities.song import Song

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000"])

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
Migrate(app, db)
with app.app_context():
    db.create_all()
