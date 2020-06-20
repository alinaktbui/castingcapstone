# The Casting Agency

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Getting Started

Heroku link: https://castingcapstone.herokuapp.com/

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server
To run the server, execute:

```bash
export FLASK_APP=app.py FLASK_DEBUG=True
flask run --reload
```

## Roles
* Casting Assistant - Can view actors and movies
* Casting Director - All permissions a Casting Assistant, can add or delete an actor from the database
* Executive Producer - All permissions a Casting Director has, can add or delete a movie from the database, AND can modify actors or movies

## Endpoints
* GET '/actors'
* GET '/movies'
* POST '/actors/create'
* POST '/movies/create'
* PATCH '/actors/<int:actor_id>'
* PATCH '/movies/<int:movie_id>'
* DELETE '/actors/<int:actor_id>'
* DELETE '/movies/<int:movie_id>'


#### GET Actors
curl http://127.0.0.1:5000/actors
```
{
  "actors": [
    {
      "age": 45, 
      "gender": "Male", 
      "id": 1, 
      "name": "Leonardo DiCaprio"
    }, 
    {
      "age": 41, 
      "gender": "Female", 
      "id": 2, 
      "name": "Claire Danes"
    }, 
    {
      "age": 32, 
      "gender": "Male", 
      "id": 3, 
      "name": "Zac Efron"
    }, 
    {
      "age": 31, 
      "gender": "Female", 
      "id": 4, 
      "name": "Emma Stone"
    }, 
    {
      "age": 40, 
      "gender": "Male", 
      "id": 7, 
      "name": "New Updated Name"
    }, 
    {
      "age": 40, 
      "gender": "Updated Name", 
      "id": 9, 
      "name": "Updated Name"
    }, 
    {
      "age": 30, 
      "gender": "Male", 
      "id": 15, 
      "name": "New Actor Name"
    }
  ], 
  "success": true
}
```

#### GET Movies
curl http://127.0.0.1:5000/movies
```
{
  "movies": [
    {
      "id": 1, 
      "movie_title": "Titanic", 
      "release_year": 1997
    }, 
    {
      "id": 2, 
      "movie_title": "Romeo + Juliet", 
      "release_year": 1996
    }, 
    {
      "id": 3, 
      "movie_title": "The Greatest Showman", 
      "release_year": 2017
    }, 
    {
      "id": 4, 
      "movie_title": "La La Land", 
      "release_year": 2016
    }, 
    {
      "id": 5, 
      "movie_title": "New Updated Title", 
      "release_year": 2050
    }
  ], 
  "success": true
} 
```

#### POST Actor 
curl http://127.0.0.1:5000/actors/create -X POST --header 'Authorization: Bearer ADD_TOKEN_HERE' --header 'Content-Type: application/json' -d '{"name":"New Actor Name", "age": 30, "gender": "Male"}'

```
{
  "actor": 15, 
  "success": true
}
```

#### POST Movie
curl http://127.0.0.1:5000/movies/create -X POST -H "Content-Type: application/json" -d '{"movie_title": "New Movie", "release_year": 2021}'
curl http://127.0.0.1:5000/movies/create -X POST --header 'Authorization: Bearer ADD_TOKEN_HERE' --header 'Content-Type: application/json' -d '{"movie_title":"New Movie", "release_year": 2020}'

```
{
  "movie": 6, 
  "success": true
}
```

#### DELETE Actor
curl -X DELETE http://127.0.0.1:5000/actors/5
curl http://127.0.0.1:5000/actors/10 -X DELETE -H 'Authorization: Bearer ADD_TOKEN_HERE' 

```
{
  "actor": 10, 
  "success": true
}
```

#### DELETE Movie
curl http://127.0.0.1:5000/actors/6 -X DELETE -H 'Authorization: Bearer ADD_TOKEN_HERE'
```
{
  "movie": 6, 
  "success": true
}
```

#### PATCH Actor
curl http://127.0.0.1:5000/actors/7 -X PATCH --header 'Authorization: Bearer ADD_TOKEN_HERE' --header 'Content-Type: application/json' -d '{"name":"New Updated Name", "age": 40, "gender": "Male"}'
```
{
  "actor": 7, 
  "success": true
}
```

#### PATCH Movie
curl http://127.0.0.1:5000/movies/5 -X PATCH --header 'Authorization: Bearer ADD_TOKEN_HERE' --header 'Content-Type: application/json' -d '{"movie_title":"New Updated Title", "release_year": 2050}'
```
{
  "movie": 5, 
  "success": true
}
```
## Endpoints
To run tests, execute:

```bash
python3 test_app.py
```
* if you experience errors, run the files in .env before running python3 test_app.py
