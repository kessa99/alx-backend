#!/usr/bin/env python3
"""
install and initiate babel flask extension
"""

from flask import Flask, render_template
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


app.config.from_object(Config)


@app.route('/')
def home():
    """
    function for babel flask
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
