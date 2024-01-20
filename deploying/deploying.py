import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Sup Worldo<h2>'


host = '0.0.0.0'
port = os.environ.get('PORT', 5000)

app.run(host=host, port=port)
