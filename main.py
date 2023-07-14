# Imports
from flask import Flask, render_template, redirect, url_for
from scripts import runner

# Global
app = Flask(__name__)

# Functions
def main():
    app.run('0.0.0.0', "8080", debug=True)

# Routes
@app.route('/')
def redir():
    return redirect(url_for('queue'))


@app.route("/queue", methods=('GET', 'POST'))
def queue():
    messages = [{'title': 'Message One',
                 'content': 'Message one content'},
                {'title': 'Message two',
                 'content': 'Message two content'}]

    return render_template('queue.html', messages=messages)

@app.route("/tasks")
def tasks():
    Scripts = runner.get_scripts()
    scripts = []
    for k, v in Scripts.items():
        scripts.append({'scriptname': v.scriptname, 'docstring': v.docstring.split('\n')})
    print(scripts)
    return render_template('tasks.html', scripts=scripts)






if __name__ == "__main__":
    main()