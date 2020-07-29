from flask import Blueprint
from src.app import db



#Endpoints/routes
api = Blueprint('api', __name__)

@api.route("/")
def home():
    return "Hello World"