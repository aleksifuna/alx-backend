#!/usr/bin/env python3
"""
Defines a Flask APP
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for the app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello_world():
    """
    Handles root request
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
