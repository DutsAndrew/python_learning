# Pylance will throw warnings in VSCode as it does not know that the virtual env has the dependencies installed.
# CLI will need to be in the virtual env for the project, the virtual env will store things in the nearby folder, in this case "my_flask_env

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/index')
def index():
  name = 'Rosalia'
  return render_template('index.html', title='welcome', username=name)

if __name__ == "__main__":
    app.run(debug=True)

# run this file in command line to start server