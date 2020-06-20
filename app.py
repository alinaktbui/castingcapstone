import os
from flask import Flask, request, abort, jsonify, session
from models import Movie, Actor, setup_db, db
from flask_cors import CORS
from auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def index():
        return jsonify({
            'success': True,
        }), 200

# GET all actors
    @app.route('/actors')
    def get_actors():
        selection = Actor.query.order_by(Actor.id).all()
        actors = [actor.format() for actor in selection]

        if selection is None:
            abort(404)

        return jsonify({
            'success': True,
            'actors': actors
        }), 200

# GET all movies
    @app.route('/movies')
    def get_movies():
        selection = Movie.query.order_by(Movie.id).all()
        movies = [movie.format() for movie in selection]

        if selection is None:
            abort(404)

        return jsonify({
            'success': True,
            'movies': movies
        }), 200

# DELETE - delete a actor
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):
        try:
            actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'actor': actor.id
            }), 200

        except ActorDeleteError:
            abort(422)

# DELETE - delete a movie
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, movie_id):
        try:
            movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'movie': movie.id
            }), 200

        except MovieDeleteError:
            abort(422)

# POST - create a new actor
    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actor')
    def create_actor(payload):
        body = request.get_json()

        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')

        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            actor.insert()

            return jsonify({
                'success': True,
                'actor': actor.id
            }), 200

        except CreateActorError:
            abort(422)

# POST - create a new movie
    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movie')
    def create_movie(payload):
        body = request.get_json()

        new_title = body.get('movie_title', None)
        new_release_year = body.get('release_year', None)

        try:
            movie = Movie(movie_title=new_title, release_year=new_release_year)

            movie.insert()

            return jsonify({
                'success': True,
                'movie': movie.id
            }), 200

        except CreateMovieError:
            abort(422)

# PATCH - update a actor
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(payload, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        body = request.get_json()

        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')

        try:
            actor.name = name
            actor.age = age
            actor.gender = gender

            actor.update()

            return jsonify({
                'success': True,
                'actor': actor.id
            }), 200

        except PatchActorError:
            abort(422)

# PATCH - updated a movie
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(payload, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        body = request.get_json()

        movie_title = body.get('movie_title')
        release_year = body.get('release_year')

        try:
            movie.movie_title = movie_title
            movie.release_year = release_year

            movie.update()

            return jsonify({
                'success': True,
                'movie': movie.id
            }), 200

        except PatchMovieError:
            abort(422)

# Error Handlers

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(405)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessible(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessible entity"
        }), 422

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal error"
        }), 500

    '''
    @TODO implement error handler for AuthError
        error handler should conform to general task above
    '''
    @app.errorhandler(AuthError)
    def autherror(error):
        return jsonify({
            "success": False,
            "error": error.error,
            "message": error.status_code
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
