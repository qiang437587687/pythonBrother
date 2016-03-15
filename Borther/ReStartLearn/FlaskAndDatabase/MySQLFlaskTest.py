
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='zhang', charset='utf8')

# conn = pymysql.connect(host='localhost', user='', passwd='', db='zhang', charset='utf8')

cur = conn.cursor()

# cur.execute("INSERT INTO zhangTest(id, name) VALUES (15, 'xiu')")

sta = cur.execute("insert into zhangTest(id, name) VALUES (67, 'zhangxianqiang')")

conn.commit()
cur.close()
conn.close()

