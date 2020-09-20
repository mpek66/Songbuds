from flask_sqlalchemy import SQLAlchemy
from extensions import db

class Users(db.Model):
    __tablename__ = "Users"
    email = db.Column(db.Text(), primary_key=True)
    password = db.Column(db.Text())

    def __init__ (self, email, password):
        self.email = email
        self.password = password

class Parties(db.Model):
    __tablename__ = "Parties"
    user = db.Column(db.Text(), primary_key=True)
    songs = db.Column(db.PickleType())
    users = db.Column(db.PickleType())

    def __init__(self, user, songs, users):
        self.user = user
        self.songs = songs
        self.users = users
