# coding:utf-8

from redis import StrictRedis,ConnectionPool
# ip:192.168.133.129
redis=StrictRedis(host='192.168.133.129',port=6379, db=0,)
# redis.set('name','Co')
uri='redis://@192.168.133.129:6379/0'
pool=ConnectionPool.from_url(uri)
redis=StrictRedis(connection_pool=pool)
print(redis.get('name'))
print(redis.keys())

def key_fun():
    """
    键操作
    :return:
    """
    # 判断键是否存在
    redis.exists('name')
    # 删除一个键
    redis.delete('name')
    # 判断键类型
    redis.type('name')
    # 查询键
    redis.keys('n*')
    # 获取随机一个键
    redis.randomkey()
    # 重命名键
    redis.rename('name','nickname')
    # 获取当前数据库中键的数目
    redis.dbsize()
    # 设定键的过期时间,单位秒
    redis.expire('name',2)
    # 获取键的过期时间，-1表示永不过期
    redis.ttl('name')
    # 将键移动到其他数据库
    redis.move('name',2)
    # 删除当前选择数据库中所有键
    redis.flushdb()
    # 删除所有数据库中所有键
    redis.flushall()

def str_fun():
    # 字符串操作
    # 赋值操作
    redis.set('name','名字')
    # 取值
    redis.get('name')
    # 赋值并返回上次value
    redis.getset('name','新名字')
    # 返回多个键对应的value
    redis.mget(['name','nickname'])
    # 不存在则更新
    redis.setnx('name','James')
    # 设定值，并指定有效期
    redis.setex('name',1,'value')
    # 设定指定键的子字符串， 补字符串
    redis.setrange('name',6,'world')
    # 批量赋值
    redis.mset({'name1':'名1','name2':'名2'})
    # 键不存在时才赋值
    redis.msetnx({'n2':'a2','n3':'a3'})
    # 键名的值进行增值操作，默认增1，键不存在，则创建，赋值为-amount
    redis.incr('age',amount=1)  # 年龄加1岁
    # 键名的值进行减值操作，默认减1，键不存在，则创建，赋值为-amount
    redis.decr('age',amount=1) # 减一岁
    # 给指定的键的值添加字符串
    redis.append('name',value='apend string')
    # 返回键名对应string的子字符串
    redis.substr('name',start=1,end=-1)
    # 同上
    redis.getrange('name',start=0,end=-1)

def list_fun():
    # 列表操作
    r=redis
    # 向列表末尾添加元素
    r.rpush('list',1,2,3)
    # 在列表头添加元素
    r.lpush('list',0,1)
    # 返回列表长度
    r.llen('list')
    # 返回列表start 至end之间的元素
    r.lrange('list',start=1,end=3)
    # 保留列表start至end之间的内容
    r.ltrim('list',1,3)
    # 返回指定索引位置的元素
    r.lindex('list',index=2)
    # 给指定位置赋值
    r.lset('list',index=1,value='vvv')
    # 删除指定个数个值
    r.lrem('list',count=2,value=2)
    # 删除并返回列表首个元素
    r.lpop(name='list')
    # 删除并返回列表尾元素
    r.rpop(name='list')
    # 返回并删除列表中的首个元素
    r.blpop(keys='list',timeout=0)
    # 返回并删除列表中尾元素，如果列表为空，则等带超时时间
    r.brpop(keys='list',timeout=0)
    # 删除列表的尾元素，并将该元素添加到另一个列表
    r.rpoplpush(src='list',dst='list2')

def set_fun():
    """
    集合操作，集合中元素不重复
    :return:
    """
    r=redis
    name='tags'
    # 向集合添加元素
    r.sadd(name, 'v1','v2','v3')
    # 删除元素
    r.srem(name,'v2')
    # 随机删除并返回一个
    r.spop(name)
    # 移动元素从src到dst
    r.smove(src='tags',dst='tags2',value='v1')
    # 返回集合个数
    r.scard(name)
    # 判断是否是集合成员
    r.sismember(name=name,value='Book')
    # 返回给定集合的交集
    r.sinter(['tags1','tags2'])
    # 求交集并保存到dest
    r.sinterstore('inttag',['tags','tags2'])
    # 求并集
    r.sunion(['tags','tags2'])
    # 求并集并保存
    r.sunionstore('inttag',['tags','tags2'])
    # 求差集
    r.sdiff(['tags','tags2'])
    # 求差集并存储
    r.sdiffstore('inttag',['tags','tags2'])
    # 返回集合的所有元素
    r.smembers(name)
    # 随机返回一个元素，不删除
    r.srandmember(name)

def ordered_set():
    """
    有序集合比集合多了一个分数字段
    :return:
    """
    r=redis
    name='grade'
    # 向有序集合添加元素，score用于排序
    r.zadd(name,100,'B0',98,'Mk')
    # 删除
    r.zrem(name,'Mk')
    # 判断元素是否存在，存在，更新score值，不存在，则添加
    r.zincrby(name=name,value='B0',amount=-2)  # B0 score-2
    # 返回给定值所排名次
    r.zrank(name,value='B0')
    # 返回给定值的倒数名次
    r.zrevrank(name=name,value='Mk')
    # 返回倒叙排序，排名在start至end之间的元素
    r.zrevrange(name,start=1,end=2)
    # 返回分数在给定区间的元素
    r.zrangebyscore(name=name,min=80,max=95)
    # 返回分数在给定区间的数量
    r.zcount(name,min=50,max=60)
    # 返回给定名字的元素个数
    r.zcard(name)
    # 删除排名在给定区间的元素
    r.zremrangebyrank(name,min=10,max=20)
    # 删除分数在给定区间的元素
    r.zremrangebyscore(name,min=10,max=20)

def map_fun():
    """
    散列表  键值对
    :return:
    """
    r=redis
    name='price'
    # 添加映射
    r.hset(name=name,key='cake',value=5.5)
    # 如果不存在，则添加
    r.hsetnx(name=name,key='book',value=6)
    # 返回给定键的值
    r.hget(name=name,key='book')
    # 返回多个键对应的值
    r.hmget(name=name,keys=['cake','book'])
    # 批量添加映射
    r.hmset(name=name,mapping={'banana':2,'pear':6})
    # 增加散列值
    r.hincrby(name,'cake',amount=3)
    # 判断键名是否存在
    r.hexists(name,key='apple')
    # 删除映射
    r.hdel(name,"banana")
    # 获取映射个数
    r.hlen(name)
    # 获取所有键名
    r.hkeys(name)
    # 获取所有值
    r.hvals(name)
    # 获取所有键值对
    r.hgetall(name)
