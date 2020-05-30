from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Creating an unconfigured Flask-SQLAlchemy instance
db = SQLAlchemy()

# Models.


class Actor(db.Model):
    """
    Actor Model to create actor table in postgres
    Each Actor must have a name, age, gender
    """
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)

    def get_actorname(self):
        """returns actor name
        Example
          `name = Actor.get_actorname `
        """
        return self.name

    def insert(self):
        """inserts new actor record
        Example
         `actor = Actor(name=name, age=age, gender=gender)`
         `actor.insert()`
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """deletes an actor record
        the actor row must exists in the table
        Example
          `actor = Actor.query.get(actor_id)`
          `actor.delete()`
        """
        db.session.delete(self)
        db.session.commit()

    def update(self):
        """ updates columns in a row
        the actor row must exist
        Example
          `actor = Actor.query.get(actor_id)`
          `actor.age = 25`
          `actor.update()`
        """
        db.session.commit()

    def format(self):
        """returns actor information in formated response
        """
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


class Movie(db.Model):
    """
    Movie Model to create movies table in postgres
    Each Movie must have a title and release date
    """
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime(), default=datetime.utcnow)

    def get_title(self):
        """returns movie title
        Example
          `title = Movie.get_title`
        """
        return self.title

    def insert(self):
        """inserts new movie record
        Example
         `movie = Movie(title=title, release_date=release_date)`
         `movie.insert()`
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """deletes a movie record
        the movie row must exists in the table
        Example
          `movie = Movie.query.get(movie_id)`
          `movie.delete()`
        """
        db.session.delete(self)
        db.session.commit()

    def update(self):
        """ updates columns in a row
        the movie row must exist
        Example
          `movie = Movie.query.get(movie_id)`
          `movie.title = 'movie tile new'`
          `movie.update()`
        """
        db.session.commit()

    def format(self):
        """returns movie information in formated response
        """
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }
