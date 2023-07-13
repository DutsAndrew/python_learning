# Pylance will throw warnings in VSCode as it does not know that the virtual env has the dependencies installed.
# CLI will need to be in the virtual env for the project, the virtual env will store things in the nearby folder, in this case "my_flask_env

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

if __name__ == "__main__":
    app.run()

# run this file in command line to start server