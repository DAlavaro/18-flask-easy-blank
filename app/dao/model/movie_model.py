from marshmallow import Schema, fields
from app.setup_db import db



class Movie(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer)
    director_id = db.Column(db.Integer)

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    name = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()