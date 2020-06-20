import os
from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Movie
Title and release year
'''
class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(db.Integer, primary_key=True)
    movie_title = Column(db.String)
    release_year = Column(db.Integer)

    def __init__(self, movie_title, release_year):
        self.movie_title = movie_title
        self.release_year = release_year

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'movie_title': self.movie_title,
            'release_year': self.release_year
        }


'''
Actors with attributes name, age and gender
'''


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    age = Column(db.Integer)
    gender = Column(db.String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }