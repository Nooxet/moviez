from app import app, models
from flask import jsonify

@app.route('/')
def index():
    return "This is no place for someone like you..."

@app.route('/movies')
def get_movies():
    ''' Returns a list of all movies '''
    movies = models.Movie.query.all()
    return jsonify([m.serialize for m in movies])

@app.route('/add')
def add():
    slj = models.Actor('Samuel L. Jackson')
    bw = models.Actor('Bruce Willys')

    m = models.Movie('Pulp Fiction', 5)
    m.actors.append(slj)
    m.actors.append(bw)
    m.save()

    mm = models.Movie('Breaking Bad', 5)
    mm.actors.append(bw)
    mm.save()

    return "Added!"
