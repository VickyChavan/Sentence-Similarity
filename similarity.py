from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException
from highlight import *

app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('home.html')

@app.route('/checker/', methods = ['POST'])
def checker():
    if request.method == 'POST':
        file1 = request.files['File1']
        h1 = file1.read().decode('utf-8').replace('\r', '').replace('\n', ' \\n')
        f2 = request.files['File2']
        h2 = f2.read().decode('utf-8').replace('\r', '').replace('\n', ' \\n')
        option = request.form['Option']
        if option == 'Line':
            k = line(h1, h2)
        else:
            k = sentence(h1, h2)
        c1 = mark_similar(h1, k, option)
        c2 = mark_similar(h2, k, option)
        return render_template('compare.html', file1 = c1, file2 = c2) 

@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template('error.html', error = e)

if __name__ == "__main__":
    app.run(debug = True)