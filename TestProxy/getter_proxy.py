# coding:utf-8

from redis_client import RedisClient
from proxy_crawler import Crawler

POOL_UPPER_THRESHOLD =10000

class Getter():
     def __init__(self):
         self.redis=RedisClient()
         self.crawler=Crawler()

     def is_over_theshold(self):
         """
         判断是否达到了代理池的限制
         :return:
         """
         if self.redis.count() >= POOL_UPPER_THRESHOLD:
             return True
         else:
             return False

     def run(self):
         print("获取器开始执行")
         if not self.is_over_theshold():
             for callback_label in range(self.crawler.__CrawlFuncCount__):
                 callback=self.crawler.__CrawlFunc__[callback_label]
                 proxies=self.crawler.get_proxies(callback)
                 for proxy in proxies:
                     self.redis.add(proxy)



