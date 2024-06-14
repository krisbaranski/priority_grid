<div align="center">

<img src="https://github.com/krisbaranski/priority_grid/blob/main/static/assets/priority.png" alt="Priority Grid Logo" width="150" height="150">

#

# Priority Grid

</div>

#### Video Demo:

## Introduction:

#### Webapp made in Flask, Python, JavaScript, SQLite3, HTML, CSS, Bootstrap.

Prioritizing methods utilizes the principles of importance and urgency to organize priorities and workload.
Here are some different approaches:

- ABC analysis,
- Pareto analysis,
- Eisenhower Box...

For more information follow this [link](https://en.wikipedia.org/wiki/Time_management#The_Eisenhower_Method)

The method i implement is the **Prioritization Matrix**

<div align="center">

<img src="https://github.com/krisbaranski/priority_grid/blob/main/static/assets/prioritization_matrix.png" alt="Prioritization Matrix" width="350" height="auto">

</div>

<br/>

This app is made - as its name already say - to specify, what your priorities are (in right order).
For that, i implemented some code, where you can specify important properties as a list.
Then, going through a random loop, these properties are shown as pairs, where you can choose only one, which is more of value.
In the end, you will get an "ordered" list, where the property on top have the most "clicks" and last one the least "clicks".
Thats how your properties will give a result of priority grid. From most to least important.
You can make as many headings as you like or need. You can also run your "test" again after reset.

## How to

here i explain how to use the grid

## Specification

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
