# Getting Started

Heroku link:

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
export FLASK_APP=app.py
flask run --reload
```

## Endpoints
GET '/actors'
GET '/movies'
POST '/actors/create'
POST '/movies/create'
PATCH '/actors/<int:actor_id>'
PATCH '/movies/<int:movie_id>'
DELETE '/actors/<int:actor_id>'
DELETE '/movies/<int:movie_id>'


To run the server, execute:

```bash
export FLASK_APP=app.py FLASK_DEBUG=True
flask run --reload
```

GET Actors
curl http://127.0.0.1:5000/actors
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

GET Movies
curl http://127.0.0.1:5000/movies
{"movies":[{"id":1,"movie_title":"Titanic","release_year":1997},{"id":2,"movie_title":"Romeo + Juliet","release_year":1996},{"id":3,"movie_title":"The Greatest Showman","release_year":2017},{"id":4,"movie_title":"La La Land","release_year":2016}],"success":true}
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


POST Actor 
curl http://127.0.0.1:5000/actors/create -X POST -H "Content-Type: application/json" -d '{"name": "New Actor", "age": 20, "gender": "Female"}'
curl http://127.0.0.1:5000/actors/create -X POST --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ6VHVFcnAyNTB6SVlKVlV4OU1FTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZXIyczB5MC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjYzVhOWJiM2MyOTIwYzVjMzI4YmYwIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5MjYyNzI3NiwiZXhwIjoxNTkyNzEzNjc2LCJhenAiOiI2TlFsaTNCQVhVRTNyN3E3VXdMbTZ1OFZiNVlCNUlRUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.c1uKGnA_Tjb8DAkWs-2f_fD1ovpmbDMORujHFh4v9XYEgypmIe2Jt3oD4NYZNQBdPJz1dr9egIZR5-GH3cZTdOrEptqxQfHM_vE3mN9yMRywnTCl0rZiI_Q_6K1a6YZPX5L_l4s4pZibZpGMZSwa-TFR4hnX4uu7P0xdGA75CZz3mnEgwkCojNCr5eGR5jRz2O3Vzi5VM5be-H4mXrsu5MLaVCsurdsxuOHsEwI_s38Z4H-L9Kx0gO1mu5WprxeOsMS5SRzk1VEvFwOiofFRm8UxGVfbHh9tzZUYlbRpviZHpmodCHdjIpLyLRZvTeCqNCVpkiTYmroezzvOSfmYsQ' --header 'Content-Type: application/json' -d '{"name":"New Actor Name", "age": 30, "gender": "Male"}'
{
  "actor": 15, 
  "success": true
}

POST Movie
curl http://127.0.0.1:5000/movies/create -X POST -H "Content-Type: application/json" -d '{"movie_title": "New Movie", "release_year": 2021}'
curl http://127.0.0.1:5000/movies/create -X POST --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ6VHVFcnAyNTB6SVlKVlV4OU1FTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZXIyczB5MC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjYzVhOWJiM2MyOTIwYzVjMzI4YmYwIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5MjYyNzI3NiwiZXhwIjoxNTkyNzEzNjc2LCJhenAiOiI2TlFsaTNCQVhVRTNyN3E3VXdMbTZ1OFZiNVlCNUlRUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.c1uKGnA_Tjb8DAkWs-2f_fD1ovpmbDMORujHFh4v9XYEgypmIe2Jt3oD4NYZNQBdPJz1dr9egIZR5-GH3cZTdOrEptqxQfHM_vE3mN9yMRywnTCl0rZiI_Q_6K1a6YZPX5L_l4s4pZibZpGMZSwa-TFR4hnX4uu7P0xdGA75CZz3mnEgwkCojNCr5eGR5jRz2O3Vzi5VM5be-H4mXrsu5MLaVCsurdsxuOHsEwI_s38Z4H-L9Kx0gO1mu5WprxeOsMS5SRzk1VEvFwOiofFRm8UxGVfbHh9tzZUYlbRpviZHpmodCHdjIpLyLRZvTeCqNCVpkiTYmroezzvOSfmYsQ' --header 'Content-Type: application/json' -d '{"movie_title":"New Movie", "release_year": 2020}'
{
  "movie": 6, 
  "success": true
}


DELETE Actor
curl -X DELETE http://127.0.0.1:5000/actors/5
curl http://127.0.0.1:5000/actors/10 -X DELETE -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ6VHVFcnAyNTB6SVlKVlV4OU1FTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZXIyczB5MC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5YjZlYTBkZTQzMWEwYzhkNjQ5ZTdhIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5MjYyNzIwOCwiZXhwIjoxNTkyNzEzNjA4LCJhenAiOiI2TlFsaTNCQVhVRTNyN3E3VXdMbTZ1OFZiNVlCNUlRUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.j2rYTfNkFJpJyVqO5C069bWvNqx-ud9IJrBGu6z2D8WwVw3FLheiOFKFcLOFVa0_sUmdUSljrS698sNdGxUE3o7FiOwitj7zR8hEk_ixFjckIKv5I_DxuPPefND9n450CyXuLxhHBnKYotE8m7QgxgwpsGS1jaDgRg3txUGrnZm3PshctRLdyMGPMehHMHGFt4n8GVnEFKIZ0kOAyhw_iPOHKp3q9lL4GqVl--GDixGFObtldAX529Ss04nLWRl--WMGfkuRzM90XJc3xsX98BJLOc-H5-0OAngNKEx0fsYK1vCuPAW1PjiaRWfGF89FIyT7wNJCpYSwWWylZqFjVw' 
{
  "actor": 10, 
  "success": true
}


DELETE Movie
curl -X DELETE http://127.0.0.1:5000/movies/5
curl http://127.0.0.1:5000/actors/6 -X DELETE -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ6VHVFcnAyNTB6SVlKVlV4OU1FTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZXIyczB5MC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5YjZlYTBkZTQzMWEwYzhkNjQ5ZTdhIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5MjYyNzIwOCwiZXhwIjoxNTkyNzEzNjA4LCJhenAiOiI2TlFsaTNCQVhVRTNyN3E3VXdMbTZ1OFZiNVlCNUlRUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.j2rYTfNkFJpJyVqO5C069bWvNqx-ud9IJrBGu6z2D8WwVw3FLheiOFKFcLOFVa0_sUmdUSljrS698sNdGxUE3o7FiOwitj7zR8hEk_ixFjckIKv5I_DxuPPefND9n450CyXuLxhHBnKYotE8m7QgxgwpsGS1jaDgRg3txUGrnZm3PshctRLdyMGPMehHMHGFt4n8GVnEFKIZ0kOAyhw_iPOHKp3q9lL4GqVl--GDixGFObtldAX529Ss04nLWRl--WMGfkuRzM90XJc3xsX98BJLOc-H5-0OAngNKEx0fsYK1vCuPAW1PjiaRWfGF89FIyT7wNJCpYSwWWylZqFjVw'
{
  "movie": 6, 
  "success": true
}


PATCH Actor
curl http://127.0.0.1:5000/actors/ -X PATCH -H "Content-Type: application/json" -d '{"name":"New Updated Name", "age": 40, "gender": "Male"}'

curl http://127.0.0.1:5000/actors/7 -X PATCH --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ6VHVFcnAyNTB6SVlKVlV4OU1FTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZXIyczB5MC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjYzVhOWJiM2MyOTIwYzVjMzI4YmYwIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5MjYyNzI3NiwiZXhwIjoxNTkyNzEzNjc2LCJhenAiOiI2TlFsaTNCQVhVRTNyN3E3VXdMbTZ1OFZiNVlCNUlRUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.c1uKGnA_Tjb8DAkWs-2f_fD1ovpmbDMORujHFh4v9XYEgypmIe2Jt3oD4NYZNQBdPJz1dr9egIZR5-GH3cZTdOrEptqxQfHM_vE3mN9yMRywnTCl0rZiI_Q_6K1a6YZPX5L_l4s4pZibZpGMZSwa-TFR4hnX4uu7P0xdGA75CZz3mnEgwkCojNCr5eGR5jRz2O3Vzi5VM5be-H4mXrsu5MLaVCsurdsxuOHsEwI_s38Z4H-L9Kx0gO1mu5WprxeOsMS5SRzk1VEvFwOiofFRm8UxGVfbHh9tzZUYlbRpviZHpmodCHdjIpLyLRZvTeCqNCVpkiTYmroezzvOSfmYsQ' --header 'Content-Type: application/json' -d '{"name":"New Updated Name", "age": 40, "gender": "Male"}'
{
  "actor": 7, 
  "success": true
}

PATCH Movie
curl http://127.0.0.1:5000/movies/5 -X PATCH -H "Content-Type: application/json" -d '{"movie_title":"Updated Title", "release_year": 2050}'

Executive Producer
curl http://127.0.0.1:5000/movies/5 -X PATCH --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ6VHVFcnAyNTB6SVlKVlV4OU1FTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZXIyczB5MC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjYzVhOWJiM2MyOTIwYzVjMzI4YmYwIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5MjYyNzI3NiwiZXhwIjoxNTkyNzEzNjc2LCJhenAiOiI2TlFsaTNCQVhVRTNyN3E3VXdMbTZ1OFZiNVlCNUlRUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.c1uKGnA_Tjb8DAkWs-2f_fD1ovpmbDMORujHFh4v9XYEgypmIe2Jt3oD4NYZNQBdPJz1dr9egIZR5-GH3cZTdOrEptqxQfHM_vE3mN9yMRywnTCl0rZiI_Q_6K1a6YZPX5L_l4s4pZibZpGMZSwa-TFR4hnX4uu7P0xdGA75CZz3mnEgwkCojNCr5eGR5jRz2O3Vzi5VM5be-H4mXrsu5MLaVCsurdsxuOHsEwI_s38Z4H-L9Kx0gO1mu5WprxeOsMS5SRzk1VEvFwOiofFRm8UxGVfbHh9tzZUYlbRpviZHpmodCHdjIpLyLRZvTeCqNCVpkiTYmroezzvOSfmYsQ' --header 'Content-Type: application/json' -d '{"movie_title":"New Updated Title", "release_year": 2050}'

{
  "movie": 5, 
  "success": true
}