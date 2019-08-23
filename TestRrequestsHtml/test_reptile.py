# coding:utf-8
import json
import re
import requests
import unittest
from lxml import etree

class TryReptileTestcase(unittest.TestCase):
    test_url='http://127.0.0.1:9999/'

    def get_index(self,url):
        # 根据给定url，获取返回页面信息
        headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'}
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None

    def parse_html(self,html):
        # 解析html，提取想要的信息，存入字典中
        pattern=re.compile('<li><a.*?href="(.*?)">(.*?)</a>',re.S)
        items=re.findall(pattern,html)
        for item in items:
            yield {'url':item[0],'title':item[1]}

    def write_to_file(self,content):
        # 将结果写入文件保存
        with open('result.txt','a',encoding='utf-8') as f:
            # print(type(json.dumps(content)))
            f.write(json.dumps(content,ensure_ascii=False)+'\n')

    def test_script(self):
        #  测试抓取
        url=self.test_url
        html=self.get_index(url=url)
        # print(html)
        # self.parse_html(html)
        for item in self.parse_html(html):
            self.write_to_file(item)

    def test_entree(self):
        text='''
         <div class="panel-body">
            <div class="text-center">
              <button class="btn btn-default btn-sm" disabled="nodeSelected" v-on:click="doTap()">Tap</button>
              <button name="mid" class="btn btn-default btn-sm" v-on:click="doSendKeys('')">Send Keys</button>
              <button class="btn btn-default btn-sm" v-on:click="doClear()">Clear Text</button> 
              <li>
            </div>
          </div>
        '''
        html=etree.HTML(text)
        # result=etree.parse('./test.html',etree.HTMLParser())      # 解析html 文件
        # result=etree.tostring(html)
        # print(result.decode('utf-8'))
        result=html.xpath('//div/button')       #  /子节点    // 子孙节点
        print(result)
        result=html.xpath('//button/..')    # 上级节点   parent:: 父节点
        print(result)
        result=html.xpath('//button[@disabled="nodeSelected"]')    # 属性节点
        print(result)
        # 获取text
        result=html.xpath('//button/text()')
        print(result)
        # 获取属性
        result=html.xpath('//button/@class')
        print(result)
        # 包含模糊匹配  contains(属性名,属性值) and
        result=html.xpath('//button[contains(@class,btn-sm) and @name="mid"]//text()')
        print(result)

        # 选择第几个
        result=html.xpath('//button[1]/text()')     # 第一个
        print(result)
        result=html.xpath('//button[last()]//text()')   # 最后一个
        print(result)
        result=html.xpath('//button[position()<3]/text()')  # 1和2节点
        print(result)
        result=html.xpath('//button[last()-2]/text()')  # 最后一个减2 位，也就是倒数第三个节点
        print(result)

    def test_get_elements(self):
        # 测试节点轴选择方法
        # 包括子、兄弟、父、祖先等元素
        html=etree.parse('test.html',etree.HTMLParser())
        print(html)
        result=html.xpath('//span')
        print(result)



