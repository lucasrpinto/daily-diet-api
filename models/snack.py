from pymysql import Date
from database import db

class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(30), nullable=False)
    description = db.Column(db.text, nullable=False)
    date = db.Column(db.Date, default=Date.utcnow, nullable=False)
    diet = db.Column(db.Boolean, default=True)