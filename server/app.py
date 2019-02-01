from flask import Flask, jsonify, render_template, request, url_for, Session
from flask_cors import CORS
from flask_heroku import Heroku
from models import db, Users
from authentication import authenticator
from authentication import session

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.register_blueprint(authenticator)
app.config.from_pyfile('config.py')
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
heroku = Heroku(app)
db.init_app(app)

# enable CORS
#TODO: Make this secure (with current implementation any website can
#successfully make cross-site requests, NOT SAFE)
CORS(app)

SONGS = [
    {
        'title': 'Losin Control',
        'artist': 'Russ',
        'enjoyed': True
    },
    {
        'title': 'Saccharine',
        'artist': 'Idk',
        'enjoyed': True
    },
    {
        'title': 'Sunny Duet',
        'artist': 'ShadowBox',
        'enjoyed': False
    }
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    print(session["profile_data"])
    return ""

# get songs route
@app.route('/get_songs', methods=['GET'])
def get_songs():
    return jsonify({
        'status': 'success',
        'songs': SONGS
    })

# an example/test route for submitting data to server
@app.route("/")
def enter_data():
    return ("""
<html>
    <head>
        <title>data entry</title>
    </head>
    <body>
        <form method="POST" action="/submit">
            <label for="mydata">Gimme your data, fool!</label>
            <input type="text" id="email" name="email">
            <input type="text" id="password" name="password">
            <button type="submit">IT FEEDS IT THE DATA</button>
        </form>
    </body>
</html>
    """)

@app.route("/submit", methods=["POST"])
def post_to_db():
    indata = Users(request.form["email"], request.form["password"])
    try:
        db.session.add(indata)
        db.session.commit()
    except Exception as e:
        print(e)
    return 'Success! To enter more data, <a href="{}">click here!</a>'.format(url_for("enter_data"))

if __name__ == '__main__':
    app.run(debug=True)
