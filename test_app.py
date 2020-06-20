import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

CASTING_ASSISTANT = os.environ['CASTING_ASSISTANT']
CASTING_DIRECTOR = os.environ['CASTING_DIRECTOR']
EXECUTIVE_PRODUCER = os.environ['EXECUTIVE_PRODUCER']


class CastingTestCase(unittest.TestCase):
    """This class represents the casting test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'dbpass', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # self.headers = {'Authorization': ''}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # self.casting_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ6VHVFcnAyNTB6SVlKVlV4OU1FTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZXIyczB5MC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5YjZlODI2M2Y4MDAwYzhjMjBmYmFkIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5MjYyNzEzNSwiZXhwIjoxNTkyNzEzNTM1LCJhenAiOiI2TlFsaTNCQVhVRTNyN3E3VXdMbTZ1OFZiNVlCNUlRUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.ETndr_iXg6e8v3Gfl2GOiSzkDUMpyp-WXmAa0-gHw6cONgbnhcYRoos9HCH3o6nHy1ZYJ2kTRny3yOxr11-ax5FDpZWtaftNcKxlANVwfwJtHPz15IjrvvaZtcDCFqsUr2DR4Odx4biOX-QhwW-RiYHIcwZ60c_O94HOzMWwpemGRUUPwrBZQtTnMEbkZtXoHK2cXxWJ2Cf_t3M0pmYKiv_zncl1uUmGOurq0mxzFkIdOyARaCX5MxpARgzk5Hf-ryx5pqmRQmAdUuwjW9WH7VOTZXr-KKpWSAtPtXFlWOffDhiu3tp9CwzXBSm10SijtvmRiqmOaOtAbJS2sp5frA'
        # self.casting_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ6VHVFcnAyNTB6SVlKVlV4OU1FTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZXIyczB5MC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5YjZlYTBkZTQzMWEwYzhkNjQ5ZTdhIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5MjYyNzIwOCwiZXhwIjoxNTkyNzEzNjA4LCJhenAiOiI2TlFsaTNCQVhVRTNyN3E3VXdMbTZ1OFZiNVlCNUlRUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.j2rYTfNkFJpJyVqO5C069bWvNqx-ud9IJrBGu6z2D8WwVw3FLheiOFKFcLOFVa0_sUmdUSljrS698sNdGxUE3o7FiOwitj7zR8hEk_ixFjckIKv5I_DxuPPefND9n450CyXuLxhHBnKYotE8m7QgxgwpsGS1jaDgRg3txUGrnZm3PshctRLdyMGPMehHMHGFt4n8GVnEFKIZ0kOAyhw_iPOHKp3q9lL4GqVl--GDixGFObtldAX529Ss04nLWRl--WMGfkuRzM90XJc3xsX98BJLOc-H5-0OAngNKEx0fsYK1vCuPAW1PjiaRWfGF89FIyT7wNJCpYSwWWylZqFjVw'
        # executive_producer = {'Authorization': 'Bearer' 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ6VHVFcnAyNTB6SVlKVlV4OU1FTSJ9.eyJpc3MiOiJodHRwczovL2Rldi1nZXIyczB5MC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjYzVhOWJiM2MyOTIwYzVjMzI4YmYwIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5MjYyNzI3NiwiZXhwIjoxNTkyNzEzNjc2LCJhenAiOiI2TlFsaTNCQVhVRTNyN3E3VXdMbTZ1OFZiNVlCNUlRUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.c1uKGnA_Tjb8DAkWs-2f_fD1ovpmbDMORujHFh4v9XYEgypmIe2Jt3oD4NYZNQBdPJz1dr9egIZR5-GH3cZTdOrEptqxQfHM_vE3mN9yMRywnTCl0rZiI_Q_6K1a6YZPX5L_l4s4pZibZpGMZSwa-TFR4hnX4uu7P0xdGA75CZz3mnEgwkCojNCr5eGR5jRz2O3Vzi5VM5be-H4mXrsu5MLaVCsurdsxuOHsEwI_s38Z4H-L9Kx0gO1mu5WprxeOsMS5SRzk1VEvFwOiofFRm8UxGVfbHh9tzZUYlbRpviZHpmodCHdjIpLyLRZvTeCqNCVpkiTYmroezzvOSfmYsQ'}

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for
    successful operation and for expected errors.
    """

    def test_get_actors(self):
        """Test GET Actors """
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_404_sent_requesting_non_existent_actor(self):
        res = self.client().get('/actor/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_movies(self):
        """Test GET Movies """
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_404_sent_requesting_non_existent_movie(self):
        res = self.client().get('/movie/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_actor_executive_producer(self):
        """Test DELETE Actor """
        res = self.client().delete('/actors/23',
                                   headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {EXECUTIVE_PRODUCER}')])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor_casting_director(self):
        """Test DELETE Actor """
        res = self.client().delete('/actors/24',
                                   headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_DIRECTOR}')])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_delete_actor_casting_assistant(self):
        res = self.client().delete('/actors/28',
                                   headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_ASSISTANT}')])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_delete_actor_fail(self):
        res = self.client().delete('/actors/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_actor_executive_producer(self):
        """Test POST Actor """
        self.new_actor = {'name': 'New Actor', 'age': 40, 'gender': 'Male'}

        res = self.client().post('/actors/create',
                                 headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {EXECUTIVE_PRODUCER}')], json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_actor_casting_director(self):
        """Test POST Actor """
        self.new_actor = {'name': 'New Actor', 'age': 40, 'gender': 'Male'}

        res = self.client().post('/actors/create',
                                 headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_DIRECTOR}')], json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_create_actor_casting_assistant(self):
        """Test POST Actor """
        self.new_actor = {'name': 'New Actor', 'age': 40, 'gender': 'Male'}

        res = self.client().post('/actors/create',
                                 headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_ASSISTANT}')], json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_new_actor_fail(self):
        """Test POST Actor """
        self.new_actor = {'name': 'New Actor', 'age': 40, 'gender': 'Male'}

        res = self.client().post('/actors/create', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_actor_executive_producer(self):
        """Test PATCH Actor """
        self.actor = {'name': 'New Updated Name', 'age': 30, 'gender': 'Male'}
        res = self.client().patch('/actors/11',
                                headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {EXECUTIVE_PRODUCER}')], json=self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_patch_actor_casting_director(self):
        """Test PATCH Actor """
        self.actor = {'name': 'New Updated Name', 'age': 30, 'gender': 'Male'}
        res = self.client().patch('/actors/11',
                                headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_DIRECTOR}')], json=self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_actor_casting_assistant(self):
        """Test PATCH Actor """
        self.actor = {'name': 'New Updated Name', 'age': 30, 'gender': 'Male'}
        res = self.client().patch('/actors/11',
                                headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_ASSISTANT}')], json=self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_actor_fail(self):
        """Test PATCH Actor """
        self.actor = {'name': 'New Updated Name', 'age': 30, 'gender': 'Male'}
        res = self.client().patch('/actors/11', json=self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie_executive_producer(self):
        """Test DELETE Movie """
        res = self.client().delete('/movies/9',
                                   headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {EXECUTIVE_PRODUCER}')])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie_casting_director(self):
        """Test DELETE Movie """
        res = self.client().delete('/movies/10',
                                   headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_DIRECTOR}')])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_delete_movie_casting_assistant(self):
        """Test DELETE Movie """
        res = self.client().delete('/movies/12',
                                   headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_ASSISTANT}')])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_delete_movie_fail(self):
        res = self.client().delete('/movies/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_movie_executive_producer(self):
        """Test POST Movie """
        self.new_movie = {'movie_title': 'New Movie', 'release_year': 2040}

        res = self.client().post('/movies/create',
                                 headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {EXECUTIVE_PRODUCER}')], json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie_casting_director(self):
        """Test POST Movie """
        self.new_movie = {'movie_title': 'New Movie', 'release_year': 2040}

        res = self.client().post('/movies/create',
                                 headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_DIRECTOR}')], json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_create_movie_casting_assistant(self):
        """Test POST Movie """
        self.new_movie = {'movie_title': 'New Movie', 'release_year': 2040}

        res = self.client().post('/movies/create',
                                 headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_ASSISTANT}')], json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_create_movie_casting_assistant(self):
        """Test POST Movie """
        self.new_movie = {'movie_title': 'New Movie', 'release_year': 2040}

        res = self.client().post('/movies/create', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_movie_executive_producer(self):
        """Test PATCH Movie """
        self.movie = {'movie_title': 'Updated Movie', 'release_year': 2030}
        res = self.client().patch('/movies/8',
                                  headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {EXECUTIVE_PRODUCER}')], json=self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_patch_movie_casting_director(self):
        """Test PATCH Movie """
        self.movie = {'movie_title': 'Updated Movie', 'release_year': 2030}
        res = self.client().patch('/movies/8',
                                headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_DIRECTOR}')], json=self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_movie_casting_assistant(self):
        """Test PATCH Movie """
        self.movie = {'movie_title': 'Updated Movie', 'release_year': 2030}
        res = self.client().patch('/movies/8',
                                headers=[('Content-Type', 'application/json'), ('Authorization', f'Bearer {CASTING_ASSISTANT}')], json=self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_movie_fail(self):
        """Test PATCH Movie """
        self.movie = {'movie_title': 'Updated Movie', 'release_year': 2030}
        res = self.client().patch('/movies/8', json=self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
