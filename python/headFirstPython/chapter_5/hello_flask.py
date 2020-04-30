#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/') # Function Decorator
def hello() -> str:
    return 'Hello world from Flask!'

app.run() # Asks the webapp to start running.