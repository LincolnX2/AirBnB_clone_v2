#!/usr/bin/python3
"""
script to start Flash web application
listens on 0.0.0.0, port 5000
routes: /: display "Hello HBNB!"
strict_slashes=False
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

app.run(host='0.0.0.0', port='5000')
