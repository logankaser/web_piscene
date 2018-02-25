from flask import Flask
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__, static_url_path='/static')
app.config.from_object("config")

from app.views import main

db = sqlite3.connect("test.db")
with app.open_resource("schema.sql", mode="r") as f:
    db.cursor().executescript(f.read())
db.commit()
