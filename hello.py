from flask import Flask, url_for, request, render_template, redirect, flash, make_response
app = Flask(__name__)

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
            response = make_response(redirect(url_for('welcome', username=request.form.get('username'))))
            response.set_cookie('username', request.form.get('username'))
            return response
        else:
            error = 'Incorrect username and password'

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    return response


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


@app.route('/')
def welcome():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'SuperSecretKey'
    app.run()
