import os
import sqlite3

if os.path.exists('data.db'):
    os.remove('data.db')
    conn=sqlite3.connect("data.db")##实体数据库，也可以链接内存数据库
    cursor=conn.cursor()
    cursor.execute('create table askdata (time text,tag0 text,tag1 text,tag2 text,tag3 text,tag4 text)')
    conn.commit()
else:
    conn=sqlite3.connect("data.db")##实体数据库，也可以链接内存数据库
    cursor=conn.cursor()
    cursor.execute('create table askdata (time text,tag0 text,tag1 text,tag2 text,tag3 text,tag4 text)')
    conn.commit()

os.system('scrapy crawl csdnASK')
