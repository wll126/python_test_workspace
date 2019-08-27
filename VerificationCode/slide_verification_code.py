# coding:utf-8
import time
from io import BytesIO

from PIL import Image
from appium.webdriver import WebElement
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
EMAIL='test@test.com'
PASSWORD='123456'


class CreackGeetest():
    """
    测试滑动验证码
    """
    def __init__(self):
        self.url='https://www.geetest.com/Register'
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,20)
        self.emal=EMAIL
        self.password=PASSWORD

    def go_register_page(self):
        """
        注册页面，存在滑动验证码
        :return:
        """
        self.browser.get(self.url)
        time.sleep(3)
        # placeholder="手机号码"
        # 滚动条往下滚动 js
        js='document.documentElement.scrollTop=1000'
        self.browser.execute_script(js)
        # input_phone=WebElement(self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[placeholder="手机号码"]'))))
        input_phone=self.browser.find_element_by_css_selector('input[placeholder="手机号码"]')
        input_phone.send_keys('123456789')
        self.browser.find_element_by_class_name('sendCode').click()
        time.sleep(3)

    def get_geetest_button(self):
        """
        获取初始验证按钮，返回按钮对象
        :return:
        """
        button=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    def get_screenshot(self):
        """
        获取网页截图
        :return:
        """
        screenshot=self.browser.get_screenshot_as_png()
        screenshot=Image.open(BytesIO(screenshot))
        return screenshot

    def get_position(self):
        """
        获取验证码位置
        :return:
        """
        img=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
        time.sleep(2)
        location=img.location
        size=img.size
        top,bottom,left,right=location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_geetest_image(self,name='captcha.png'):
        """
        获取验证码图片
        :param name:
        :return:
        """
        top,bottom,left,right=self.get_position()
        print('验证码位置',top,bottom,left,right)
        screenshot=self.get_screenshot()
        captcha=screenshot.crop((left,top,right,bottom))
        return captcha

    def get_slider(self):
        """
        获取滑块
        :return:
        """
        slider=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_slider_button')))
        return slider

    def is_pixel_equal(self,image1,image2,x,y):
        """
        判断两个像素是否相同
        :param image1:
        :param image2:
        :param x:
        :param y:
        :return:
        """
        pixel1=image1.load()[x,y]
        pixed2=image2.load()[x,y]
        threshold=60
        if abs(pixel1[0]-pixed2[0])<threshold and abs(pixel1[1]-pixed2[1])<threshold and abs(pixel1[2]-pixed2[2])<threshold:
            return True
        else:
            return False

    def get_gap(self,image1,image2):
        """
        获取缺口偏移量
        :param image1:
        :param image2:
        :return:
        """
        left=60
        for i in range(left,image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1,image2,i,j):
                    left=i
                    return left
        return left

    def get_track(self,distance):
        """
        根据偏移量获取移动轨迹
        :param distance:
        :return:
        """
        # 移动轨迹
        track=[]
        #  当前位移
        current=0
        #  减速阈值
        mid=distance*4/5
        # 计算间隔
        t=0.2
        # 初速度
        v=0

        while current<distance:
            if current<mid:
                # 加速度设定为2
                a=2
            else:
                # 加速度设为-3
                a=-3
            # 初始速度为0
            v0=v
            # 当前速度为 v=v0+at
            v=v0+a*t
            # 移动距离 x=v0t+1/2*a+t^2
            move=v0*t+1/2*a*t*t
            # 当前位移
            current+=move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_to_gap(self,slider,tracks):
        """
        拖动滑块到缺口处
        :param slider:
        :param tracks:
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def main(self):
        """整个验证过程"""
        # 进入登录页面
        self.go_register_page()
        # 获取当前截图
        image1=self.get_geetest_image()
        # 点击滑块
        self.get_slider().click()
        # 获取第二张截图
        imgae2=self.get_geetest_image()
        # 对比两张截图，获取缺口位置
        left=self.get_gap(image1,imgae2)
        # 获取轨迹
        track=self.get_track(distance=140)
        # 获取滑块
        slider=self.get_slider()
        # 滑动动作
        self.move_to_gap(slider,track)




if __name__=="__main__":
    creak=CreackGeetest()
    creak.main()


