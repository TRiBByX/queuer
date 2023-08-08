from flask import Flask, render_template, redirect, url_for, flash, request
from datetime import date, datetime
from models import *
from static import *
from db import *

app = Flask('Queuer')


def main():
    app.run('127.0.0.1', '8080', debug=True)


@app.route('/')
def front_page():
    return render_template('')


if __name__ == '__main__':
    main()
