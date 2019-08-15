# !/usr/bin/python
# coding:utf8

from pymongo import MongoClient

host,port = "192.168.133.129", 27017
# 创建mongodb 连接
conn=MongoClient(host=host,port=port)
db=conn.mydb   # 连接mydb数据库，如果没有则创建
my_set=db.my_set  # 使用my_set集合，没有则创建
my_set.insert_one({"name":"zhangsan","age":18})
# my_set.save({"name":"lisi","age":19})
# 插入多条数据
users=[{"name":"wangwu","age":16},{"name":"zhaoer","age":11}]
my_set.insert_many(users)
# my_set.save(users)

# 查询所有数据
for i in my_set.find():
    print(i)

# 条件查询
for i in my_set.find({"name":"zhansan"}):
    print(i)
# 查询一条
print(my_set.find_one({"name":"zhansan"}))

#更新数据
my_set.update({"name":"zhansan"},{'$set':{"age":20}})

#删除数据
my_set.remove({"name":"lisi"})
id=my_set.find_one({"name":"zhansan"})["_id"]
my_set.remove(id)

#  删除集合所有记录
# db.users.remove()






