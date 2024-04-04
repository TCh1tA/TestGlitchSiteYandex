from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия колонизации Марса'


@app.route('/index')
def yabloki():
    return 'И на Марсе будут яблони цвести!'


if __name__ == "__main__":
    app.run('127.0.0.1', port=8080)
