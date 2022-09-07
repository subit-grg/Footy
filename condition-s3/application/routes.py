from application import app
from flask import jsonify
from flask import render_template
from random import choice
import requests

conditions = ['Snowy', 'Sunny', 'Rainy', 'Slippery', 'Dry']

@app.route('/get-condition', methods=['GET'])
def get_condition():
    condition = choice(conditions)
    return jsonify(condition=condition)