from application import app
import requests
from flask import request, jsonify
from random import choice



@app.route('/get-oppo', methods=['POST'])
def get_opp():
    request_json = request.get_json()
    request_ = request_json['stadium']
    oppo = ['Manchester United','Liverpool','Barcelona','Charlton Athletic']
    if request_ == "Wembley Stadium":
        oppo.append('Charlton Athletic')
        oppo.append('Charlton Athletic')
        oppo.append('Charlton Athletic')
        oppo.append('Charlton Athletic')
    elif request_ == "Camp Nou":
        oppo.append('Barcelona')
        oppo.append('Barcelona')
        oppo.append('Barcelona')
        oppo.append('Barcelona')
    elif request_ == "Old Trafford":
        oppo.append('Manchester United')
        oppo.append('Manchester United')
        oppo.append('Manchester United')
        oppo.append('Manchester United')
    elif request_ == 'Anfield':
        oppo.append('Liverpool')
        oppo.append('Liverpool')
        oppo.append('Liverpool')
        oppo.append('Liverpool')
    opps = choice(oppo)
    return jsonify(opp=opps)