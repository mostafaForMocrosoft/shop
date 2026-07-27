from flask import Flask
from app.config import BASE_DIR
from os import path
from app import extensions
from app import auth

def create_app():


    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(path.join(BASE_DIR, "shop.sqlite3"))
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = "laskldaklsdlaksldaksllda".encode()
    app.config['SQLALCHEMY_TRACH_MODIFICATIONS'] = False
    
    app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    )

    extensions.db.init_app(app)

    app.register_blueprint(auth.auth)

    return app