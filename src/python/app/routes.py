from app import app, models

@app.route('/')
def index():
    m = models.Movie('Pulp Fiction', 5)
    m.save()
    return "Hello, World"
