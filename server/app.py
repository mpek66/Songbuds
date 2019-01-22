from flask import Flask, jsonify
from flask_cors import CORS
from flask_heroku import Heroku
from models import db

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    return jsonify('pong!')

# get songs route
@app.route('/get_songs', methods=['GET'])
def get_songs():
    return jsonify({
        'status': 'success',
        'songs': SONGS
    })

if __name__ == '__main__':
    app.run()
