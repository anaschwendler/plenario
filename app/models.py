from app import db
from sqlalchemy.dialects.postgresql import JSON
import enum

class VoteType(enum.Enum):
    __tablename__ = 'votetype'

    positive = "A favor"
    negative = "Contra"
    absence = "Ausência"
    abstention = "Abstenção"

class Senator(db.Model):
    __tablename__ = 'senator'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    party = db.Column(db.String(30), index=True)
    party_number = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(5), index=True)
    description1 = db.Column(db.Text)
    description2 = db.Column(db.Text)
    source = db.Column(db.String(120), unique=False)
    twitter = db.Column(db.String(120), unique=False)
    facebook = db.Column(db.String(120), unique=False)
    instagram = db.Column(db.String(120), unique=False)

class Proposition(db.Model):
    __tablename__ = 'proposition'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    proposition = db.Column(db.String(120), unique=True, index=True)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)
    link = db.Column(db.String(120))

class Vote(db.Model):
    __tablename__ = 'vote'

    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.Enum(VoteType))
    senator = db.Column(db.Integer, db.ForeignKey('senator.id'))
    proposition = db.Column(db.Integer, db.ForeignKey('proposition.id'))
