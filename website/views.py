from website import app
from flask import Blueprint, render_template

@app.route('/', methods=['GET', 'POST'])
def divison():
    return render_template("division.html")