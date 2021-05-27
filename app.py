from flask import Flask, render_template, send_from_directory, request
from os import walk

app = Flask(__name__)
app.config['SECRET_KEY'] = 'paprask asfaksfbasbfh 15h21951 25hasf bfasjfa'


@app.route('/', methods=['POST', 'GET'])
def home():
    _, _, playlists = next(walk('playlists'))

    if request.method == 'POST':
        chosen = request.form.get('existing_playlist')
    else:
        chosen = playlists[-1]

    return render_template('home.html', playlists=playlists, chosen=chosen)


@app.route('/get/<path>/<file>')
def get_file(path, file):
    response = send_from_directory(path, file)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
