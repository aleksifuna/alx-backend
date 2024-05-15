#!/usr/bin/env python3
"""
Defines a Flask APP
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Handles root request
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
