from app.dao.movie_dao import MovieDAO
from app.services.movie_service import MovieService
from app.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)