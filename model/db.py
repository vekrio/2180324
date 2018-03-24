
import pymysql
import config

class DbConnection:
    def __init__(self):
        self.__conn_dict  config.py

#连接数据库
conn =pymysql.connect(
    host='192.168.107.184',
    user='sa',
    password='1qaz@wsx',
    port=1433   ,
    database='riji',
    charset='utf8'
)
print(conn)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql ='select = from diary'
cursor.execute(sql)
rows =cursor.fetchall()
cursor.close()
conn.close()
print(rows)