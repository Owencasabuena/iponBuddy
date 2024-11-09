from flask import Flask, flash, redirect, render_template, request
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user
from forms import RegistrationForm 

app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        hashed_password = bcrypt.generate_password_hash()
        return redirect("/login")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    login_user()
    if request.method == "POST":
        return redirect("/home")
    else:
        return render_template("login.html") 

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")