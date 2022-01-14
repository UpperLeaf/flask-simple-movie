from flask import Flask, request, Response
from flask_restx import Resource, Api, fields
from flask import abort, jsonify


app = Flask(__name__)
api = Api(app)

ns_movies = api.namespace('ns_movies', description='Movie APIs')

movie_data = api.model(
    'Movie Data',
    {
        "movie_name": fields.String(description="Movie name", required=True),
        "movie_description": fields.String(description="Movie Description", required=True),
        "movie_image_url": fields.String(description="Movie Image URL"),
        "movie_director": fields.String(description="Movie Director"),
        "movie_published_at": fields.Date(descrption="Movie Published Date")
    }
)

movies = {}
count_of_movies = len(movies.keys())

@ns_movies.route('/movies')
class Movie(Resource):

    def get(self):
        return {
            'number_of_movies': len(movies.keys()),
            'movies': movies
        }

    @api.expect(movie_data)
    def post(self):
        global count_of_movies
        idx = count_of_movies
        count_of_movies += 1

        params = request.get_json()
        params['movie_id'] = idx
        movies[idx] = params
        return Response(status=200)

@ns_movies.route('/movies/<int:movie_id>')
class MovieInfo(Resource):
    def get(self, movie_id):
        if not movie_id in movies.keys():
            abort(status=404, description=f"Movie Not Found")

        return {
            'movie_id': movie_id,
            'data': movies[movie_id]
        }

    @api.expect(movie_data)
    def put(self, movie_id):
        if not movie_id in movies.keys():
            abort(status=404, description=f"Movie Not Found")

        movies[movie_id] = request.get_json()
        return Response(status=200)

    def delete(self, movie_id):
        if not movie_id in movies.keys():
            abort(status=404, description=f"Movie Not Found")

        del movies[movie_id]
        return Response(status=200)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)