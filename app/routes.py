from flask import Flask, render_template, redirect, abort
import json

app = Flask(__name__)

@app.get("/aboutme")
def index():
    me = {
        "first_name":"Trey",
        "last_name":"Schneider",
        "hobby":"Coding"
    }
    return json.dumps(me)

