from dnm import db


class Member(db.Model):
    # local ID
    id = db.Column(db.Integer, primary_key=True)
    # ID from strapi
    content_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String, nullable=True)
    image = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Member('{self.name}')"


class Resource(db.Model):
    # local ID
    id = db.Column(db.Integer, primary_key=True)
    # ID from strapi
    content_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String, nullable=True)
    link = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Resource('{self.name}')"
