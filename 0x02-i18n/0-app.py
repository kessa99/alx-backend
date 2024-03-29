#!/usr/bin/env python3
"""
firsttask: create simple setup basic flask
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    render the home page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
