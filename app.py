import os

from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
import random
import sqlite3
from datetime import datetime


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responces aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'priorities.db')
    conn= sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def isalpha_or_space(self):
    if self == "":
        return False
    for char in self:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


def current_year():
    current_year = datetime.now().year
    return current_year

@app.route("/")
def about():
    """Log user in"""
    # Forget any user_id
    session.clear()

    return render_template("about.html")


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html", message="Please input username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("error.html", message="Please input password")

        # Query database for username
        conn = get_db_connection()
        cursor = conn.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))
        rows = cursor.fetchall()
        conn.close()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("error.html", message="Invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/home")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure input exists
        if not request.form.get("username") or not request.form.get("password") or not request.form.get("confirmation"):
            return render_template("error.html", message="Must provide input")

        # Ensure password and confirmation are the same
        elif request.form.get("password") != request.form.get("confirmation"):
            return render_template("error.html", message="Passwords do not match, please repeat")

        # Query database for new user
        conn = get_db_connection()
        cursor = conn.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))
        rows = cursor.fetchall()

        # Ensure username does not exist
        if len(rows) != 0:
            conn.close()
            return render_template("error.html", message="Username already exists")

        # Insert new user into the database
        hashed_password = generate_password_hash(request.form.get("password"))
        conn.execute("INSERT INTO users (username, hash) VALUES(?, ?)", (request.form.get("username"), hashed_password))
        conn.commit()

        # Query the database to get the new user's ID
        cursor = conn.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))
        rows = cursor.fetchall()
        conn.close()

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/home")

    else:
        return render_template("register.html")


