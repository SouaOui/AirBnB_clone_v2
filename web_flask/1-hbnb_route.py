#!/usr/bin/python3
"""adding a route"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """default route home"""
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hello():
    """adding new route"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
