
from app import db

class DBModel():
    """Superclass for all database models"""

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    date_updated = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


movies_actors = db.Table('movies_actors',
    db.Column('movies_id', db.Integer, db.ForeignKey('movies.id')),
    db.Column('actors_id', db.Integer, db.ForeignKey('actors.id'))
)

movies_genres = db.Table('movies_genres',
    db.Column('movies_id', db.Integer, db.ForeignKey('movies.id')),
    db.Column('genres_id', db.Integer, db.ForeignKey('genres.id'))
)

class Movie(db.Model, DBModel):

    __tablename__ = 'movies'

    # IMDb data
    imdb_id     = db.Column(db.String(20))
    title       = db.Column(db.String(255))
    plot        = db.Column(db.String(2047))
    year        = db.Column(db.Integer)
    rating      = db.Column(db.Integer)
    genres      = db.relationship('Genre', secondary=movies_genres,
                    backref=db.backref('movies', lazy='dynamic'))
    actors      = db.relationship('Actor', secondary=movies_actors,
                    backref=db.backref('movies', lazy='dynamic'))

    # User specified data
    user_summary    = db.Column(db.String(2047))
    user_rating     = db.Column(db.Integer)
    user_seen       = db.Column(db.Integer)

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        #self.actor = actor

    def __repr__(self):
        return "Movie: {}".format(self.title)

    @property
    def serialize(self):
        ''' Serializes the Movie object into a JSON object '''
        return {
                'id'        : self.id,
                'imdb_id'   : self.imdb_id,
                'title'     : self.title,
                }


class Genre(db.Model, DBModel):

    __tablename__ = 'genres'

    genre = db.Column(db.String(20))

    def __init__(self, genre):
        self.genre = genre

    def __repr__(self):
        return self.genre

class Actor(db.Model, DBModel):

    __tablename__ = 'actors'

    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
