# coding:utf-8

"""
调度模块
"""
import time

from async_test import Tester
from getter_proxy import Getter
from proxy_interface import app

TESTER_CYLE=20
GETTER_CYLE=20
TESTER_ENABLED=True
GETTER_ENABLED=True
API_ENABLED=True
API_HOST='127.0.0.1'
API_PORT='5000'

from multiprocessing import Process

class Scheduler():
    def schedule_tester(self,cycle=TESTER_CYLE):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester=Tester()
        while True:
            print('测试器开始执行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self,cyle=GETTER_CYLE):
        """
        定时获取代理
        :param cyle:
        :return:
        """
        getter=Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cyle)

    def schedule_api(self):
        """
        开启API
        :return:
        """
        app.run(API_HOST,API_PORT)

    def run(self):
        """
        多进程运行
        :return:
        """
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process=Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process=Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process=Process(target=self.schedule_api)
            api_process.start()


if __name__=="__main__":
    Scheduler().run()