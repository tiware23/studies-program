#!/usr/bin/env
from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

@app.route('/search4', methods=['POST']) # GET is Default Method.
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_title=title, the_results=results, 
                           the_letters=letters, the_phrase=phrase,)

@app.route('/') # The "entry_page" function now has two URLs associated with it.
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to search4letters on the web!")

if __name__ == '__main__':
    app.run(host='0.0.0.0')