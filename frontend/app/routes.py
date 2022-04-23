from urllib import response
from flask import Flask, render_template
import requests
app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5000"

@app.get('/')
def display_users():
    url = f"{BACKEND_URL}/users"
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json().get("users")
        return render_template("index.html", users = user_data)
    else:
        return render_template("no_users_error.html")

@app.get('/report')
def report_page():
    url = f"{BACKEND_URL}/report"
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json().get("vehicles")
        print(user_data)
        return render_template("report.html", info = user_data)
    else:
        return render_template("no_info_error.html")