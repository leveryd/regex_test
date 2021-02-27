"""
https://github.com/PyMySQL/PyMySQL/issues/967
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='SSL@bce123',
                             database='mysql',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:

    with connection.cursor() as cursor:
        sql = "insert xxx_table values" + "(%s" + ",%(x)s" * 100 + "from mysql.user"
        cursor.executemany(sql, ('xx',))
        result = cursor.fetchone()
        print(result)
