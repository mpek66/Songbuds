from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "Users"
    email = db.Column(db.Text(), primary_key=True)
    password = db.Column(db.Text())

    def __init__ (self, email, password):
        self.email = email
        self.password = password
