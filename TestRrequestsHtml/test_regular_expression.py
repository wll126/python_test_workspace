import unittest
import re

class TestRegexCase(unittest.TestCase):
    """
    正则表达式测试
    """
    content='Hello 123 4567 Www thi is a regex demo!'

    def test_match(self):
        # 测试match匹配方法 默认贪婪匹配
        print(len(self.content))
        result=re.match('Hello.*(\d+).*demo',self.content)
        print(result)
        print(result.group())
        print(result.group(1))
        print(result.span())
        # 非贪婪匹配 ?
        result = re.match('Hello.*?(\d+).*demo', self.content)
        print(result)
        print(result.group())
        print(result.group(1))
        print(result.span())

    def test_modifier(self):
        # 测试修饰符作用
        # re.S 匹配换行符
        """
        re.I    忽略大小写
        re.L    做本地化识别
        re.M    多行匹配
        re.S    使.匹配包括换行在内的所有字符
        re.U    根据Unicode字符集解析字符
        re.X    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
        :return:
        """
        content='''Hello  123 456
        world is regex demo'''
        result=re.match('Hello.*?(\d+).*demo',content,re.S)
        print(result.group())

    def test_search(self):
        # 测试匹配搜索,只返回第一个匹配结果
        content='Ent  is ma Hello 123 567 old world is demo'
        result=re.search('Hello.*?(\d+).*demo',content)
        print(result)
        print(result.group(1))

    def test_findall(self):
        # 测试匹配整个字符串 返回list类型
        content = 'Ent  is ma Hello 123 567 old world is demo'
        result=re.findall('(\d+)',content)
        print(result)

    def test_sub(self):
        # 测试正则匹配替换方法
        content=self.content
        content=re.sub('\d+','I',content)
        print(content)

    def test_compile(self):
        # 将字符串编译成正则表达式的方法
        content1='2019-12-15 12:00'
        content2='2019-12-13 13:00'
        content3='2010-11-11 14:20'
        pattern=re.compile('\d{2}:\d{2}',re.S)
        r1=re.sub(pattern,'',content1)
        r2=re.sub(pattern,'',content2)
        r3=re.sub(pattern,'',content3)
        print(r1,r2,r3)


if __name__ == '__main__':
    unittest.main()
