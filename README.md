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

- ABC analysis,
- Pareto analysis,
- Eisenhower Box...

For more information follow this [link](https://en.wikipedia.org/wiki/Time_management#The_Eisenhower_Method)

The method i implement is the **Prioritization Matrix**

<div align="center">

<img src="https://github.com/krisbaranski/priority_grid/blob/main/static/assets/prioritization_matrix.png" alt="Prioritization Matrix" width="350" height="auto">

</div>

<br/>

## What is it about and how to use it

#### Explanation

This app is made to specify, what your priorities in specific subject are (i.e. qualities, tasks, todos ...).
Often when we have some priorities, it doesn't come obvious what is their right prior order.

One can do it manually. It will take some work to write things on paper, count them, replace items... So, as you can see, its time consuming.
Therefore here you have an easy web app to create a list and order your items. With a few clicks you will get your list prioritized.

In this app you can specify important properties as a list.
Then the app go through a random loop of those properties, showing them as pairs.
There you can choose only one, which is more of value. It continue until all properties were meet once.
In the end, you get a result as a list of key:value pairs of those properties, ordered descending.
The property on top have the most "points" and last one the least or no "points".
Thats how your properties will give a result of priority grid. From most to least important.

You can make as many headings as you like and you can create a new list to prioritize.
You can also run your "matrix" again after reset.
Consider that number of your items will give multiple pairs i.e. 6 items = 15 possible pairs, 10 items = 45. So it can still take some time to figure out.

#### Rules

1. give a title to your list of priority grid items, i.e.
   `Qualities`
2. create a list of items to work with, i.e.
   `Strong`
   `Fast`
   `Something`
   `...`
3. now you get pairs of items. Choose only one of them, which is more valuable for you
   `Strong` OR `Fast`
4. those pairs will continue until all possible combinations are shown (i.e. 6 items = 15 possible pairs)
5. when finished, you will be redirected to result site where you get a list of your items sorted from most for least important

###

## Install ide, tools and dependencies

Download and install VSCode (or code editor of your choice) for local work

Install python3, to check current version:
`python3 --version`

Inside of the app directory, install virtual environment:
`pip3 install virtualenv`

To use flask run command, install virtual env:
`virtualenv env`

Start using virtual env:
`source env/bin/activate`

Install flask:
`pip3 install flask`

Start local server to see the development in browser (localhost:5000):
`flask run` or
`python3 app.py`

You can also install gunicorn for local testing
`pip install gunicorn`

# Build up

```
- Flask basic files ( app.py, /templates, /static/assets, styles.css)
- Preloader animation with logo on index page (CSS, JavaScript)
- Introduction and "rules of game" on index site as accordion
- Bootstrap responsive navigation menu, buttons, layout, fonts, lists
- SQLite3 tables to store data in db (priorities.db)
- Python implementation of choosing "game"
- History of your priorities
- Possibility to add, change, delete grids titles and/or items
- Config file for generating secret_key
- Checking functionality
- Debugging, fixing bugs
-
```

# Structure

### app.py

```
- import of dependencies (Flask, os, config, random, sqlite3)
- define functions for:
    > database,
    > routes
```

#### config.py

```
configure automatically generated secret_key
```

#### backup.txt

```
sqlite3 commands to create and delete tables
```

#### priorities.db

```
Database tables for storing titles and corresponding items
```

### templates/

#### - layout.html

```
basic site, fully responsive with title, menu and jinja main container template
bootstrap plugin for forms, buttons, layout, responsive menu
```

#### - index.html

```
home site with introduction, rules and link to create new grid
```

#### - title.html

```
start of priority grid, with title as header for list of items
after submit redirecting to items
```

#### - items.html

```
here are defined items, list of priorities
option to delete wrong item
button to continue to choose site
```

#### - choose.html

```
here two buttons are displayed which represent one of items
written logic to count points for chosen one of items
items "connect to each other as many times as on presented grid"
when all possible connnections finished, redirect to result site
```

#### - result.html

```
after all calculation from choose session, title and its items are displayed with name and count of points from "game"
items are sorted on count from highest descending
```

#### - history.html

```
documentation for all titles and corresponding items
sorted from newest to oldest
there is option to try choosing items again
or delete explicit title and its items
```

#### - error.html

```
if errors occur, user is redirected to this site
error is explained
button to go back one page to correct error
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

### requirements.txt

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

##

#### This tool made my life a lot easier, i hope it will do same for you

### Enjoy!
