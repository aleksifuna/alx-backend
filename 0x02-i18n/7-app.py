#!/usr/bin/env python3
"""
Defines a Flask APP
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union
from pytz import timezone
import pytz

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    gets user related to login_as from request parameter
    """
    if 'login_as' in request.args:
        id = request.args.get('login_as')
        return users.get(int(id))
    return None


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


@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    gets and return the locale
    """
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Gets and return the timezone
    """
    if 'timezone' in request.args:
        tz = request.args.get('timezone')
        try:
            return timezone(tz).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        tz = g.user['timezone']
        try:
            return timezone(tz).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def hello_world():
    """
    Handles root request
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
