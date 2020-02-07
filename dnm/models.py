from dnm import db

class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    image = db.Column(db.Text, nullable=True)
