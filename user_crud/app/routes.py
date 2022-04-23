
from flask import Flask, request, render_template, redirect
from datetime import datetime
from app.database import user, vehicle

app = Flask(__name__)
VERSION = "1.0.0"

@app.route('/version', methods = ['GET'])
def get_version():
    out = {
        'server_time': datetime.now().strftime("%F %H:%M:%S"),
        "version": VERSION
    }
    return out

@app.route('/users', methods = ['GET'])
def get_all_users():
    user_list = user.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "users": user_list
    }
    return resp

@app.route('/users/<int:pk>', methods = ['GET', 'POST', 'put', 'delete'])
def user_func(pk):
    target = user.select_by_id(pk)
    if target:
        if request.method == "GET":
            resp = {
                "status": "ok",
                "message": "success",
            }
            if len(target) > 0:
                resp['user'] = target
            else:
                resp["message"] = "user not fount"
                resp['status'] = "error"
            return resp
        elif request.method == "POST":
            user_data = request.json
            user.insert(user_data)
            return "", 204
        elif request.method == "PUT":
            user_data = request.json
            user.update(pk, user_data)
            return "", 204
        elif request.method == "DELETE":
            user.deactivate(pk)
            return "", 204
    else:
        return "User not found", 404

@app.route('/vehicles', methods = ['GET'])
def get_all_vehicles():
    vehicle_list = vehicle.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "vehicles": vehicle_list
    }
    return resp

@app.route('/vehicles/<int:pk>', methods = ['GET', 'POST', 'put', 'delete'])
def vehicle_func(pk):
    target = vehicle.select_by_id(pk)
    if target:
        if request.method == "GET":
            resp = {
                "status": "ok",
                "message": "success",
            }
            if len(target) > 0:
                resp['vehicle'] = target
            else:
                resp["message"] = "vehicle not fount"
                resp['status'] = "error"
            return resp
        elif request.method == "POST":
            vehicle_data = request.json
            vehicle.insert(vehicle_data)
            return "", 204
        elif request.method == "PUT":
            vehicle_data = request.json
            vehicle.update(pk, vehicle_data)
            return "", 204
        elif request.method == "DELETE":
            vehicle.deactivate(pk)
            return "", 204
    else:
        return "vehicle not found", 404

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

