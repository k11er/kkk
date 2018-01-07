#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv
from pylab import *
def draw_pie(list1,list2):
    plt.pie(list2,labels=list1,autopct="%1.2f%%")
    # plt.ylabel('number')
    plt.title('hot label')
    # plt.rc('font', family = ['Microsoft YaHei'])

def draw_bar(list1,list2):
    width = 0.1
    plt.bar(list1,list2,
           width,bottom = 0,
           color='blue')
    plt.ylabel('number')
    plt.title('hot label')

handle = open('2017out.csv','r',encoding='UTF-8')
reader = csv.reader(handle)
list1 =[]
list2 =[]
for item in reader:
    list1.append(item[0])
    list2.append(item[1])
list1 = list1[11:]
list2 = list2[11:]
print(list1)
print(list2)
draw_bar(list1,list2)
#draw_pie(list1,list2)
plt.show()
