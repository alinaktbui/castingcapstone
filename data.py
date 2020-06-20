import psycopg2

connection = psycopg2.connect('dbname=casting_test user=postgres password=dbpass')

cursor = connection.cursor()

# # cursor.execute("""
# #   CREATE TABLE movies (
# #     id INTEGER PRIMARY KEY,
# #     movie_title VARCHAR NOT NULL,
# #     release_year INTEGER
# #   );
# # """)

SQL = 'INSERT into movies (id, movie_title, release_year) VALUES (%(id)s, %(movie_title)s, %(release_year)s);'

# data = {
#   'id': 1,
#   'movie_title': 'Titanic',
#   'release_year': 1997
# }

# data = {
#   'id': 2,
#   'movie_title': 'Romeo + Juliet',
#   'release_year': 1996
# }

# data = {
#   'id': 3,
#   'movie_title': 'The Greatest Showman',
#   'release_year': 2017
# }

# data = {
#   'id': 4,
#   'movie_title': 'La La Land',
#   'release_year': 2016
# }

# data = {
#   'id': 5,
#   'movie_title': 'La La Land',
#   'release_year': 2016
# }

# cursor.execute(SQL, data)
# connection.commit()

# cursor.execute("""
#   CREATE TABLE actors (
#     id INTEGER PRIMARY KEY,
#     name VARCHAR NOT NULL,
#     age INTEGER,
#     gender VARCHAR NOT NULL,
#     movie_id INTEGER REFERENCES actors
#   );
# """)

SQL = 'INSERT into actors (id, name, age, gender) VALUES (%(id)s, %(name)s, %(age)s, %(gender)s);'

# data = {
#   'id': 1,
#   'name': 'Leonardo DiCaprio',
#   'age': 45,
#   'gender': 'Male'
# }

# data = {
#   'id': 2,
#   'name': 'Claire Danes',
#   'age': 41,
#   'gender': 'Female'
# }

# data = {
#   'id': 3,
#   'name': 'Zac Efron',
#   'age': 32,
#   'gender': 'Male'
# }

data = {
  'id': 4,
  'name': 'Emma Stone',
  'age': 31,
  'gender': 'Female'
}

cursor.execute(SQL, data)
connection.commit()
