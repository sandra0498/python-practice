
from flask import Flask 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>My Flask App </h1>"
def index():
    return "<img src = 'moving_circle.gif' >"

# @app.route('/upload', methods=['POST'])
# def


if __name__ == '__main__':
    app.run()