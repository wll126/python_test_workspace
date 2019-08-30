# coding:utf-8

from requests import Session
from urllib.parse import urlencode

from queue.redis_queue import RedisQueue
from request.weixin_request import WeixinRequest


class Spider():
    base_url='http://weixin.sogou.com/weixin'
    keyword='MC'
    headers={
        'Host':'weixin.sogou.com'
    }
    session=Session()
    queue=RedisQueue()

    def start(self):
        """
        初始化工作
        :return:
        """
        # 全局更新headers
        self.session.headers.update(self.headers)
        start_url=self.base_url+'?'+urlencode({'query':self.keyword,'type':2})
        weixin_request=WeixinRequest(url=start_url,callback=self.parse_index,need_proxy=True)
        self.queue.add(weixin_request)