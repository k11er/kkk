# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import pymysql
import pymysql.cursors


class TutorialPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        fiename = base_dir + '/news.txt'
        with open(fiename, 'a') as f:
            f.write(str(item['date']))
            f.write('\n')
            f.write(str(item['tag0']))
            f.write('\n')
            f.write(str(item['tag1']))
            f.write('\n')
            f.write(str(item['tag2']))
            f.write('\n')
            f.write(str(item['tag3']))
            f.write('\n')
            f.write(str(item['tag4']))
            f.write('\n')
        return item

class mysqlPipeline(object):
    def process_item(self,item,spider):
        '''
        将爬取的信息保存到mysql
        '''
        # 将item里的数据拿出来
        date = item['date']
        tag0 = item['tag0']
        tag1 = item['tag1']
        tag2 = item['tag2']
        tag3 = item['tag3']
        tag4 = item['tag4']

        db = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',  # 自己的mysql用户名
            passwd='',  # 自己的密码
            db='scrapyDB',  # 数据库的名字
            charset='utf8mb4',  # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode = True)
        try:
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 插入语句
            sql = "INSERT INTO news(date,tag0,tag1,tag2,tag3,tag4)" \
                  "VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (date,tag0,tag1,tag2,tag3,tag4)
            # sql = "INSERT INTO news(date,tag0,tag1,tag2,tag3,tag4)" \
            #       "VALUES('2000.0.0', 'b', 'c', 'd', 'e', 'f')"
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        finally:
            # 关闭连接
            db.close()
        return item