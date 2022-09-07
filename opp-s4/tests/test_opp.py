from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    @patch('application.routes.choice', return_value='Liverpool')
    def test_opp(self, mock_func):
        response = self.client.post(url_for('get_opp'), json={'location':'Allianz Arena'})
        self.assert200(response)
        self.assertIn(b'Liverpool',response.data)

    @patch('application.routes.choice', return_value='Liverpool')
    def test_opp2(self, mock_func):
        response = self.client.post(url_for('get_opp'), json={'location':'Old Trafford'})
        self.assert200(response)
        self.assertIn(b'Liverpool',response.data)

    @patch('application.routes.choice', return_value='Liverpool')
    def test_opp3(self, mock_func):
        response = self.client.post(url_for('get_opp'), json={'location':'Wembley Stadium'})
        self.assert200(response)
        self.assertIn(b'Liverpool',response.data)
    
    @patch('application.routes.choice', return_value='Liverpool')
    def test_opp4(self, mock_func):
        response = self.client.post(url_for('get_opp'), json={'location':'Anfield'})
        self.assert200(response)
        self.assertIn(b'Liverpool',response.data)