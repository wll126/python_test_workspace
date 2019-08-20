# coding=utf-8

"""
测试真机的功能自动化
"""
import uiautomator2
import time
import schedule


def test_add_note():
    '''  测试写个笔记试试  '''
    # 连接usb设备
    d = uiautomator2.connect_usb()
    print(d.device_info)
    print(d.app_info('com.miui.notes'))
    d.app_stop('com.miui.notes')
    # d.app_clear('com.miui.notes')
    d.app_start('com.miui.notes')
    d(resourceId='com.miui.notes:id/menu_add').click()
    d(resourceId='com.miui.notes:id/rich_editor').send_keys('  今天天气不错，是个晴天！')
    d(resourceId='com.miui.notes:id/done').click()
    d.app_stop('com.miui.notes')


def test_punch_the_clock():
    '''钉钉打卡'''
    # 包名
    package_name = 'com.alibaba.android.rimet'
    # 连接USB设备
    d = uiautomator2.connect('http://0.0.0.0:7912') #.connect_usb()
    # 先关闭当前
    d.app_stop(package_name)
    # 开启钉钉
    d.app_start(package_name)
    # resourceId :com.alibaba.android.rimet:id/home_bottom_tab_icon
    time.sleep(3)
    # 进入企业
    d(resourceId="com.alibaba.android.rimet:id/home_bottom_tab_button_work").click()
    # 考勤打卡
    d.click(0.127, 0.732)
    time.sleep(1)
    # 打卡
    # d.click(0.513, 0.57)
    time.sleep(3)
    # 更新打卡
    d.click(0.153, 0.582)
    # 确定
    d(resourceId="android:id/button1").click()
    # 我知道了
    d.click(0.496, 0.774)
    time.sleep(3)
    # 关闭应用
    d.app_stop(package_name)


schedule.every().day.at('8:00').do(test_punch_the_clock)
schedule.every().day.at('21:00').do(test_punch_the_clock)
while True:
    schedule.run_pending()

