from website import app
from flask import Blueprint, render_template

@app.route('/', methods=['GET', 'POST'])
def divison():
    return render_template("division.html")

@app.route('/prefects', methods=['GET', 'POST'])
def prefects():
    return render_template("prefects.html")

#@app.route('/', methods=['GET','POST'])
#def redirect():
    #return render_template("prefects.html")