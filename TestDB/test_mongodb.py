#coding:utf-8

import pymongo

"""
操作符说明：
$lt 小于 
$gt 大于
$lte 小于等于
$gte 大于等于
$ne 不等于
$in 在范围内
$nin 不在范围内
$regex 匹配正则表达式
$exists 属性是否存在
$type 类型判断
$mod 数字模式操作 {'age':{'$mod':[5,0]}}
$text 文本查询 {'text':{'$search':'Mike'}}
$where 高级条件查询 {'where':{'obj.fans_count==obj.follows_count'}}  
"""
# 连接数据库
client=pymongo.MongoClient(host='192.168.133.129', port=27017)
#  uri = "mongodb://%s:%s@%s"

# 指定数据库
db=client.test
# 指定集合
collection=db.students

def test_insert():
    # 插入数据
    student={'id':'20170104','name':'K','age':21,'gender':'male'}
    result=collection.insert_one(student)
    print(result)
    print(result.inserted_id)

def test_select():
    # 查询数据
    result=collection.find_one({'age':20})
    print(type(result))
    print(result)
    # 查询多条
    results=collection.find({'age':20})
    for re in results:
        print(re)
    # 查询大于20岁
    result=collection.find({'age':{'$gt':20}})
    print([re for re in result])
    # 查询以M开头的
    results=collection.find({'name':{'$regex':'^M.*'}})
    print([re for re in results])
    # 查询数据条数
    count=collection.find().count()
    print(count)
    # 排序
    results=collection.find().sort('name',pymongo.ASCENDING)
    print([r['name'] for r in results])
    # 偏移
    results=collection.find().sort('name',pymongo.DESCENDING).skip(2)
    print([r['name'] for r in results])
    # limit
    results = collection.find().sort('name', pymongo.DESCENDING).skip(2).limit(2)
    print([r['name'] for r in results])

def test_update():
    # 更新数据操作
    condition={'name':'Mike'}
    student=collection.find_one(condition)
    student['age']=25
    result=collection.update(condition,student)
    print(result)
    result=collection.update_many(condition,{'$inc':{'age':1}})
    print(result)
    print(result.matched_count,result.modified_count)

def test_remove():
    # 删除操作
    result=collection.remove({'name':'Kevin'})
    print(result)
    result=collection.delete_one({'name':'K'})
    print(result)
    print(result.deleted_count)

test_insert()
# test_select()
# test_update()
test_remove()
