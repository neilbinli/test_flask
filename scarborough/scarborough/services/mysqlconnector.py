import pymysql


def get_conn(shost, suer, spasswd, sdb):
    conn = pymysql.connect(host=shost, user=suer, passwd=spasswd, db=sdb, charset='utf8', local_infile=True)
    return conn


def setup_cursor(dbc):
    dbc.execute('SET NAMES utf8;')
    dbc.execute('SET CHARACTER SET utf8;')
    dbc.execute('SET character_set_connection=utf8;')
    return dbc


def set_cursor(dbc):
    dbc.execute('SET NAMES utf8;')
    dbc.execute('SET CHARACTER SET utf8;')
    dbc.execute('SET character_set_connection=utf8;')
    return dbc


if __name__ == "__main__":
    get_conn()
