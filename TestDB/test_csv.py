# coding:utf-8

"""
csv 文件常用的方法
"""
import csv
import pandas

with open('files/data.csv','w') as f:
    writer=csv.writer(f,delimiter=' ')
    writer.writerow(['id','name','age'])
    writer.writerow(['1001','name1',20])
    writer.writerow(['1002','name2',21])
    writer.writerow(['1003','name3',22])

with open('files/data2.csv','w') as f:
    fields=['id','name','age']
    writer=csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerow({'id':'1','name':'n1','age':20})
    writer.writerow({'id':'2','name':'n2','age':20})
    writer.writerow({'id':'3','name':'n3','age':20})

with open('files/data2.csv','a',encoding='gbk') as f:
    fields=['id','name','age']
    writer=csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerow({'id':'1','name':'王伟','age':20})
    writer.writerow({'id':'2','name':'王二','age':20})
    writer.writerow({'id':'3','name':'王三','age':20})

# 读取
with open(file='files/data2.csv',mode='r',encoding='gbk') as f:
    reader=csv.reader(f)
    for row in reader: print(row)

df=pandas.read_csv('files/data2.csv',encoding='gbk')
print(df)

