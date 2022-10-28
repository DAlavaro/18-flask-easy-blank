from flask import request
from flask_restx import Resource, Namespace
from model.movie_model import MovieSchema, Movie
from setup_db import db

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        GET /movies — получить все фильмы
        - [ ]  GET /movies?director_id=15?genre_id=3 — получить все фильмы режиссера.
        - [ ]  GET /movies?genre_id=3 — получить все фильмы жанра.
        - [ ]  GET /movies?year=2007 — получить все фильмы за год.
        """
        all_movies = db.session.query(Movie).all()
        # movies = movies_schema.dump(all_movies)
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        if director:
            all_movies = db.session.query(Movie).filter(Movie.director_id == director).all()
        if genre:
            all_movies = db.session.query(Movie).filter(Movie.genre_id == director).all()
        movies = movies_schema.dump(all_movies)
        return movies

    def post(self):
        """
        POST /movies — создать фильм.
        """
        try:
            data_json = request.json
            movie = Movie(**data_json)
            db.session.add(movie)
            db.session.commit()
            return '', 201
        except Exception as e:
            return f'{e}', 404





@movie_ns.route('/<int:id_>/')
class BookView(Resource):

    def get(self, id_: int):
        """
        GET /movies/3 — получить фильм по ID.
        """
        try:
            movies = db.session.query(Movie).filter(Movie.id == id_).one()
            return movie_schema.dump(movies), 200
        except Exception as e:
            return str(e), 404

    def put(self, id_):
        """
        PUT /movies/1 — изменить информацию о фильме.
        """
        data = request.json
        db.session.query(Movie).filter(Movie.id == id_).update(data)
        db.session.commit()

        return "", 204


    def delete(self, id_: int):
        """
        DELETE /movies — удалить фильм.
        """
        movie = db.session.query(Movie).get(id_)
        db.session.delete(movie)
        db.session.commit()

        return "", 204
