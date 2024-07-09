<div align="center">

<img src="https://github.com/krisbaranski/priority_grid/blob/main/static/assets/priority.png" alt="Priority Grid Logo" width="150" height="150">

# Priority Grid

</div>

#### Video Demo:

## Tech Stack

#### Flask, Python, Jinja, SQLite3, HTML, CSS, Bootstrap, JavaScript

## Introduction:

Prioritizing methods utilizes the principles of importance and urgency to organize priorities and workload.
Here are examples of approach:

- ABC analysis
- Pareto analysis
- Eisenhower Box
- Priority Matrix
- ...

For more information follow this [link](https://en.wikipedia.org/wiki/Time_management#The_Eisenhower_Method)

The method i implement is the **Prioritization Matrix** and it looks like image below

<div align="center">

<img src="https://github.com/krisbaranski/priority_grid/blob/main/static/assets/prioritization_matrix.png" alt="Prioritization Matrix" width="350" height="auto">

</div>

<br/>

## What is it about

#### Explanation

This apps purpose is to specify the easy way, what your priorities in particular subject are (i.e. qualities, tasks, todos ...).
When we have some subject to prioritize, it doesn't become obvious what is their right order. This app clearify important properties as a simple list.

Classical approach is to do it manually, as you can see on image above (priority matrix). It will take some work to fill all items on paper, compare and count them, replace items order. So, as you can see, its time consuming.

Therefore this app is an easy tool to create a list and order your items with a few clicks.

The app go through a random loop of properties, showing them as pairs.
There you can choose only one, which is more of value. It continue until all properties were meet once.
In the end, you get a result as a list of key:value pairs of those properties, ordered descending.
The property on top have the most "points" and last one the least or no "points".
Thats how your properties will give a result of priority grid. From most to least important.

You can make as many headings as you like and you can create a new list to prioritize.
You can also run your "matrix" again after reset.
Consider that number of your items will give multiple pairs i.e. 6 items = 15 possible pairs, 10 items = 45. It can still take few minutes to figure out your priority grid.

## How to use it

#### Follow this steps

1. on main page `index` is a button `create new` to start, it redirect you to title page
2. on `title` page fill input with a title of your priority list, i.e.
   **`Qualities`**
3. now you are redirected to `items` page where you create a list of items to work with, i.e.
   **`Strong`**
   **`Fast`**
   **`Something`**
   `...`
   afer finish push the button `start choosing`
4. now you are redirected to `choose` page where you get pairs of items. Choose only one of them, which is more valuable for you i.e.:
   **`Strong`** OR **`Fast`**
5. those pairs will continue until all possible combinations are shown (i.e. 6 items = 15 possible pairs)
6. when finished, you will be redirected to `result` page where you get a list of your items sorted from most for least important
7. on `history` page are stored all your lists with titles and corresponding items

###

## Install ide, tools and dependencies

Steps of preperation to work with project:

- download and install VSCode (or code editor of your choice) for local work

- install python3, to check current version:
  `python3 --version`

- inside of the app directory, install virtual environment:
  `pip3 install virtualenv`

- to use flask run command, install virtual env:
  `virtualenv env`

- start using virtual env:
  `source env/bin/activate`

- install flask:
  `pip3 install flask`

- start local server to see the development in browser (localhost:5000):
  `flask run` or
  `python3 app.py`

- you can also install gunicorn for local testing
  `pip install gunicorn`

## Build up

```
- Flask basic files ( app.py, /templates, /static/assets, styles.css)
- Preloader animation with logo on index page (CSS, JavaScript)
- Introduction and "rules of game" on index site as accordion (Bootstrap)
- Bootstrap responsive navigation menu, buttons, layout, fonts, lists
- SQLite3 tables to store data in db (priorities.db)
- Python implementation of choosing "game"
- Access to database in history to show all of your priority results
- Possibility to add, change, delete grids titles and/or items
- Config file for generating secret_key
- Debugging, checking functionality, fixing bugs
```

## File structure

#### app.py

```
- import of dependencies (Flask, os, config, random, sqlite3)
- define functions for:
    > database
    > error check
    > routes
    > reset
    > delete item
    > delete title and items
```

#### config.py

```
configure automatically generated secret_key
```

#### backup.txt

```
sqlite3 commands to create and delete database tables
```

#### priorities.db

```
Database tables for storing titles and corresponding items
```

#### requirements.txt

```
blinker==1.8.2
click==8.1.7
colorama==0.4.6
cs50==9.3.4
cssbeautifier==1.15.1
djlint==1.34.1
EditorConfig==0.12.4
Flask==3.0.3
gunicorn==22.0.0
html-tag-names==0.1.2
html-void-elements==0.1.0
importlib_metadata==7.1.0
itsdangerous==2.2.0
Jinja2==3.1.4
jsbeautifier==1.15.1
json5==0.9.25
MarkupSafe==2.1.5
packaging==24.1
pathspec==0.12.1
PyYAML==6.0.1
regex==2023.12.25
six==1.16.0
SQLAlchemy==2.0.30
sqlparse==0.5.0
termcolor==2.4.0
tomli==2.0.1
tqdm==4.66.4
typing_extensions==4.12.2
Werkzeug==3.0.3
zipp==3.19.2
```

### templates/

#### - layout.html

```
basic page, fully responsive with title, menu and jinja main container template
bootstrap plugin for forms, buttons, layout, responsive menu
```

#### - index.html

```
homeage with introduction, rules and link to create new grid
preloader with app logo
```

#### - title.html

```
start of priority grid, with title as header for list of items
after submit redirect to items
```

#### - items.html

```
here are defined items, list of priorities
option to delete wrong item
button to continue to choose page
```

#### - choose.html

```
here are two buttons displayed where every represents one of items
written logic to count points for chosen item
items are shown and comapred as many times as all possible compares are made
after finish comparison, redirect to result page
```

#### - result.html

```
after all calculation from choose session, title and corresponding items are displayed
title, items name and count of points from "choosing game"
items are sorted on count from highest descending
```

#### - history.html

```
documentation for all titles and corresponding items with counted points
sorted from newest to oldest
option to try choosing items again
option to delete particular title and its items
```

#### - error.html

```
if errors occur -implemented in app.py - user is redirected to error page
error is displayed
button to go one page back to correct error
```

### static/

#### - styles.css

```
extended style of components
```

#### - assets/

```
images used in the app as logo
```

## To Do

- register and login user to make private lists
- create tables for user data storage
- reset function to start chosing again

#### This tool made my life a lot easier, i hope it will do same for you

### Enjoy!
