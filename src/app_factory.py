from flask import Flask
from flask_socketio import SocketIO

from src.config.database import db

socketio = SocketIO(cors_allowed_origins="*")


def create_app():
    from src.routers.payment_routes import payment_bp
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SECRET_KEY"] = "SECRET_KEY_WEBSOCKET"

    db.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(payment_bp)

    return app
