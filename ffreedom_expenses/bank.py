from flask import Blueprint

bank_bp = Blueprint("bank", __name__, url_prefix="/bank")


@bank_bp.route("/connect")
def connect():
    return '<a href="/connect">Connect to your Bank</a>'
