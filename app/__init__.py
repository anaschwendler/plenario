from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from whitenoise import WhiteNoise

app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')

db = SQLAlchemy(app)

alembic = Alembic()
alembic.init_app(app)

from app import views, models