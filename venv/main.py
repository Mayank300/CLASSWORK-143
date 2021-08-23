from flask import Flask, request, jsonify
import csv
from demo_graphic import output
from content_filter import getRecomendation
from storage import liked_movies,disliked_movies,unwatched_movies,all_movies
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/get-movies')

def get_movies():
    movie_data = {
        'title': all_movies[0][19],
        'poster_link': all_movies[0][27],
        'release_date': all_movies[0][13] or 'n/a',
        'dureation': all_movies[0][15],
        'rating': all_movies[0][20],
        'overview': all_movies[0][9],
    }
    return jsonify({
        'data': movie_data,
        'status': 'success 😻',
    })

@app.route('/liked-movies', methods=['POST'])

def liked_movies():
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status': 'success',
    }),200

@app.route('/disliked-movies', methods=['POST'])
 
def disliked_movies():
    movie = all_movies[0]
    disliked_movies.append(movie)
    disliked_movies.pop(0)
    return jsonify({
        'status': 'success',
    }),200


@app.route('/unwatched-movies', methods=['POST'])
 
def unwatched_movies():
    movie = all_movies[0]
    unwatched_movies.append(movie)
    unwatched_movies.pop(0)
    return jsonify({
        'status': 'success',
    }),200

@app.route('/recomanded-movies')

def recomanded_movies():
    all_recomendation = []
    for liked_movie in liked_movies:
        recomendation = getRecomendation(liked_movie[19])
        for i in recomendation:
            all_recomendation.append(i)

    import itertools

    all_recomendation.sort()
    all_recomendation = list(all_recomendation for  all_recomendation,_ in itertools.groupby(all_recomendation))
    movie_data = []
    for i in all_recomendation:
        d = {
            'title': i[0],
            'poster_link': i[1],
            'release_date': i[2] or 'n/a',
            'dureation': i[3],
            'rating': i[4],
            'overview': i[5],
        }
        movie_data.append(d)
    return jsonify({
        'data': movie_data,
        'status': 'success 🙂',
    }),200


@app.route('/popular-movies')

def popular_movies():
    movie_data = []
    for i in output:
        d = {
            'title': i[0],
            'poster_link': i[1],
            'release_date': i[2] or 'n/a',
            'dureation': i[3],
            'rating': i[4],
            'overview': i[5],
        }
        movie_data.append(d)
    return jsonify({
        'data': movie_data,
        'status': 'success 🙂',
    }),200


if __name__ == '__main__':
    app.run(debug=True)