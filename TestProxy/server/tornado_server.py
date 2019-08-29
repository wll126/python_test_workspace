# coding:utf-8

import tornado.ioloop
from tornado.web import RequestHandler, Application

from redis_client import RedisClient

API_PORT=8000

class MainHandler(RequestHandler):
    def initialize(self,redis):
        self.redis=redis

    def get(self,api=''):
        if not api:
            links=['random','proxies','names','all','count']
            for link in links:
                self.write('<a href='+link+'>'+link+'</a><br>')

        if api=='random':
            result=self.redis.random()
            if result:
                self.write(result)


def server(redis,port=API_PORT,address=''):
    application=Application([(r'/',MainHandler,dict(redis=redis)),(r'/(.*)',MainHandler,dict(redis=redis))])
    application.listen(port,address)
    print('API listening on ',port)
    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    server(redis=RedisClient())