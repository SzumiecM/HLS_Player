from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'paprask asfaksfbasbfh 15h21951 25hasf bfasjfa'


@app.route("/")
def hello_world():
    return render_template('home.html', )


@app.route('/get/<path>/<file>')
def get_file(path, file):
    response = send_from_directory(path, file)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
