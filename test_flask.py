from flask import Flask, request, render_template
import sqlite3,os
from flask.ext.wtf import Form
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
isreturn = 0
def tdb():
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        #cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        #cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
        #cursor.close()
        #conn.commit()
        #conn.close()
        # 关闭Connection:
        print(cursor.rowcount)
        #conn = sqlite3.connect('test.db')
        #cursor = conn.cursor()
        cursor.execute('select * from user where id=?', ('3',))
        values = cursor.fetchall()
        cursor.close()
        conn.close()
        print(values)
        return values

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
        us = tdb()
        #print('sfsfsfsfsafafadsfafsafff'+us+'sfsafdasfasfaf')
        if(ty == 'all'):
            s = '''<li><a href='/'>%s</a></li>
             <li><a href='/'>bbbbbbbbbbbbbbbbb</a></li>
             <li><a href='/'>ccccccccccccccccc</a></li>''' % ty
        return s

@app.route('/<name>')
def nam(name):
    if(isreturn==0):
        ua = request.headers
        return render_template('personal.html', name=name)



if __name__ == '__main__':
    app.run()