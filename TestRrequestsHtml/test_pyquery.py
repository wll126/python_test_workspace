# coding:utf8

import unittest
from pyquery import PyQuery as pq


class TestPq(unittest.TestCase):
    """
    测试pyquery
    """
    html = '''
    <div id="app">
        <nav class="navbar navbar-default" style="margin-bottom: 0px">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
              data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">ATX <strong>WEditor</strong></a>
          </div>
          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <--         <ul class="nav navbar-nav">
              <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
            </ul> -->
            <form class="navbar-form navbar-left" onsubmit="return false">
              <div class="form-group">
                <select v-model="platform" class="selectpicker" value="Android" title="Platform" data-width="fit">
                  <option data-icon="glyphicon-piggy-bank" value="Android">Android</option>
                  <option data-icon="glyphicon-apple" value="iOS">iOS</option>
                  <option data-icon="glyphicon-apple" value="Neco">Neco(beta)</option>
                </select>
                <input type="text" v-model="serial" class="form-control" placeholder="deviceUrl">
              </div>
              <button type="submit" class="btn btn-default" click="doConnect">
                Connect
                <span v-if="deviceId" class="glyphicon glyphicon-grain color-green"></span>
              </button>
              <button :disabled="loading" class="btn btn-default" click="dumpHierarchyWithScreen()">
                <i class="fa fa-refresh"></i> Dump Hierarchy
              </button>
              <template v-if="platform == 'Android'">
                <el-switch v-model="liveScreen" active-text="实时" inactive-text="静态">
                </el-switch>
              </template>
            </form>
            <ul class="nav navbar-nav navbar-right">
              <-- <li><a href="#">Link</a></li> -->
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">相关文档 <span class="caret"></span></a>
                <ul class="dropdown-menu">
                  <li><a target="_blank" href="https://github.com/openatx/weditor">openatx/weditor</a></li>
                  <li role="separator" class="divider"></li>
                  <li><a target="_blank" href="https://github.com/openatx/uiautomator2">openatx/uiautomator2</a></li>
                  <li><a target="_blank" href="https://github.com/openatx/facebook-wda">openatx/facebook-wda</a></li>
                </ul>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    '''
    def setUp(self):
        self.doc=pq(self.html)

    def ttest_css(self):
        print('*'*20)
        # 测试CSS选择器
        # doc = pq(self.html)
        print('---------------------------')
        ap=self.doc('#app')
        print(self.doc('#app'))

    def ttest_find(self):
        # 测试查找子节点的方法
        items=self.doc('ul')
        lis=items.find('a') # 子孙节点
        lis=items.children('a') # 一级子节点
        # 查找父节点
        lis=items.parent()      # 直接父节点
        lis=items.parents()     # 所有父节点
        # 兄弟节点
        lis=items.siblings()    # 所有兄弟节点
        # 多节点遍历
        # for li in lis.items():
        #     print(type(li),li)
        # 获取属性 attr()
        a=self.doc('a')
        # 捕获文本 text()  html()
        for item in a.items():
            print(item.html())
            print(item.attr('href'))
            print(item.text())
        # print(type(lis), lis)

    def ttest_change_node(self):
        # 改变节点属性
        # addClass   removeClass
        item=self.doc('.divider')
        print(item)
        item.remove_class('divider')
        print(item)
        item.add_class('divider')
        print(item)

        #  attr() text() html()
        item.attr('role','change')
        print(item)
        item.text('change item')
        print(item)
        item.html('<span>add span</span>')
        print(item)
        # 移除  remove
        item.find('span').remove()
        print(item)

    def test_css_index(self):
        # 测试伪类选择器
        # first-child 第一个节点
        li=self.doc('li:first-child')
        # last-child 最后一个节点
        li=self.doc('li:last-child')
        # 第二个节点
        li=self.doc('li:nth-child(2)')
        # 大于2的节点
        li=self.doc('li:gt(2)')
        # 偶数位置节点 nth-child(2n)
        li=self.doc('li:nth-child(2n)')
        # 包含某文本的节点 contains()
        li=self.doc('li:contains(weditor)')
        print(li)






if __name__=="__main__":
    unittest.main()