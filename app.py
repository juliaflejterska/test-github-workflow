"""
Module that contains a Flask application.

This module defines the Flask app that serves the website.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """
    Index page of the website.

    This function returns a string containing an HTML response.
    """
    return '<h1>Hello WSB! Greetings from Flask!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
