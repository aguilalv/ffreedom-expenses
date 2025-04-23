from flask import Flask


def create_app():
    """
    Application factory function.
    """
    app = Flask(__name__)

    # Register blueprints
    from .hello import hello_bp
    from .bank import bank_bp

    app.register_blueprint(hello_bp, url_prefix="/hello")
    app.register_blueprint(bank_bp, url_prefix="/bank")

    return app
