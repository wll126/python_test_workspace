# coding:utf-8

"""
关系型数据库 SQLite Mysql Oracle SQL Server DB2

"""
import pymysql
db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor=db.cursor()

def create_db():
    # 建库
    cursor.execute('SELECT VERSION()')
    data=cursor.fetchone()
    print('database version:',data)
    cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')

def create_table():
    # 建表
    sql='CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))'
    cursor.execute(sql)

def insert_data():
    id,user,age='20001','张三',20
    # 添加数据
    sql='INSERT INTO students(id,name,age) values(%s,%s,%s)'
    try:
        cursor.execute(sql,(id,user,age))
        db.commit()
    except:
        db.rollback()

def insert_or_update(data={'k':'v'}):
    # 查询数据主键是否存在，存在则更新，不存在，则插入数据
    tables='students'
    keys=','.join(data.keys())
    values=','.join(['%s']*len(data))



# create_table()
insert_data()
db.close()
