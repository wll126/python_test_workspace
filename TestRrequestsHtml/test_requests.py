import unittest
import requests
import logging
import re
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




if __name__ == '__main__':
    unittest.main()
