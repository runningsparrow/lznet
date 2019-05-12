# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class LznetPipeline(object):
    def process_item(self, item, spider):
        #debug
        print "do nothing"
        return item

#数据存储
class MysqlPipeline(object):
    # 链接数据库
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='sparrow1',
                                    db='lznet', charset='utf8')

    # 数据存储
    def process_item(self, item, spider):
        cursor = self.conn.cursor()

        #查询是否已经存在
        cursor.execute('select * from district where district=%s and district_getdate=%s',(item['district'],item['district_getdate']))
        result = cursor.fetchone()
        if result:
            print u"已经存在: " + item['district'] + item['district_getdate']
        else:
            cursor.execute('insert into district value(null,%s,%s,%s,%s,0)', (item['district'],item['district_link'],item['district_title'],
                           item['district_getdate'],))
            print "insert one: " + item['district'] + item['district_getdate']
            self.conn.commit()
        return item

    #关闭数据库
    def close_spider(self,spider):
        self.conn.close()