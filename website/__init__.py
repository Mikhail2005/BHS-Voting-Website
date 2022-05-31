from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "WESRDTFYGUHIJOK"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Voting Website.db'


db = SQLAlchemy(app)

from website import models
from website import views



