# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os


class TutorialPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        fiename = base_dir + '/news.txt'
        with open(fiename, 'a') as f:
            f.write(str(item['date']))
            f.write('\n')
            f.write(str(item['tags']))
            f.write('\n')
        return item
