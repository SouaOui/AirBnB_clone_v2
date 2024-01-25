#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_page(n):
    """display a number with its nature"""
    return render_template('number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

