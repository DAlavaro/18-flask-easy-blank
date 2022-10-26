from flask_restx import Resource, Namespace
from app.container import movie_dao

from app.dao.model.movie_model import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_schema('/')
class MoviesSchema(Resource):
    def get(self):
        all_movies = movie_dao.get_all()
        return movie_schema.dump((all_movies)), 200



