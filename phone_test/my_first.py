# coding=utf-8   #编码格式
from appium import webdriver  #引入webdriver
from time import sleep  #引入sleep

# 安卓版本
from appium.webdriver.common.touch_action import TouchAction
"""

adb devices  获取device Name
adb shell getprop ro.build.version.release
adb shell getprop ro.build.version.sdk
获取apk相关信息、包名、启动Activity 等等
aapt 
wditor 获取元素属性
pip install weditor   
python -m weditor  启动
"""

platform_version = '4.4.2'
# 设备名称
device_name = '127.0.0.1:62001'
# 包名  com.android.contacts/.activities.PeopleActivity
# 钉钉 'com.alibaba.android.rimet/.biz.SplashActivity'
package_name = 'com.android.contacts'
activity_name = '.activities.PeopleActivity'

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
driver.find_element_by_id('com.android.contacts:id/create_contact_button').click()
sleep(1)
# press
''''
新建:com.android.contacts:id/create_contact_button
登录：com.android.contacts:id/add_account_button
导入联系人:com.android.contacts:id/import_contacts_button
'''
# TouchAction(driver).move_to(x=int(x*0.5), y=int(y*0.5)).press().release().perform()
driver.quit()

# driver.quit()  #退出