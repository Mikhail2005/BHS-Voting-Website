from website import app
from flask import render_template, redirect, request
from website.models import Prefects

@app.route('/', methods=['GET', 'POST'])
def divison():
    
    return render_template("division.html")

@app.route('/prefects', methods=['GET', 'POST'])
def prefects():
    results = Prefects.query.all()
    return render_template("prefects.html", results=results)

@app.route('/prefects', methods=['GET', 'POST'])
def prefects():
    results = Prefects.query.all()
    return render_template("prefects.html", results=results)

@app.route('/prefects', methods=['GET', 'POST'])
def prefects():
    results = Prefects.query.all()
    return render_template("prefects.html", results=results)



