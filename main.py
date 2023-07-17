# Imports
from flask import Flask, render_template, redirect, url_for
from scripts import runner
from helpers import db_helper

import sqlite3

# Global
app = Flask(__name__)

# Functions
def main():
    app.run('0.0.0.0', "8080", debug=True)

# Routes
@app.route('/')
def redir():
    return redirect(url_for('queue'))

@app.route('/run/<string:script>', methods=['GET', 'POST'])
def run(script):
    return f'<h1> Run: {script}!</h1>'


@app.route("/queue", methods=('GET', 'POST'))
def queue():
    messages = [{'title': 'Message One',
                 'content': 'Message one content'},
                {'title': 'Message two',
                 'content': 'Message two content'}]
    archive = [{'title': 'Message One',
                 'content': 'Message one content'},
                {'title': 'Message two',
                 'content': 'Message two content'}]

    return render_template('queue.html', messages=messages, archive=archive)

@app.route("/tasks")
def tasks():
    Scripts = runner.get_scripts()
    scripts = []
    for k, v in Scripts.items():
        scripts.append({'scriptname': v.scriptname, 'docstring': v.docstring.split('\n')})
    return render_template('tasks.html', scripts=scripts)


if __name__ == "__main__":
    main()