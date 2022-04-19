
from flask import Flask, request, render_template, redirect
from datetime import datetime
from app.database import user

VERSION = "1.0.0"

app = Flask(__name__)

@app.route('/version', methods = ['GET'])
def get_version():
    out = {
        'server_time': datetime.now().strftime("%F %H:%M:%S"),
        "version": VERSION
    }
    return out


@app.route('/users', methods = ['GET', 'POST'])
def get_all_users():
    if request.method == "GET":
        user_list = user.scan()
        resp = {
            "status": "ok",
            "message": "success",
            "users": user_list
        }
        return resp


@app.route('/users/<int:pk>', methods = ['GET', 'POST', 'put', 'delete'])
def user_func(pk):
    if request.method == "GET":
        target = user.select_by_id(pk)
        resp = {
            "status": "ok",
            "message": "success",
            "users": target
        }
        return resp
    elif request.method == "POST":
        user_data = request.json
        user.insert(pk, user_data)
        return "", 204
    elif request.method == "PUT":
        user_data = request.json
        user.update(pk, user_data)
        return "", 204
    elif request.method == "DELETE":
        user.deactivate(pk)
        return "", 204


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

