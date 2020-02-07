from dnm import db

class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String, nullable=True)
    member_image = db.Column(db.Text, nullable=True)

class References(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    link = db.Column(db.Text, nullable=True)
    image = db.Column(db.Text, nullable=True)
