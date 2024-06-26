import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

import itertools
import random
import sqlite3

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


def get_db_connection():
    conn= sqlite3.connect('priorities.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_titles_from_db():
    """Access database for titles"""
    titles = db.execute("SELECT * FROM titles")
    return titles


def get_items_from_db():
    """Access database for items"""
    items = db.execute("SELECT * FROM items")
    return items


def get_counts_from_db():
    """Get counted items for score"""
    counts = db.execute("SELECT count FROM items WHERE item_id = ?", item_id)
    return counts


def increment_count(item):
    """Increment count"""
    count = db.execute("INSERT OR IGNORE INTO items (count) VALUES (?)", (count))
    increment_count = db.execute("UPDATE items SET count = count + 1 WHERE item_id = ?", (item_id))
    return increment_count


@app.route("/")
def index():
    """Set basic informations about app"""
    return render_template("index.html")


@app.route("/title", methods=["POST"])
def title():
    """Add title"""
    if request.method == "POST":
        title = request.form.get("title")

        if not title:
            return render_template("error.html", message="Missing title")

        elif not title.isalpha():
            return render_template("error.html", message="Please input text")

        # Insert title
        conn = get_db_connection()
        conn.execute("INSERT INTO titles (title) VALUES (?)", (title,))
        conn.commit()
        conn.close()

        return redirect("/items")


@app.route("/items", methods=["GET", "POST", "DELETE"])
def items():
    """Add title and items to the list"""
    item = request.form.get["item"].strip().lower()
    
    if request.method == 'POST':

        if not item:
            return render_template("error.html", message="Missing item")
        if not item.isalpha():
            return render_template("error.html", message="Input text, no digits or special symbols")

        db.execute("INSERT OR IGNORE INTO items (item_name) VALUES (?)", item_name)

        return redirect("/items")

    elif request.method == "DELETE":
        delete = request.form.get("delete")
        db.execute("DELETE FROM items WHERE item_id = ?", item_id)

        return render_template("items.html", title=title, items=items)

    else:
        titles = get_titles_from_db()
        items = get_items_from_db()

        return render_template("items.html", title=title, items=items)


@app.route("/choose", methods=['GET', 'POST'])
def choose():

    items = get_items_from_db()
    pairs = list(itertools.product(items, repeat=2))
    random.shuffle(pairs)
    counts = get_counts_from_db()

    if request.method == 'POST':
        chosen_item = int(request.form['chosen_item'])
        increment_count(chosen_item)
        return redirect(url_for('choose'))
    pair = pairs.pop(0) if pairs else None
    return render_template("choose.html", pair=pair, counts=counts)


@app.route("/result")
def result():
    title = db.execute("SELECT title from titles WHERE id = ?", id)
    counts = get_counts_from_db()
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return render_template("result.html", title=title, sorted_counts=sorted_counts)


@app.route("/history", methods=["GET"])
def history():
    """Show history of priorities"""
    conn = get_db_connection()
    titles = conn.execute("SELECT * FROM titles").fetchall()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()

    items_by_title = {}
    for title in titles:
        items_by_title[title['id']] = []

    for item in items:
        # items_by_title[item['title_id']].append(item['item'])
        items_by_title[item['title_id']].append({'id': item['item_id'], 'item_name': item['item_name'], 'count': item['count']})

    # Show rendered history page with all transactions
    return render_template("history.html", titles=titles, items_by_title=items_by_title)


if __name__ == "__main__":
    app.run(debug=True)
