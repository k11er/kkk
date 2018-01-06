# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3


class TutorialPipeline(object):
    def process_item(self, item, spider):
        conn=sqlite3.connect("data.db")
        cursor=conn.cursor()
        cursor.execute('insert into askdata values (?,?,?,?,?,?)',(str(item['date']),str(item['tag0']),str(item['tag1']),str(item['tag2']),str(item['tag3']),str(item['tag4'])))
        cursor.execute('select * from askdata ')
        result=cursor.fetchall()
        print(result)
        conn.commit()
        return item
