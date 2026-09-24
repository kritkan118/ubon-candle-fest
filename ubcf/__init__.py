import os, secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ubcandle_db.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/ubcandledb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password><username>.mysql.pythonanywhere-services.com/<username>$<database_name>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ubcf2026_06aw_user:NTUO64mQgC9nrazqXkPqZWjgFySi6zbM@dpg-daqaft0jo6nc73do5c1g-a.oregon-postgres.render.com/ubcf2026_06aw'
app.config['SECRET_KEY'] = b'secretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from ubcf import routes, models