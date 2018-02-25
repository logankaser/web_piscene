from flask import Flask
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__, static_url_path='/static')
app.config.from_object("config")
app.secret_key = "\xcc\xe9\xc7\x90\xe1?\xe7\xb3\xbc\\\xe1\xd6\x80\x18\xdc\xde\xc0\x81\x15\xddp~\xf9C"

from app.views import main

db = sqlite3.connect("test.db")
with app.open_resource("schema.sql", mode="r") as f:
    db.cursor().executescript(f.read())
db.commit()
