from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return '<h1 style="text-align:center">hello,bitch</h1>'
@app.route('/<name>')
def users(name):
    return '<h1 style="text-align:center">hello,%s</h1>' % name
if __name__ == '__main__':
    app.run()