import socket
import unittest
import urllib
import urllib.request as req
import urllib.parse
import urllib.error
import logging
logging.basicConfig(level=logging.DEBUG)

# 测试网址
test_url='http://127.0.0.1:9999/'

class MyTestCase(unittest.TestCase):
    """
    测试请求http  页面并解析的过程
    author :wll  20190819
    """
    def test_urllib(self):
        response=req.urlopen('http://127.0.0.1:9999/')
        # print(response.read().decode('utf-8'))
        # print(type(response))
        # logging.info(dir(response))
        logging.info("status:%d" % response.status)
        logging.info(response.getheaders())
        logging.info(response.getheader('Server'))

    def test_post(self):
        # post data
        try:
            data=bytes(urllib.parse.urlencode({'username':'name','password':'123'}), encoding='utf8')
            response=urllib.request.urlopen('http://127.0.0.1:9999/login',data=data,timeout=0.001)
            logging.info(response.read())
        except urllib.error.URLError as e:
            if isinstance(e.reason,socket.timeout):
                logging.info("TIME OUT ")
        except Exception as e2:
            logging.error(e2)

    def test_proxy(self):
        # 测试使用代理
        from urllib.error import URLError
        from urllib.request import ProxyHandler,build_opener
        proxy_handler=ProxyHandler({'http':'http://127.0.0.1:9743','https':'https://127.0.0.1:9743'})
        opener=build_opener(proxy_handler)
        try:
            response=opener.open('http://127.0.0.1:9999/')
            print(response.read().decode('utf-8'))
        except URLError as e:
            logging.error(e.reason)

    def test_cookie(self):
        # 测试cookie的处理
        import http.cookiejar,urllib.request
        # cookie=http.cookiejar.CookieJar()
        cookieFileName='cookies.txt'
        # cookie=http.cookiejar.MozillaCookieJar(filename=cookieFileName)    #  处理cookie和文件相关的事件
        cookie=http.cookiejar.LWPCookieJar(filename=cookieFileName)     # 生成LWP格式的cookie
        # cookie=http.cookiejar.LWPCookieJar()
        # cookie.load(cookieFileName,ignore_expires=True,ignore_discard=True)         # 加载cookie文件
        handler=urllib.request.HTTPCookieProcessor(cookie)
        opener=urllib.request.build_opener(handler)
        response=opener.open('http://127.0.0.1:9999/set_cookie')
        cookie.save(ignore_discard=True, ignore_expires=True)
        for item in cookie:
            print(item.name+"="+item.value)
        print(response.read().decode('utf-8'))

    def test_error(self):
        # 测试处理异常
        from urllib import request,error
        try:
            response=request.urlopen('http://127.0.0.1:9999/123')
        except error.HTTPError as e:
            logging.error(e)
            print(e.reason,e.code,e.headers,sep='\n')
        except error.URLError as e:
            print(e.reason)
            if isinstance(e.reason,socket.timeout):
                print('Time Out!')
        else:
            print("request successfully!")

    def test_urlparse(self):
        # 测试解析url
        from urllib.parse import urlparse,urlsplit,urljoin,urlencode,quote
        result=urlparse(test_url+'login?username=us&password=123')
        print(type(result),result)
        result = urlsplit(test_url + 'login;user?username=us&password=123')
        print(type(result), result)
        from urllib.parse import urlunparse,urlunsplit,parse_qs,parse_qsl,unquote
        # 反解析
        data=('http','127.0.0.1','index.html','','a=6','comment')
        print(urlunparse(data))
        data = ('http', '127.0.0.1', 'index.html', 'a=6', 'comment')
        print(urlunsplit(data))
        print(urljoin('http://www.baidu.com', 'facu.html'))
        # urlencode   {}-> param
        params={'name':'wk','age':22}
        bas_url='http://wwww.ceshi.com?'
        url=bas_url+urlencode(params)
        print(url)
        query=urlsplit(url).query
        print(parse_qs(query))
        print(parse_qsl(query))
        #  转码中文
        keyword='用户名'
        quote_result=quote(keyword)
        print("%s转码结果:%s" %(keyword,quote_result))
        # 反解码
        print("反转结果:",unquote(quote_result))

    def test_robot(self):
        # 测试robots
        from urllib.robotparser import  RobotFileParser
        rp=RobotFileParser()
        rp.set_url(test_url+'robots.txt')
        rp.read()
        print(rp.can_fetch('*',test_url))











if __name__ == '__main__':
    unittest.main()
