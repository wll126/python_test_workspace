import unittest
from urllib.parse import urlencode

import requests
import logging
import re

from pymongo import MongoClient

logging.basicConfig(level=logging.DEBUG)

class TestRequestsCase(unittest.TestCase):
    test_url='http://127.0.0.1:9999/'
    '''
    测试requests的基本用法  
    请求类型：get post head put delete options
    '''
    def test_get(self):
        # 测试get请求
        data={'arg1':'ag1','age':11}
        r=requests.get(self.test_url+'get_info',params=data)
        logging.debug(type(r))
        logging.debug(r.status_code)
        logging.debug(type(r.text))
        logging.debug(r.text)
        logging.debug(r.cookies)

    def test_get_link(self):
        # 测试抓取网页 链接
        '''User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)
         Chrome/76.0.3809.100 Mobile Safari/537.36'''
        headers={ 'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                               '(KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'}
        r=requests.get(self.test_url,headers=headers)
        # print(r)
        text=r.text
        # print(text)
        # '<link rel="stylesheet" type="text/css" href="static_url('style.css')}}">'
        pattern=re.compile('href="([^"]*)">',re.S)
        link=re.findall(pattern,text)
        print(link)

    def test_post(self):
        # 测试pos请求
        data = {'arg1': 'ag1', 'age': 11}
        r = requests.post(self.test_url + 'get_info', data=data)
        exit() if not r.status_code==requests.codes.ok else print('Request successfully')
        logging.debug(type(r))
        logging.debug(r.status_code)
        logging.debug(type(r.headers))
        logging.debug(r.headers)
        logging.debug(r.cookies)
        logging.info(r.url)
        logging.info(r.history)

    def test_ajax(self):
        # 测试ajax请求
        head="""GET /ajax/ HTTP/1.1
                Host: 127.0.0.1:9999
                Connection: keep-alive
                Accept: */*
                X-Requested-With: XMLHttpRequest
                User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36
                Sec-Fetch-Mode: cors
                Sec-Fetch-Site: same-origin
                Referer: http://127.0.0.1:9999/
                Accept-Encoding: gzip, deflate, br
                Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
                Cookie: username=evancss"""
        headers={
            'Host':'127.0.0.1:9999',
            'Referer':'http://127.0.0.1:9999/',
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/76.0.3809.100 Mobile Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        params={'a1':'i1','page':1}
        url=self.test_url+'ajax?'+urlencode(params)
        try:
            response=requests.get(url=url,headers=headers)
            if response.status_code ==200:
                print(response.json())
                self.save_to_mongo(response.json())
        except requests.ConnectionError as e:
            print('Error',e.arg)

    def save_to_mongo(self,result):
        client=MongoClient(host='192.168.133.129', port=27017)
        db=client['test']
        collection=db['test']
        if collection.insert_one(result):
            print("Saved to Mongo")
        results = collection.find()
        for re in results:print(re)



if __name__ == '__main__':
    unittest.main()
