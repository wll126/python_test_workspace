#!/usr/bin/python3
# -*- coding:utf-8 -*-

from locust import HttpLocust,TaskSet,task

"""
一个简单的压力测试
"""


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("login",{"username":"test","password":"123456"})

    @task(2)
    def index(self):
        self.client.get("user/10")

    @task(1)
    def about(self):
        self.client.get('user/9')

    @task(3)
    def second(self):
        self.client.get("user/11")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "127.0.0.1"
    min_wait = 1000
    max_wait = 5000


if __name__ == "__main__":
     import os
     os.system("locust -f test_locust.py --host=http://127.0.0.1:5000/")
