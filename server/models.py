from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "Users"
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)

    def __init__ (self, email, password):
        self.email = email
        self.password = password
