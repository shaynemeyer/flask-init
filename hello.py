import pymysql

from flask import Flask, url_for, request, render_template, redirect, flash, make_response, session
app = Flask(__name__)

import logging
from logging.handlers import RotatingFileHandler

# @app.route('/')
# def index():
#     return url_for('show_user_profile', username='Shayne')
#
# @app.route('/hello')
# def hello_world():
#     # import pdb; pdb.set_trace()
#     return 'Hello World!'
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return "User %s" % username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return "Post %d" % post_id

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'username is ' + request.values["username"]
#     else:
#         return '<form method="post" action="/login">' \
#            '<input type="text" name="username" />' \
#            '<p></p>' \
#            '<button type="submit">Submit</button></form>'


# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Successfully logged in")
            # response = make_response(redirect(url_for('welcome', username=request.form.get('username'))))
            # response.set_cookie('username', request.form.get('username'))
            # return response
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = 'Incorrect username and password'
            app.logger.warning('Incorrect username and password for user (%s)', request.form.get('username'))

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # response = make_response(redirect(url_for('login')))
    # response.set_cookie('username', '', expires=0)
    # return response
    session.pop('username', None)
    return redirect(url_for('login'))


def valid_login(username, password):
    # mysql
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = ''
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'my_flask_app'
    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST,
        user=MYSQL_DATABASE_USER,
        passwd=MYSQL_DATABASE_PASSWORD,
        db=MYSQL_DATABASE_DB
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * from user WHERE username='%s' AND password='%s'" % (username, password))
    data = cursor.fetchone()

    if data:
        return True
    else:
        return False


@app.route('/')
def welcome():
    # username = request.cookies.get('username')
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = '\x92p6a\xef\xff@\x9c\xe1\xb5S\x1b,\xde\xa2\xee\x00\xe9\xd2\xb2\xa4\xde\xf4\x9c'

    # Logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
