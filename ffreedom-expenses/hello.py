from flask import Blueprint

hello_bp = Blueprint("hello_bp", __name__)

@hello_bp.route("/", methods=["GET"])
def hello_world():
    return "Hello, World!"
