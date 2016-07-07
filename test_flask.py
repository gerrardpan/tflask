from flask import Flask,request

app = Flask(__name__)
@app.route('/')
def home():
    ua = request.headers
    return '<h1 style="text-align:center">hello,bitch</h1><p>%s</p>' % ua
@app.route('/<name>')
def users(name):
    return '<h1 style="text-align:center">hello,%s</h1>' % name
if __name__ == '__main__':
    app.run()