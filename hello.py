from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return url_for('show_user_profile', username='Shayne')

@app.route('/hello')
def hello_world():
    # import pdb; pdb.set_trace()
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return "User %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post %d" % post_id

if __name__ == '__main__':
    app.debug = True
    app.run()
