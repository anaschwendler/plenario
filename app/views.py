from flask import render_template
from app import app, db
from app.models import *

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html", title='Home')

@app.route('/senators')
def senators():
    senators = Senator.query.order_by('name asc').all()
    return render_template("senators.html", title='Senadores', senators=senators)

@app.route('/senator/<senator_name>')
def senator_page(senator_name):
    senator = Senator.query.filter_by(name=senator_name).first()
    if senator is None:
        return abort(404)
    else:
        return render_template("senator.html",senator=senator)

@app.route('/propositions')
def propositions():
    propositions = Proposition.query.all()
    votes = Vote.query.all()
    return render_template("propositions.html", title='Proposições', propositions=propositions, votes=votes)

@app.route('/proposition/<proposition_name>')
def proposition_page(proposition_name):
    proposition = Proposition.query.filter_by(name=proposition_name).first()
    if proposition is None:
        return abort(404)
    else:
        return render_template("proposition.html",proposition=proposition)

@app.route('/about')
def about():
    return render_template("about.html", title='Sobre')
