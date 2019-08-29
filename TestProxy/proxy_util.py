# coding:utf-8

"""代理的使用"""
import zipfile
from urllib import request
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
import socket
from selenium import webdriver
import requests
import socks

# HTTP代理服务
# 1 认证代理
from selenium.webdriver.chrome.options import Options

proxy = 'username:password@127.0.0.1:9743'
proxy = '127.0.0.1:9743'
proxy_handler = ProxyHandler({'http': 'http://' + proxy, 'https': 'https://' + proxy})
test_url='http://127.0.0.1:9999/'
def http_proxy():
    """
    http代理类型
    :return:
    """
    opener=build_opener(proxy_handler)
    try:
        response=opener.open(test_url)
        print(response.read().decode('utf-8'))
        # requests 实现
        response=requests.get(test_url,proxies=proxy_handler)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print(e.args)
    except URLError as e:
        print(e.reason)


def socket_proxy():
        """
        socks5 代理类型
        :return:
        """
        socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',9742)
        socket.socket=socks.socksocket
        try:
            response=request.urlopen('http://httpbin.org/get')
            print(response.read().decode('utf-8'))
        except URLError as e:
            print(e.reason)

def selenium_proxy():
    """
    selenium 设置代理
    :return:
    """

    proxy='127.0.0.1:9743'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://'+proxy)
    browser=webdriver.Chrome(chrome_options=chrome_options)
    browser.get(test_url)

def chrome_proxy():
    # 认证代理
    ip='127.0.0.1'
    port=9743
    username='foo'
    password='paswd'
    manifest_json="""
    {
        "version":"1.0.0",
        "manifest_version":2,
        "name":"Chrome Proxy",
        "permissions":[
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background":{
            "scripts":["background.js"]
        }
    }
    """

    background_js="""
    var config={
        mode:"fixed_servers",
        rules:{
            singleProxy:{
                scheme:"http",
                host:"%(ip)s",
                port:%(port)s
            }
        }
    }
    
    chrome.proxy.settings.set({value:config,scope:"regular"},function(){});
    function callbackFn(details){
        return {
            authCredentials:{
                username:"%(username)s",
                password:"%(password)s"
            }
        }
    }
    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {urls:["<all_urls>"] }
        ['blocking']
    )
    """ %{'ip':ip,'port':port,'username':username,'password':password}

    plugin_file='proxy_auth_plugin.zip'
    with zipfile.ZipFile(plugin_file,'w') as zp:
        zp.writestr("manifest.json",manifest_json)
        zp.writestr("background.js",background_js)
    chrome_options=Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_extension(plugin_file)
    browser=webdriver.Chrome(chrome_options=chrome_options)
    browser.get(test_url)


def test_phantomjs():
    # 测试PhantomJS 代理
    service_arg=[
        '--proxy=127.0.0.1:9743',
        '--proxy-type=http',
        '--proxy-auth=username:password'
    ]
    broser=webdriver.PhantomJS(service_args=service_arg)
    broser.get(test_url)
    print(broser.page_source)

test_phantomjs()





