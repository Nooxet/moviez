from app import app, models

@app.route('/')
def index():
    # get all actors for the movie
    m = models.Movie.query.get(1)
    print (m)
    print ([i for i in m.actors])

    # get all movies for the actor
    a = models.Actor.query.get(2)
    print ("Actor", a)
    print ([i for i in a.movies])
    return "Got"

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
