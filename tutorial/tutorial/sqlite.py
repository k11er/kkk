#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''CREATE TABLE DATA
  (date  NOT NULL,
   tag_1 CHAR(30),
   tag_2 CHAR(30),
   tag_3 CHAR(30),
   tag_4 CHAR(30),
   tag_5 CHAR(30))''')
print('table create')
conn.commit()
conn.close()

print("opened database successfully");