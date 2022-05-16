from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    meterID_1 = db.Column(db.Integer)
    meterID_2 = db.Column(db.Integer)
    meterID_3 = db.Column(db.Integer)
    meterID_4 = db.Column(db.Integer)

    #meter = db.relationship('MeterID')

#class MeterID(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    meterID_1 = db.Column(db.Integer)
#    meterID_2 = db.Column(db.Integer)
#    meterID_3 = db.Column(db.Integer)
#    meterID_4 = db.Column(db.Integer)
#    meterID_5 = db.Column(db.Integer)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))