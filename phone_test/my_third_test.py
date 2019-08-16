# coding:utf8

import uiautomator2
from time import sleep
"""
测试app  百度翻译功能
"""
app_package_name='com.baidu.baidutranslate'


def test_translate():
    d=uiautomator2.connect_usb()    # 使用uiautomator2框架
    print(d.device_info)
    print(d.app_info(app_package_name))
    d.app_stop(app_package_name)    # 测试前先将程序停止，保证测试可重复性
    # 启动百度翻译
    d.app_start(app_package_name)
    sleep(3)
    # 逐级点击，进入翻译主界面
    # id com.baidu.baidutranslate:id/trans_content_input
    d(resourceId='com.baidu.baidutranslate:id/trans_content_input').send_keys('今天天气不错')
    # id com.baidu.baidutranslate:id/translate_layout_translate_btn 翻译按钮
    d(resourceId='com.baidu.baidutranslate:id/translate_layout_translate_btn').click()
    sleep(5)
    d.app_stop(app_package_name)


if __name__=="__main__":
    test_translate()



