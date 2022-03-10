from unicodedata import name
from flask import Flask
app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return 'Hello, ' + name

@app.route('/repeat/<num>/<name>')
def num(num, name):
    i = 0
    str = ''
    for i in range(i, int(num) + 1, 1):
        str += name + ' '
    return str

@app.route('/<misc>')
def sorry(misc):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(debug=True, port=5001)