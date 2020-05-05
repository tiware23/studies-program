#!/usr/bin/env
from flask import Flask, render_template, request,  escape
from vsearch import search4letters
from socket import gethostname

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/search4', methods=['POST']) # GET is Default Method.
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_title=title, the_results=results, 
                           the_letters=letters, the_phrase=phrase,)

@app.route('/') # The "entry_page" function now has two URLs associated with it.
@app.route('/entry')
def entry_page() -> 'html':
    host_name = gethostname()
    return render_template('entry.html', the_title="Welcome to search4letters on the web!", the_hostname=host_name)

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split("|"):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)

if __name__ == '__main__':
    app.run(host='0.0.0.0')