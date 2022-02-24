

from flask import render_template, url_for, flash, redirect, request
from flaskoffice import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/offices")
def offices():
    return render_template('offices.html', title='Offices')