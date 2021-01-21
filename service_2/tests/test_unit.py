from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase): 

    def test_get_animal(self):
        with patch("random.choice") as random:
            random.return_value = "pig" 
            response = self.client.get(url_for('get_animal'))
            self.assertEqual(b'pig', response.data)

        for _ in range(10):
            response = self.client.get(url_for('get_animal'))
            self.assertIn(response.data, [b"pig", b"cow", b"horse", b"chicken"])
    
    def test_get_noise(self):
        response = self.client.post(url_for('get_noise'), json={"animal" : "pig"})
        self.assertEqual(b"oink", response.data)