from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import upgrade, Migrate
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_login.mixins import UserMixin

import pymysql

from wtforms import StringField, PasswordField
from wtforms.validators import Length, Email

from werkzeug.security import generate_password_hash, check_password_hash

from dash_application import create_dash_kpi1, create_dash_kpi2, create_dash_kpi3, create_dash_kpi4, create_dash_kpi5, create_dash_kpi6

app = Flask(__name__)
app.config["SECRET_KEY"] = "THIS IS A SECRET"       ##REPLACE LATER

#LOCAL SETUP
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

#CLOUD SETUP
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Ic8JErjp39oaGwEe@/users?unix_socket=/cloudsql/tip-kilian-martin:europe-west1:tip-kilian-martin"



Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager()
login.init_app(app)
create_dash_kpi1(app)
create_dash_kpi2(app)
create_dash_kpi3(app)
create_dash_kpi4(app)
create_dash_kpi5(app)
create_dash_kpi6(app)



@login.user_loader
def user_loader(user_id):
    return User.query.filter_by(id = user_id).first()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)  ##ALSO ADD ROLE HERE
    password = db.Column(db.String(128), nullable=False)
    




class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[Length(min=5)])


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[Length(min=5)])
    repeat_password = PasswordField("Repeate Password", validators=[Length(min=5)])



@app.route("/")
@app.route("/index/<item_type>")
def index(item_type="All"):
    
    return render_template("index.html", item_type=item_type)

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if check_password_hash(user.password, form.password.data):
            login_user(user)

            return redirect(url_for('index'))

        ##implement failed attempt

    return render_template("login.html", form=form)

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit() and form.password.data == form.repeat_password.data:
        user = User(
            email = form.email.data,
            password = generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))
    ##IMplement failed login attempt


    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/dashboards/<dashboard>")
def dashboards(dashboard):
    #print(dashboard, flush=True)

    return render_template("dashboards.html", dashboard=dashboard)


@app.route('/admin/dbupgrade/<key>')      ##Consider replacing; not very secure
def dbupgrade():
    if key == "jsisid83jd8dajkdsjkdsjk":
        migrate = Migrate(app, db)
        upgrade(directory=migrate.directory)
        return 'migrated'
    else:
        return 'unauthorized'


@app.route("/slides")
def slides():

    return render_template("slides.html")


"""

if __name__ == "__main__":
    app.run(debug=True)
"""