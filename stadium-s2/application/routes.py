from application import app
import requests
from flask import jsonify
from random import choice

stadiums = ["Wembley Stadium","Camp Nou","Allianz Arena","Old Trafford","Anfield",]

@app.route('/get-stadium', methods=['GET'])
def get_stadium():
    stadium = choice(stadiums)
    return jsonify(stadium=stadium)
