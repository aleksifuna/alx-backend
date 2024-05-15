#!/usr/bin/env python3
"""
Defines a Flask APP
"""

from flask import Flask, render_template, request
from babel import Babel

class Config:
    """
    Configuration class for the app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'utc'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    Returns the best matched locale as per languages config
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def hello_world():
    """
    Handles root request
    """
    return render_template('0-index.html')
if __name__ == '__main__':
    app.run(debug=True)
