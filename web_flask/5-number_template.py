#!/usr/bin/python3
"""
Starts the Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """displays C followed by the value of text."""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """displays Python followed by the value of text."""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>')
def nisnumber(n):
    """displays n is a number only if n is an integer."""
    if isinstance(n, int) is True:
        return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays a HTML page only if n is an integer."""
    if isinstance(n, int) is True:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
