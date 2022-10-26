from app.dao.model import movie_model

# CRUD (Создание, чтение, обновление, удаление)
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(movie_model).all()