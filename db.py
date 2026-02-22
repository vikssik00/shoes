import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="shoes",
        cursorclass=pymysql.cursors.DictCursor
    )
