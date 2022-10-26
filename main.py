from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.movies_ns import movie_ns


# Функция будет создавать приложение и возвращать его
def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    # задаем конфигурацию приложения вызвав специальный метод from_object
    application.config.from_object(config)
    # применяем конфигурацию чтобы Фласк по всему приложению ее применил во все будущие компоненты
    application.app_context().push()
    return application



def configure_app(application: Flask):
    # обращаемся к базе данных и вызываем метод init_app
    db.init_app(application)
    api = Api(app)
    # вместо создания namespace реализуем добавление
    api.add_namespace(movie_ns)
    # api.add_namespace(author_ns)
    # api.add_namespace(book_ns)


def load_data(app, db):
   m1 = Movie

app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run(host="localhost", port=10001, debug=True)



