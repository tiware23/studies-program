#!/usr/bin/env
from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST']) # GET is Default Method.
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    ret = search4letters(phrase, letters)  
    return f'The search returned this letter: {ret}'

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to search4letters on the web!")

app.run(port=8080, debug=True)