@app.route("/home")
@login_required
def index():
    """Set basic informations about app"""
    user_id = session["user_id"]  # Retrieve user_id from session

    conn = get_db_connection()
    cursor = conn.execute("SELECT username FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()  # Fetch the result
    conn.close()

    if row:
        username = row['username']
    else:
        username = None  # Handle case where user_id doesn't exist

    return render_template("index.html", username=username)


@app.route("/title", methods=["GET", "POST"])
@login_required
def title():
    """Add title"""
    if request.method == "POST":
        title = request.form.get("title")

        conn = get_db_connection()
        existing_title = conn.execute('SELECT * FROM titles WHERE title = ?', (title,)).fetchone()

        if existing_title:
            conn.close()
            return render_template('error.html', message="Title already exists")

        elif not title:
            return render_template("error.html", message="Missing title")

        elif not isalpha_or_space(title):
            return render_template("error.html", message="Please input text")

        # Insert title
        conn = get_db_connection()
        conn.execute("INSERT INTO titles (title) VALUES (?)", (title,))
        title_id = conn.execute("SELECT max(id) FROM titles").fetchone()[0]
        print(title_id)
        conn.commit()
        conn.close()

        return redirect(f"/items/{title_id}")

    else:
        conn = get_db_connection()
        title_id = conn.execute("SELECT id FROM titles")
        conn.commit()
        conn.close()

        return render_template("title.html")


@app.route("/items/<int:title_id>", methods=["GET", "POST"])
@login_required
def items(title_id):
    """Add items to the list"""
    conn = get_db_connection()
    title_id = conn.execute("SELECT max(id) FROM titles").fetchone()[0]
    title = conn.execute("SELECT * FROM titles WHERE id = ?", (title_id,)).fetchone()
    items = conn.execute("SELECT * FROM items WHERE title_id = ?", (title_id,)).fetchall()
    conn.close()

    if title is None:
        return render_template("error.html", message="Title not found")

    if request.method == "POST":
        item_name = request.form['item']

        if not item_name:
            return render_template("error.html", message="Missing item")

        elif not isalpha_or_space(item_name):
            return render_template("error.html", message="Please input text")

        conn = get_db_connection()
        existing_item = conn.execute("SELECT * FROM items WHERE title_id = ? AND item_name = ?", (title_id, item_name)).fetchone()

        if existing_item:
            conn.close()
            return render_template('error.html', message="Item already exists")

        conn = get_db_connection()
        conn.execute("INSERT INTO items (title_id, item_name) VALUES (?, ?)", (title_id, item_name))
        conn.commit()
        conn.close()

        return redirect(url_for('items', title_id=title_id))

    return render_template("items.html", title=title, items=items)


@app.route("/choose/<int:title_id>", methods=["GET", "POST"])
@login_required
def choose(title_id):
    if 'game_data' not in session:
        conn = get_db_connection()
        title_id = conn.execute("SELECT max(id) FROM titles").fetchone()[0]
        items = conn.execute("SELECT * FROM items WHERE title_id = ?", (title_id,)).fetchall()
        conn.close()

        item_pairs = [(items[i]['id'], items[j]['id']) for i in range(len(items)) for j in range(i+1, len(items))]
        random.shuffle(item_pairs)

        session['game_data'] = {
            'title_id': title_id,
            'item_pairs': item_pairs,
            'current_pair': 0,
            'count': {item['id']: 0 for item in items}
        }

    game_data = session['game_data']

    if request.method == 'POST':
        selected_item = int(request.form['selected_item'])
        game_data['count'][str(selected_item)] += 1

        conn = get_db_connection()
        conn.execute("UPDATE items SET count = count + 1 WHERE id = ?", (selected_item,))
        conn.commit()
        conn.close()

        game_data['current_pair'] += 1

        if game_data['current_pair'] >= len(game_data['item_pairs']):
            return redirect(f"/result/{title_id}")

        session['game_data'] = game_data

    current_pair = game_data['item_pairs'][game_data['current_pair']]
    conn = get_db_connection()
    item1 = conn.execute('SELECT * FROM items WHERE id = ?', (current_pair[0],)).fetchone()
    item2 = conn.execute('SELECT * FROM items WHERE id = ?', (current_pair[1],)).fetchone()
    conn.close()

    return render_template('choose.html', item1=item1, item2=item2)


@app.route("/result/<int:title_id>")
@login_required
def result(title_id):
    game_data = session.pop('game_data', None)
    if not game_data:
        return redirect(url_for('index'))

    conn = get_db_connection()
    title = conn.execute("SELECT title FROM titles WHERE id = ?", (game_data['title_id'],)).fetchone()
    items = conn.execute('SELECT * FROM items WHERE title_id = ?', (game_data['title_id'],)).fetchall()
    sorted_items = conn.execute("SELECT * FROM items WHERE title_id = ? ORDER BY count DESC", (game_data['title_id'],)).fetchall()
    conn.close()

    return render_template('result.html', sorted_items=sorted_items, title=title, game_data=game_data)


@app.route('/reset_game')
@login_required
def reset_game(title_id):
    if 'game_data' in session:
        title_id = session['game_data']['title_id']
        session.pop('game_data')

        conn = get_db_connection()
        conn.execute("UPDATE items SET count = 0 WHERE title_id = ?", (title_id,))
        conn.commit()
        conn.close()
        return redirect(url_for('items', title_id=title_id))

    else:
        conn = get_db_connection()
        title_id = conn.execute("SELECT max(id) FROM titles").fetchone()[0]
        title = conn.execute("SELECT * FROM titles WHERE id = ?", (title_id,)).fetchone()
        items = conn.execute("SELECT * FROM items WHERE title_id = ?", (title_id,)).fetchall()

        return render_template("items.html", title=title, items=items)


@app.route("/delete/<int:title_id>", methods=["POST"])
@login_required
def delete(title_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM items WHERE title_id = ?", (title_id,))
    conn.execute("DELETE FROM titles WHERE id = ?", (title_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route("/history", methods=["GET"])
@login_required
def history():
    """Show history of priorities"""
    conn = get_db_connection()
    titles = conn.execute("SELECT * FROM titles ORDER BY id DESC").fetchall()
    items = conn.execute("SELECT * FROM items ORDER BY count DESC").fetchall()
    conn.close()

    items_by_title = {title['id']: [] for title in titles}

    for item in items:
        title_id = item['title_id']
        if title_id in items_by_title:
            items_by_title[title_id].append({
                'id': item['id'],
                'item_name': item['item_name'],
                'count': item['count']
            })

    # Show rendered history page with all transactions
    return render_template("history.html", titles=titles, items_by_title=items_by_title)


if __name__ == "__main__":
    app.run(debug=True)
