from dnm import db

class Member(db.Model):
    #local ID
    id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
    member_name = db.Column(db.String, nullable=True)
    member_image = db.Column(db.Text, nullable=True)

class References(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    link = db.Column(db.Text, nullable=True)
=======
    #ID from strapi
    content_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String, nullable=True)
>>>>>>> facd933977807a82fcc9a166e89588161c0f1a96
    image = db.Column(db.Text, nullable=True)
