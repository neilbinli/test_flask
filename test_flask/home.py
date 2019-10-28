from flask import Flask, render_template, request, jsonify
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

dic_user_pw = {'libertybreeze@163.com': '123456',
               }


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
    error = None
    if request.method == 'POST':
        if valid_login(request.values['username'], request.values['password']):
            return jsonify(message='login successfully for %s' % request.values['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route('/register_retype_password', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if valid_login(request.values['username'], request.values['password']):
            return jsonify(message='register successfully for %s' % request.values['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route('/about')
def about():
    return 'The about page'


def valid_login(user, pw):
    if pw == dic_user_pw[user]:
        return True
    else:
        return False


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
