# coding:utf-8
import requests

TIMEOUT=10
from requests import Request
PROXY_POOL_URL='http://127.0.0.1:5000/random'

class WeixinRequest(Request):
    def __init__(self,url,callback,method='GET',headers=None,need_proxy=False,fail_time=0,timeout=TIMEOUT):
        Request.__init__(self,method,url,headers)
        self.callback=callback
        self.need_proxy=need_proxy
        self.fail_time=fail_time
        self.timeout=timeout

    def get_proxy(self):
        """
        从代理池获取代理
        :return:
        """
        try:
            response=requests.get(PROXY_POOL_URL)
            if response.status_code==200:
                print('Get Proxy',response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None
        