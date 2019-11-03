from flask import Flask, render_template, request, jsonify, redirect, send_file
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

HOST1 = '192.168.1.5'
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
            sql = 'select * from login_user_pw where user="%s"' % user
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
            sql_is_confirmed = res[0][2]
            if sql_is_confirmed != 'True':
                error = 'The pw of user %s is not confirmed' % user
                logger.error(error)
            else:
                if user == sql_user and pw == sql_pw:
                    return jsonify(message='Login successfully for %s' % request.values['username'])
                else:
                    error = 'Invalid username/password for user %s and pw %s' % (user, pw)
                    logger.error(error)
    else:
        return render_template("login.html")
    return jsonify(message=error)


@app.route('/register_account', methods=['GET', 'POST'])
def register_account():
    if request.method == 'POST':
        if register_user(request.values['username'], request.values['password']):
            msg = "Successfully register with account %s" % request.values['username']
            return jsonify(message=msg)
        else:
            error = 'Invalid username/password'
            return jsonify(message=error)
    else:
        error = 'Invalid method'
        return jsonify(message=error)


@app.route('/retype_password', methods=['GET', 'POST'])
def retype_password():
    if request.method == 'GET':
        error = 'Invalid method'
        return jsonify(message=error)
    elif request.method == 'POST':
        if 'password' not in request.values.keys():
            return render_template('retype_password.html', user=request.values['username'])
        elif retype_user(request.values['username'], request.values['password']):
            msg = "Successfully confirm password with account %s" % request.values['username']
            return jsonify(message=msg)
        else:
            error = "Wrong password retyped or account %s was already confirmed" % request.values['username']
            return jsonify(message=error)
    else:
        error = 'Invalied method'
        return jsonify(message=error)


@app.route('/about/')
def about():
    return 'The about page'


@app.route('/mainpage', methods=['GET', 'POST'])
def mainpage():
    return render_template("mainpage.html")
    # return 'The main page'


def register_user(user, pw):
    conn = mysqlconnector.get_conn(HOST1, USER1, PASSWD1, DB1)
    try:
        cur = mysqlconnector.set_cursor(conn.cursor())
        sql = 'select * from login_user_pw where user="%s"' % user
        cur.execute(sql)
        res = cur.fetchall()

        if len(res) > 1:
            error = 'There are more than 1 password for user %s, check it please.' % user
            logger.error(error)
            return False
        elif len(res) == 1:
            if res[0][2] == 'True':
                error = 'The password for user %s is already confirmed, check it please.' % user
                logger.error(error)
                return False
            else:
                sql = 'delete from login_user_pw where user="%s"' % user
                cur.execute(sql)
                conn.commit()
                sql = 'insert into login_user_pw (user, password, confirmed) values ("%s", "%s", "%s")' \
                      % (user, pw, 'False')
                cur.execute(sql)
                conn.commit()
                return True
        else:
            sql = 'insert into login_user_pw (user, password, confirmed) values ("%s", "%s", "%s")' \
                  % (user, pw, 'False')
            cur.execute(sql)
            conn.commit()
    except Exception as e:
        msg = 'Exception %s in login when querying login_user_pw with user=%s' % (e, user)
        logger.error(msg)

    finally:
        conn.close()
    return True


def retype_user(user, pw):
    conn = mysqlconnector.get_conn(HOST1, USER1, PASSWD1, DB1)
    try:
        cur = mysqlconnector.set_cursor(conn.cursor())
        sql = 'select * from login_user_pw where user="%s"' % user
        cur.execute(sql)
        res = cur.fetchall()

        if len(res) > 1:
            error = 'There are more than 1 password for user %s, check it please.' % user
            logger.error(error)
            return False
        elif len(res) == 1:
            if res[0][2] == 'True':
                error = 'The password for user %s is already confirmed, check it please.' % user
                logger.error(error)
                return False
            else:
                if pw == res[0][1]:
                    sql = 'update login_user_pw  set confirmed="True" where user="%s"' % user
                    cur.execute(sql)
                    conn.commit()
                    return True
                else:
                    error = 'The password for user %s is inconsistent with init one, check it please.' % user
                    logger.error(error)
                    return False
        else:
            error = 'There is not account for %s, check it please.' % user
            logger.error(error)
            return False
    except Exception as e:
        msg = 'Exception %s in login when querying login_user_pw with user=%s' % (e, user)
        logger.error(msg)

    finally:
        conn.close()
    return True


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
