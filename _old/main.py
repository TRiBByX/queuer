# imports
from flask import Flask, render_template, redirect, url_for, flash, request
from scripts import runner
from model import *
from datetime import date, datetime


# Global
app = Flask(__name__)
app.config['SECRET_KEY'] = '!!!!!!!!!'

# Functions


def main():
    app.run('127.0.0.1', "8080", debug=True)


@app.route('/')
def redir():
    return redirect(url_for('queue'))


@app.route('/schedule/<string:script>', methods=['GET', 'POST'])
def scheduler(script):

    if script == 'empty':
        return render_template('run.html',
                               script={'scriptname': 'testname',
                                       'docstring': 'testdocstring',
                                       'author': 'testauthor',
                                       'options': ['testoption']},
                                date=date.today())

    Scripts = runner.get_scripts()
    if script.lower() in Scripts:
        script = Scripts[script.lower()]
    if request.method == "POST":
        try:
            jobname = request.form['jobname']
            options = [option for key, option in request.form.items()
                       if key in script.options]
            exectime = request.form['exectime']
            exectime = exectime[:10] + ' ' + exectime[-5:]
            exectime = datetime.strptime(exectime, "%Y-%m-%d %H:%M")
        except Exception as e:
            print(e)

        if not jobname:
            flash('Job name is required')
        elif not options:
            flash('Job options are required')
        elif not exectime:
            flash('Exec time is required')
        elif exectime < datetime.now():
            flash('Time has to be in the future')
        else:
            redirect(url_for('queue'))
        


    return render_template('run.html', script=script.to_dict(),
                           date=date.today())


@app.route("/queue")
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
        scripts.append({'scriptname': v.scriptname,
                        'docstring': v.docstring.split('\n')})
    return render_template('tasks.html', scripts=scripts)


if __name__ == "__main__":
    main()
