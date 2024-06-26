<div align="center">

<img src="https://github.com/krisbaranski/priority_grid/blob/main/static/assets/priority.png" alt="Priority Grid Logo" width="150" height="150">

#

# Priority Grid

</div>

#### Video Demo:

## Tech Stack

#### Flask, Python, JavaScript, SQLite3, HTML, CSS, Bootstrap

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

## What is it about

This app is made to specify, what your priorities in specific subject are (i.e. qualities, tasks...).
For that, i implement some code, where you can specify important properties as a list.
It will then go through a random loop of these properties, showing them as pairs.
There you can choose only one, which is more of value. It continue till all properties were meet once.
In the end, you will get a list of key:value pairs of these properties, ordered descending.
The property on top have the most "clicks" and last one the least "clicks".
Thats how your properties will give a result of priority grid. From most to least important.
You can make as many headings as you like or need or create a new list to prioritize.
You can also run your "test" again after reset.

## How to use it

here i explain how to use the grid

## Specifications

Download and install VSCode (or other code editor) for local work

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
`flask run`

## Steps of building app

- Flask basic files ( app.py, helpers.py, /templates, /static, /assets, styles.css)
- Preloader animation with logo on layout page (CSS, JavaScript)
- Bootstrap responsive navigation menu, buttons, layout, fonts, lists
- SQLite3 tables to store data
-

## Some stuff

I hope it can help you and make your priorities work for you!

### Enjoy!
