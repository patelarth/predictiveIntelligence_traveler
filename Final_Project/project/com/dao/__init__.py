import pymysql


def con():
    return pymysql.connect(
        host = 'localhost',
        user = 'root',
        port = 3306,
        password = '',
        database = 'finalproject',
        cursorclass = pymysql.cursors.DictCursor
    )