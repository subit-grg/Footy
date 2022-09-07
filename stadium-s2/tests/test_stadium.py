from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_stadium(TestBase):
    @patch('application.routes.choice', return_value='Anfield')
    def test_stad(self, mock_func):
        response = self.client.get(url_for('get_stadium'))
        self.assert200(response)
        self.assertIn(b'Anfield', response.data)