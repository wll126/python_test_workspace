import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://19.3.11.5/')
time.sleep(2)
element=driver.find_element(By.ID,'nativeClient')
print(element.tag_name)
print(element.text)
element.click()
time.sleep(3)
driver.find_element_by_partial_link_text('VMware').click()
time.sleep(2)
# 湖北银行虚拟桌面安装使用指南.docx
driver.find_element_by_partial_link_text('虚拟桌面').click()
time.sleep(3)
driver.quit()

