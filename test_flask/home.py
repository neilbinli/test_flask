from flask import Flask, render_template, request, jsonify
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import scarborough.services.mysqlconnector as mysqlconnector
import logging
from scarborough.utils.logger import config_logging

logger = logging.getLogger('home')
config_logging('home')


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

HOST1 = '0.0.0.0'
USER1 = 'root'
PASSWD1 = 'Welcome2019!'
DB1 = 'scarborough'
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
    error = ''
    if request.method == 'POST':
        user = request.values['username']
        pw = request.values['password']
        conn = mysqlconnector.get_conn(HOST1, USER1, PASSWD1, DB1)
        res = None
        try:
            cur = mysqlconnector.set_cursor(conn.cursor())
            sql = 'select * from login_user_pw where user=%s' % user
            cur.execute(sql)
            res = cur.fetchall()

        except Exception as e:
            msg = 'Exception %s in login when querying login_user_pw with user=%s' % (e, user)
            logger.error(msg)

        finally:
            conn.close()

        if len(res) > 1:
            error = 'There are more than 1 password for user %s, check it please.' % user
            logger.error(error)
        elif len(res) == 0:
            error = 'There are no result for user %s, check it please.' % user
            logger.error(error)
        else:
            sql_user = res[0][0]
            sql_pw = res[0][1]
            sql_is_confirmed = bool(res[0][2])
            if not sql_is_confirmed:
                error = 'The pw of user %s is not confirmed' % user
                logger.error(error)
            else:
                if user == sql_user and pw == sql_pw:
                    return jsonify(message='login successfully for %s' % request.values['username'])
                else:
                    error = 'Invalid username/password for user %s and pw %s' % (user, pw)
                    logger.error(error)
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
