# coding:utf-8

from pickle import dumps,loads
from redis import StrictRedis

from request.weixin_request import WeixinRequest

REDIS_HOST='127.0.0.1'
REDIS_PORT=6379
REDIS_PASSWORD=None
REDIS_KEY='weixin'


class RedisQueue():
    def __init__(self):
        """
        初始化 Redis
        """
        self.db=StrictRedis(host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD)

    def add(self,request):
        """
        向队列添加序列化后的REQUEST
        :param request:
        :return:
        """
        if isinstance(request,WeixinRequest):
            return self.db.rpush(REDIS_KEY,dumps(request))
        return False

    def pop(self):
        """
        取出下一个Request 反序列化
        :return:
        """
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def empty(self):
        return self.db.llen(REDIS_KEY) ==0
