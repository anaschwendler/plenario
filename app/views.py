from flask import render_template
from app import app, db
from app.models import *

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')

@app.route('/senators')
def senators():
    senators = Senator.query.all()
    return render_template("senators.html", title='Senadores', senators=senators)

@app.route('/propositions')
def propositions():
    propositions = Proposition.query.all()
    votes = Vote.query.all()
    return render_template("propositions.html", title='Proposições', propositions=propositions, votes=votes)

@app.route('/about')
def about():
    return render_template("about.html", title='Sobre')