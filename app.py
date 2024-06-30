import os

from flask import Flask, flash, redirect, render_template, request, session, url_for

from config import Config
import random
import sqlite3


# Configure application
app = Flask(__name__)

# Configure secret key
app.config.from_object(Config)

# Ensure templates are auto_reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


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


def isalpha_or_space(self):
    if self == "":
        return False
    for char in self:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


@app.route("/")
def index():
    """Set basic informations about app"""
    return render_template("index.html")


@app.route("/title", methods=["GET", "POST"])
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
        conn.commit()
        conn.close()

        return redirect("/items")
    
    else:
        return render_template("title.html")


@app.route("/items/<int:title_id>", methods=["GET", "POST"])
def items(title_id):
    """Add items to the list"""
    conn = get_db_connection()
    title = conn.execute("SELECT * FROM titles WHERE title_id = ?", (id,)).fetchone()
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
    
    return render_template("/items", title=title, items=items)


@app.route("/choose/<int:title_id>", methods=["GET", "POST"])
def choose(title_id):
    if 'game_data' not in session:
        conn = get_db_connection()
        items = conn.execute("SELECT * FROM items WHERE title_id = ?", (title_id,)).fetchall()
        conn.close()
        
        item_pairs = [(items[i]['id'], items[j]['id']) for i in range(len(items)) for j in range(i+1, len(items))]
        random.shuffle(item_pairs)

        session['game_data'] = {
            'title_id': title_id,
            'item_pairs': item_pairs,
            'current_pair': 0,
            'count': {item['item_id']: 0 for item in items}
        }

    game_data = session['game_data']
    
    if request.method == 'POST':
        selected_item = int(request.form['selected_item'])
        game_data['count'][selected_item] += 1
        game_data['current_pair'] += 1
        
        if game_data['current_pair'] >= len(game_data['item_pairs']):
            return redirect(url_for('results'))

        session['game_data'] = game_data

    current_pair = game_data['item_pairs'][game_data['current_pair']]
    conn = get_db_connection()
    item1 = conn.execute('SELECT * FROM items WHERE id = ?', (current_pair[0],)).fetchone()
    item2 = conn.execute('SELECT * FROM items WHERE id = ?', (current_pair[1],)).fetchone()
    conn.close()

    return render_template('choose.html', item1=item1, item2=item2)


@app.route("/result/<int:title_id>")
def result():
    game_data = session.pop('game_data', None)
    if not game_data:
        return redirect(url_for('index'))

    conn = get_db_connection()
    title = conn.execute("SELECT title FROM titles WHERE id = ?", (game_data['title_id'],)).fetchone()
    items = conn.execute('SELECT * FROM items WHERE title_id = ?', (game_data['title_id'],)).fetchall()
    conn.close()
    
    sorted_items = sorted(items, key=lambda item: game_data['count'][item['item_id']], reverse=True)

    return render_template('results.html', sorted_items=sorted_items, title=title)


@app.route('/update_title/<int:title_id>', methods=('GET', 'POST'))
def update_title(title_id):
    conn = get_db_connection()
    title = conn.execute('SELECT * FROM titles WHERE id = ?', (title_id,)).fetchone()

    if request.method == 'POST':
        new_title = request.form['title']
        conn.execute('UPDATE titles SET title = ? WHERE id = ?', (new_title, title_id))
        conn.commit()
        conn.close()
        return redirect(url_for('items'))

    conn.close()
    return render_template('title.html', title=title)


@app.route('/reset_game')
def reset_game():
    if 'game_data' in session:
        title_id = session['game_data']['title_id']
        session.pop('game_data')
        return redirect(url_for('choose', title_id=title_id))
    return redirect(url_for('index'))


@app.route("/delete/<int:title_id>", methods=["POST"])
def delete(title_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM items WHERE title_id = ?", (title_id,))
    conn.execute("DELETE FROM titles WHERE id = ?", (title_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route("/history", methods=["GET"])
def history():
    """Show history of priorities"""
    conn = get_db_connection()
    titles = conn.execute("SELECT * FROM titles ORDER BY id DESC").fetchall()
    items = conn.execute("SELECT * FROM items ORDER BY count DESC").fetchall()
    conn.close()

    items_by_title = {}
    for title in titles:
        items_by_title[title['id']] = []

    for item in items:
        items_by_title[item['title_id']].append({'id': item['item_id'], 'item_name': item['item_name'], 'count': item['count']})

    # Show rendered history page with all transactions
    return render_template("history.html", titles=titles, items_by_title=items_by_title)


if __name__ == "__main__":
    app.run(debug=True)
