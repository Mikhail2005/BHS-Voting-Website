

from website import db


class Prefects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    profile_picture = db.Column(db.String())
    
    division_id = db.Column(db.Integer)
   
    