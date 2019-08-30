# coding:utf-8

"""
Cookies池的存储模块，使用redis hash 存储cookie信息，key 为账号，cookie为value
"""

import random
import redis

REDIS_HOST='localhost'
REDIS_PORT=6379
REDIS_PASSWORD=None



class RedisClient(object):
    def __init__(self, type, website, host=REDIS_HOST, port=REDIS_PORT,password=REDIS_PASSWORD):
        """
        初始化 Redis 连接
        :param type:
        :param website:
        :param host:
        :param port:
        :param password:
        """
        self.db=redis.StrictRedis(host=host,port=port, password=password,decode_responses=True)
        self.type=type
        self.website=website

    def name(self):
        """
        获取hash的名称
        :return:
        """
        return "{type}:{website}".format(type=self.type,website=self.website)

    def set(self,username,value):
        """
        设置键值对
        :param username:   用户名
        :param value: 密码或者cookies
        :return:
        """
        return self.db.hset(self.name(),username,value)

    def get(self,username):
        """
        根据键名获取键值
        :param username:
        :return:
        """
        return self.db.hget(self.name(),username)

    def delete(self,username):
        """
        根据键名删除键值对
        :param username: 用户名
        :return:
        """
        return self.db.hdel(self.name(),username)

    def count(self):
        """
        获取数目
        :return:
        """
        return self.db.hlen(self.name())

    def random(self):
        """
        随机得到键值，用于随机Cookies 获取
        :return:
        """
        return random.choice(self.db.hvals(self.name()))

    def usernames(self):
        """
        获取所有账户信息
        :return: 所有用户名
        """
        return self.db.hkeys(self.name())

    def all(self):
        """
        获取所有键值对
        :return:
        """
        return self.db.hgetall(self.name())
    
