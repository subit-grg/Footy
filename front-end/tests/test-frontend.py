from flask import url_for
from flask_testing import TestCase
import pytest
import requests_mock
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFrontend(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as m:
            m.get('http://stadium:5000/get-stadium', json={'stadium':'Camp Nou'})
            m.get('http://condition:5000/get-condition', json={'condition':'Snowy'})
            m.post('http://oppo:5000/get-oppo', json={'opp':'Barcelona'})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'You will be facing Barcelona at Camp Nou under Snowy condition', response.data)
