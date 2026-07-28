from flask import Blueprint
from app.config import BASE_DIR, path

auth = Blueprint("auth", __name__, url_prefix="/auth", static_folder=path.join(BASE_DIR, "app", "static"), template_folder=path.join(BASE_DIR, "app", "templates"))

import app.auth.routes