from datetime import date
from database import db

class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, default=date.today, nullable=False)
    diet = db.Column(db.Boolean, default=True)
