from flask import Flask, render_template, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def hello_world():
    return render_template('login.html')


@app.route('/<username>')
def show_user_profile(username):
    return 'Hello %s!' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    test = ["test0", "test1", "test2", ]
    return render_template('login.html', test=test)


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
