# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
import xiciTest.settings


class XicitestPipeline(object):

    def process_item(self, item, spider):

        DBKWARGS = spider.settings.get('DBKWARGS')

        con = pymysql.connect(**DBKWARGS)

        cur = con.cursor()

        lis = (item['IP'], item['PORT'], item['TYPE'], item['SPEED'], item['LAST_CHECK_TIME'])

        cur.execute('CREATE TABLE IF NOT EXISTS proxy(IP varchar(50) PRIMARY KEY, PORT varchar(50),'
                    'TYPE varchar(50),SPEED varchar(50),LAST_CHECK_TIME varchar(50), POSITION varchar(50))')

        exsitObject = cur.execute('SELECT * FROM zhang.proxy WHERE IP = "%s"' % lis[0])

        sql = ''
        data = ()

        if not exsitObject:

            sql = ('INSERT INTO proxy(IP,PORT, TYPE, SPEED, LAST_CHECK_TIME) VALUES (%s, %s, %s, %s, %s)')
            data = lis
        else:

            sql = ('UPDATE proxy SET LAST_CHECK_TIME = %s WHERE IP = %s')
            data = (lis[4], lis[0])

        print(lis)

        try:
            cur.execute(sql, data)
        except Exception as e:  # python3 中要用 as
            print('insert error', e)
            print('#####################################fail################################################')
            con.rollback()
        else:
            con.commit()
            print('====================================success===============================================')

        cur.close()

        con.commit()

        return item


