#!/usr/bin/python

from flask import Flask, jsonify
from flask import abort, make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
from flask import request
auth = HTTPBasicAuth()

import vlan

app = Flask(__name__)

tasks = [
    {

    }
]

@auth.get_password
def get_password(username):
    if username == 'ken':
        return 'Passw0rd!'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/createvlan', methods=['POST'])
@auth.login_required
def createvlan():
        function = {
                'eth' : request.json['eth'],
                'num' : request.json['num'],
                'desc' : request.json['desc'],
		'ip' : request.json['ip'] 
        }
        tasks.append(function)
        vlan.createvlan(function['eth'],function['num'],function['desc'],function['ip'])
        return jsonify({'vlan' : vlan.readvlan()})
@app.route('/readvlan', methods=['GET'])
def readvlan():
        return jsonify({'vlan' : vlan.readvlan()})

@app.route('/delvlan', methods=['POST'])
@auth.login_required
def delvlan():
        function = {
                'eth' : request.json['eth'],
		'num' : request.json['num']
        }
        tasks.append(function)
        vlan.delvlan(function['eth'],function['num'])
        return jsonify({'vlan' : vlan.readvlan()})

@app.route('/updatevlan', methods=['POST'])
@auth.login_required
def updatevlan():
        function = {
                'eth' : request.json['eth'],
                'eth1' : request.json['eth1'],
                'num' : request.json['num'],
                'num1' : request.json['num1'],
		'desc' : request.json['desc'],
		'ip' : request.json['ip']
        }
        tasks.append(function)
        vlan.updatevlan(function['eth'],function['eth1'],function['num'],function['num1'],function['desc'],function['ip'])
        return jsonify({'vlan' : vlan.readvlan()})

if __name__ == '__main__':
    app.run(debug=True)


