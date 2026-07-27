from app.auth import auth

@auth.route("/")
def authe():
    return "auth"