#!/usr/bin/python

from flask import Flask, jsonify
from flask import abort,make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
from flask import request
auth = HTTPBasicAuth()

import fw

app = Flask(__name__)

tasks = [
    {

    }
]

@auth.get_password
def get_password(username):
    if username == 'Devesh':
        return 'Passw0rd!'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/createfirewall', methods=['POST'])
@auth.login_required
def createfirewall():
    function = {
		'fname' : request.json['fname']
	       }
    tasks.append(function)
    fw.createfirewall(function['fname'])
    return jsonify({'firewall' : fw.readfirewall()}), 201

@app.route('/readfirewall', methods=['GET'])
def readfirewall():
    return jsonify({'firewall' : fw.readfirewall()})


@app.route('/updatefirewall', methods=['POST'])
@auth.login_required
def updatefirewall():
	function = {
		    'fname' : request.json['fname'],
		    'fname2' : request.json['fname2']
	           }
	tasks.append(function)
	fw.updatefirewall(function['fname'], function['fname2'])
	return jsonify({'firewall' : fw.readfirewall()}), 201

@app.route('/delfirewall', methods=['POST'])
@auth.login_required
def delfirewall():
	function = {
		'fname' : request.json['fname']
		}
	tasks.append(function)
	fw.delfirewall(function['fname'])
	return jsonify({'firewall' : fw.readfirewall()}), 201

if __name__ == '__main__':
    app.run(debug=True)

