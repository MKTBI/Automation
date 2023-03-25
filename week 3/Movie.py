from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/movies', methods=['POST'])
def create_movie():
    title = request.json['title']
    description = request.json['description']
    year = request.json['year']
    director = request.json['director']

    return jsonify({'status': 'success', 'message': 'Movie added successfully'})

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = []
    
    for row in movies:
        movie = {'id': row[0], 'title': row[1], 'description': row[2], 'year': row[3], 'director': row[4]}
        movies.append(movie)

    return jsonify(movies)