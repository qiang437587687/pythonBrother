#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("SQLite")

import sqlite3

# 连接到数据库 如果不存在那么就创建一个数据库
conn = sqlite3.connect('SQLTest.db')

# 创建一个Cursor:
cursor = conn.cursor()

# 执行一个SQL语句 创建一个user表:

cursor.execute('CREATE TABLE IF NOT EXISTS user (id VARCHAR (20) PRIMARY KEY, name VARCHAR (20))')

# cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'zhang\')')

print(cursor.rowcount)

cursor.close()

conn.commit()

conn.close()


# 以上是存储的过程下面是 提取的过程

connn = sqlite3.connect('SQLTest.db')

cursorr = connn.cursor()

cursorr.execute('SELECT * FROM user WHERE id=?', '1')

values = cursorr.fetchall()

print(values)

cursorr.close()

connn.close()



