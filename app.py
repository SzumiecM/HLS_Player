from flask import Flask, render_template, send_from_directory, request, make_response
from os import walk
from flask_cors import cross_origin, CORS

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'paprask asfaksfbasbfh 15h21951 25hasf bfasjfa'
# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)


# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST', 'GET'])
def home():
    _, _, playlists = next(walk('playlists'))
    url = None

    if request.method == 'POST':
        chosen = request.form.get('existing_playlist')
        if not chosen:
            url = request.form.get('url')
            url = url.replace('watch?v=', 'embed/')
    else:
        chosen = playlists[-1]

    print(url)
    return render_template('home.html', playlists=playlists, chosen=chosen, url=url)


@app.route('/get/<path>/<file>')
def get_file(path, file):
    return send_from_directory(path, file)


@app.route('/redirect/')
def redirect():
    url = request.args.get('url')
    print(url)
    return url
