#!/usr/bin/env python3
"""
create get_locale function with babel.selector
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    config class for app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(config)


@babel.localeselector
def get_locale():
    """
    determine the best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
    return html page
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
