# coding=utf-8   #编码格式
from appium import webdriver  #引入webdriver
from time import sleep  #引入sleep

# 安卓版本
from appium.webdriver.common.touch_action import TouchAction

platform_version = '4.4.2'
# 设备名称
device_name = '127.0.0.1:62001'
# 包名
# 钉钉 'com.alibaba.android.rimet/.biz.SplashActivity'
package_name = 'com.youdao.calculator'
activity_name = '.activities.MainActivity'

# 定义初始化的属性信息
desired_caps = {'platformName': 'Android', 'platformVersion': platform_version, 'deviceName':device_name ,
                'appPackage': package_name, 'appActivity': activity_name, 'unicodeKeyboard': True, 'noReset': True,
                'resetKeyboard': True}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps, keep_alive=True)  #启动服务器地址，后面跟的是手机信息
t = 1000
# 获取手机屏幕尺寸 720*1280
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
x1 = int(x*0.75)
y1 = int(y*0.5)
x2 = int(x*0.05)
for i in range(3):
    driver.swipe(x1, y1, x2, y1, t)
    sleep(1)
driver.find_element_by_id('com.youdao.calculator:id/guide_button').click()
sleep(1)
# press

TouchAction(driver).move_to(x=int(x*0.5), y=int(y*0.5)).press().release().perform()
driver.quit()

# driver.quit()  #退出