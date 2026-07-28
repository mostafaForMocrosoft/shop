from app.auth import auth
from flask import request, flash, redirect, url_for, render_template, session
from app.models.user import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

@auth.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        
        try:
            user = User(username = username, email=email, password=generate_password_hash(password), role="writer")
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
    

@auth.route("/login", methods = ['GET', "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    session['user_id'] = user.id
                    session['role'] = user.role
                    return "شما با موفقیت وارد شدید"
                else:
                    flash("رمز عبور اشتباه است")
                    return redirect(url_for("auth.login"))
            else:
                flash("ایمیل اشتباه است")
                return redirect(url_for("auth.login"))
        except Exception as ex:
            print(ex)
            flash("سرور با خطایی مواجه شد")
            return redirect(url_for("auth.login"))
    return render_template("auth/login.html")