#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print('动态抓取 -- 先学习数据库mongo(然而现在并没有连接上) 下面是MySql的相关用法 (ー ー゛)')

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='zhang')

cur = conn.cursor()

# cur.execute("INSERT INTO zhangTest(id, name) VALUES (15, 'xiu')")
#
# cur.execute("INSERT INTO zhangTest(id, name) VALUES (11, 'xiu')")
#
# cur.execute("INSERT INTO zhangTest(id, name) VALUES (12, 'xiu')")
#
# cur.execute("INSERT INTO zhangTest(id, name) VALUES (13, 'xiu')")
#
# cur.execute("INSERT INTO zhangTest(id, name) VALUES (14, 'xiu')")

cur.execute('SELECT * FROM zhang.zhangTest WHERE name = "%s"' % ('xiu')) # 这个后面的数据貌似要添加一个 () 然后里面写上对用的东西

result = cur.fetchall()

for res in result:
    print('id = %d' % res[0])
    print('name = %s' % res[1])

conn.commit()
cur.close()
conn.close()














