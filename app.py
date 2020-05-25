import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from models import db, Actor, Movie

# create and configure the app
app = Flask(__name__)
app.config.from_object(Config) # connect app to a local postgresql database
db = SQLAlchemy(app) # initializing the instance with the app context
CORS(app)
