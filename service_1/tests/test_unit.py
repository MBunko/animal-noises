from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app, db
from application.routes import Animals

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Animals(animal_type="test animal", animal_noise="debug"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase): 

    def test_horse(self):
        with requests_mock.mock() as m:
            m.get('http://animal-noises_animal-backend:5000/animal', text='horse')
            m.post('http://animal-noises_animal-backend:5000/noise', text='neigh') 
            response = self.client.get(url_for('index'))
            self.assertIn(b'horse goes neigh', response.data)
            self.assertIn(b'test animal went debug', response.data)