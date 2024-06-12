import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto_reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use  SQLite database
db = SQL("sqlite:///priorities.db")


@app.after_request
def after_request(response):
    """Ensure responces aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    """Set basic informations about app"""