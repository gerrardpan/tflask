from flask import Flask, request, render_template
from flask.ext.wtf import Form
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
isreturn = 0

@app.route('/')
def home():
    if(isreturn==0):
        ua = request.headers
        return render_template('personal.html')
    pass

@app.route('/artlist/<type>')
def users(type):
    if(isreturn==0):
        ty = type
        if(ty == 'all'):
            s = '''<li><a href='/'>aaaaaaaaaaaaaaaaaaa</a></li>
             <li><a href='/'>bbbbbbbbbbbbbbbbbbb</a></li>
             <li><a href='/'>ccccccccccccccccccc</a></li>'''
        return s

@app.route('/<name>')
def nam(name):
    if(isreturn==0):
        ua = request.headers
        return render_template('personal.html', name=name)

if __name__ == '__main__':
    app.run()