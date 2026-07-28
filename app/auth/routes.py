from app.auth import auth
from flask import request, flash, redirect, url_for, render_template
from app.models.user import User
from app.extensions import db

@auth.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        
        try:
            user = User(username = username, email=email, password=password, role="writer")
            db.session.add(user)
            db.session.commit()
            flash("شما با موفقیت ثبت نام کردید")
            return redirect(url_for("auth.login"))
        except Exception as ex:
            print("error: " + str(ex))
            flash("سرور با خطایی مواجه شد")
            return redirect(url_for("auth.register"))
    else:
        return render_template("auth/register.html")