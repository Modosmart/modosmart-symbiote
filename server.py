#!/usr/bin/python
import os
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# api = Api(app)

# class RoomSensor(Resource):
#     def get(self, ip):
#         # print(request.method)
#         resp = {'IP': ip}
#         return jsonify(resp)
#
# api.add_resource(RoomSensor, '/api/ble/room_sensor/<ip>')

app = Flask(__name__)

@app.route("/api/ble/room_sensor/<ip>", methods=['POST'])
def le_scan(ip):
    if request.method == 'POST':
        

@app.route("/api/ble/room_sensor/<ip>", methods=['GET'])
def room_sensor(ip):
    if request.method == 'GET':
        # resp = Response('', status=200, mimetype='application/json')
        resp = {'error': 'false'}
        return jsonify(resp)

        # start looking for BLE devices

# @app.route("/api/ble/room_sensor/<ip>", methods=['GET'])
#     def room_sensor(ip):

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3030, debug=True)
