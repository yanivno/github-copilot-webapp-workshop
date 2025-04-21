from flask import Flask, render_template, request, jsonify
import json
import logging
from collections import defaultdict

app = Flask(__name__)

# Load movies from JSON file
with open('movies.json', 'r') as file:
    movies = json.load(file)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    logging.info("Rendering index page")
    return render_template('index.html', movies=movies)

@app.route('/api/movies', methods=['GET'])
def get_movies():
    logging.info("Fetching all movies")
    return jsonify(movies)

@app.route('/api/movies', methods=['POST'])
def add_movie():
    new_movie = request.json
    logging.info(f"Adding new movie: {new_movie}")
    new_movie['id'] = len(movies) + 1
    movies.append(new_movie)
    # Save updated movies to JSON file
    with open('movies.json', 'w') as file:
        json.dump(movies, file, indent=4)
    logging.info("Movie added successfully")
    return jsonify(new_movie), 201

@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    logging.info(f"Deleting movie with ID: {movie_id}")
    global movies
    movies = [movie for movie in movies if movie['id'] != movie_id]
    # Save updated movies to JSON file
    with open('movies.json', 'w') as file:
        json.dump(movies, file, indent=4)
    logging.info("Movie deleted successfully")
    return '', 204


@app.route('/directors')
def directors():
    logging.info("Rendering directors page")
    directors_dict = defaultdict(list)
    for movie in movies:
        directors_dict[movie['director']].append(movie)
    return render_template('directors.html', directors=directors_dict)

if __name__ == '__main__':
    logging.info("Starting Flask app")
    app.run(debug=True)
