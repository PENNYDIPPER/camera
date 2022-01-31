# app.py

import os
import sqlite3
from flask import Flask, request, g
app = Flask(__name__)

DATABASE = 'global.db'


# helper method, allows database access within a controller
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db