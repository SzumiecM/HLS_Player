from flask import Flask, render_template, send_from_directory, request, make_response
from os import walk
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST', 'GET'])
def home():
    playlists = [playlist for _, _, playlist in walk('playlists')][0]
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
