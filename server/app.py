from flask import Flask, jsonify, render_template, request, url_for, Session
from flask_cors import CORS
from flask_heroku import Heroku
from authentication import authenticator, session
from create import creator
from party import partyer
from extensions import db
from models import Users, Parties

def register_extensions(app):
    db.init_app(app)
    app.app_context().push()
    db.drop_all()
    db.create_all()


# instantiate the app
app = Flask(__name__)
app.register_blueprint(authenticator)
app.register_blueprint(creator)
app.register_blueprint(partyer)
app.config.from_pyfile('config.py')
heroku = Heroku(app)
CORS(app)
register_extensions(app)

if __name__ == '__main__':
    app.run(debug=True)
