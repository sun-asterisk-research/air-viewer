import os

from flask_cors import CORS

from app.main import app

cors = CORS(app, resources={"/api/*": {"origins": "*"}})

origins = []
