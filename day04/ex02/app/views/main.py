# -*- coding: utf-8 -*-
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    routes.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lkaser <lkaser@student.42.us.org>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/02/24 11:37:14 by lkaser            #+#    #+#              #
#    Updated: 2018/02/24 11:37:14 by lkaser           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sqlite3 import dbapi2 as sqlite3
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash
from app import app

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, "sqlite_db"):
        top.sqlite_db = sqlite3.connect("test.db")
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db


@app.teardown_appcontext
def close_database(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, "sqlite_db"):
        top.sqlite_db.close()

def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv


def get_user_id(username):
    """Convenience method to look up the id for a username."""
    rv = query_db("SELECT id FROM Users WHERE username = ?",
                  [username], one=True)
    return rv[0] if rv else None


@app.before_request
def before_request():
    g.user = None
    if "id" in session:
        g.user = query_db("select * from Users where id = ?",
                          [session["id"]], one=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Logs the user in."""
    if g.user:
        return redirect(url_for("store"))
    error = None
    if request.method == "POST":
        user = query_db("""SELECT * FROM Users WHERE
            username = ?""", [request.form["username"]], one=True)
        if user is None:
            error = "Invalid username and password pair"
        elif not check_password_hash(user["pw_hash"],
                                     request.form["password"]):
            error = "Invalid username and password pair"
        else:
            session["id"] = user["id"]
            flash("Login successful!")
            return render_template("login.html", error=error)
    return render_template("login.html", error=error)

@app.route('/user/modify', methods=['GET', 'POST'])
def modify():
    """Change user password"""
    if g.user is None:
       return redirect(url_for("login"))
    error = None
    if request.method == "POST":
        if not check_password_hash(g.user["pw_hash"], request.form["password"]):
            error = "Invalid password"
        else:
            flash("Password changed")
            db = get_db()
            db.execute("""UPDATE Users SET pw_hash = ? WHERE id = ?""", [
                generate_password_hash(request.form["password_new"]),
                g.user["id"]
            ])
            db.commit()
            return render_template("modify.html", error=error)
    return render_template("modify.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Registers the user."""
    error = None
    if request.method == "POST":
        if not request.form["username"]:
            error = "You have to enter a username"
        elif not request.form["email"] or \
                "@" not in request.form["email"]:
            error = "You have to enter a valid email address"
        elif not request.form["password"]:
            error = "You have to enter a password"
        elif request.form["password"] != request.form["password2"]:
            error = "The two passwords do not match"
        elif get_user_id(request.form["username"]) is not None:
            error = "The username is already taken"
        else:
            db = get_db()
            db.execute("""
                INSERT INTO Users (
                username, email, pw_hash) values (?, ?, ?)
            """,
                [request.form["username"], 
                request.form["email"],
                generate_password_hash(request.form["password"])])
            db.commit()
            flash("Registration complete!")
            return redirect(url_for("login"))
    return render_template("register.html", error=error)


@app.route("/logout")
def logout():
    """Logs the user out."""
    flash("You were logged out")
    session.pop("id", None)
    return redirect(url_for("login"))

