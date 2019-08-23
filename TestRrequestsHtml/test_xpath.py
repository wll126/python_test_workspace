from lxml import etree

def test_get_parents():
    # 测试节点轴选择方法
    # 包括子、兄弟、父、祖先等元素
    html = etree.parse('test.html', etree.HTMLParser())
    print(html)
    result = html.xpath('//span')
    print(result)
    # 获取所有祖先节点 ancestor::
    result=html.xpath('//el-tooltip/ancestor::*')
    print('祖先节点',result)
    # 获取属性值 attribute::*
    result=html.xpath('//el-tooltip/attribute::*')
    print("属性值:",result)
    # 获取所有子节点 child::
    result=html.xpath('//span/child::*')
    print("子节点",result)
    # 获取所有子孙节点 descendant::
    print(html.xpath('//div/descendant::*'))
    # 获取当前节点之后的所有节点 following::
    print(html.xpath('//span/following::*'))
    # 获取当前节点之后的所有同级节点 following-sibling::
    print(html.xpath('//span/following-sibling::*'))




test_get_parents()