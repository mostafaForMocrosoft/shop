from flask import Flask, session
from app.config import BASE_DIR
from os import path
from app import extensions
from app import auth
from datetime import timedelta
import secrets
import redis

# it is very important
# session.clear()
# session["user_id"] = user.id

r = redis.Redis("localhost", port=6379, decode_responses=True)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(path.join(BASE_DIR, "shop.sqlite3"))
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = secrets.token_hex(856)
    app.config['SQLALCHEMY_TRACH_MODIFICATIONS'] = False
    app.config["SESSION_COOKIE_PATH"] = "/"
    app.config["SESSION_COOKIE_NAME"] = "shop"

    app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='ُStrict',
    )

    app.permanent_session_lifetime = timedelta(hours=1)
    session.permanent = True

    extensions.db.init_app(app)

    app.register_blueprint(auth.auth)

    return app