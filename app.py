from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# from waitress import serve

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # database file stored in /instance/portfolio.db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/portfolio.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # REGISTER BLUEPRINTS
    from my_port import port_bp
    from calculate import calculate_bp

    app.register_blueprint(port_bp, url_prefix="/")
    app.register_blueprint(calculate_bp, url_prefix="/calculate")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, use_reloader=True)

