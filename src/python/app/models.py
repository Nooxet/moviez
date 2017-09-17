
from app import db

class Movie(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    rating = db.Column(db.Integer)

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "Movie: {}".format(self.name)
