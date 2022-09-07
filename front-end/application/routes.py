from application import app
import requests
from flask import render_template, url_for, jsonify

@app.route('/')
def index():
    stadium_ = requests.get('http://stadium-s2:5000/get-stadium')
    condition_ = requests.get('http://condition-s3:5000/get-condition')
    oppo_ = requests.post('http://opp-s4:5000/get-oppo', json=stadium_.json())
    return render_template('index.html',opp=oppo_.json()['opp'], stadium=stadium_.json()['stadium'], condition=condition_.json()['condition'])