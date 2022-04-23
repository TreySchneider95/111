from flask import g

import sqlite3

DATABASE = "user.db"

def get_db():
    # db = getattr(g, "_database", None)
    db = g._database = sqlite3.connect(DATABASE)
    return db