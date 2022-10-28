# импорт библиотек
from flask import Flask
from flask_restx import Api

# импорт конфигурации и базы данных
from config import Config
from setup_db import db

# импорт нэймспэйсов
from views.movies_ns import movie_ns
from views.directors_ns import directors_ns
from views.genres_ns import genres_ns


# Функция будет создавать приложение и возвращать его
def create_app(config_object) -> Flask:
    """
    Создаем app
    """
    app = Flask(__name__)
    # задаем конфигурацию приложения вызвав специальный метод from_object
    app.config.from_object(config_object)
    # применяем конфигурацию чтобы Flask по всему приложению ее применил во все будущие компоненты
    configure_app(app)
    return app


def configure_app(app: Flask):
    """
    Подключаем namespace
    """
    # обращаемся к базе данных и вызываем метод init_app
    db.init_app(app)
    api = Api(app)
    # вместо создания namespace реализуем добавление
    api.add_namespace(movie_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="localhost", port=10001, debug=True)
