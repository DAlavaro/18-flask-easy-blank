from flask_restx import Namespace, Resource
from model.genre_model import GenreSchema, Genre
from setup_db import db

genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresViews(Resource):
    def get(self):
        """
            Формирование представления для получения жанров
        """
        try:
            all_genres = db.session.query(Genre).all()
            return genres_schema.dump(all_genres)
        except Exception as e:
            return f'{e}', 404


@genres_ns.route('/<id_>')
class GenreViews(Resource):
    def get(self, id_):
        """
            Формирование представления для получения жанра по id
            В случае отсутствия фильма - ошибка
        """
        try:
            genre = db.session.query(Genre).filter(Genre.id == id_).one()
            return genre_schema.dump(genre), 200
        except Exception as e:
            return f'{e}', 404
