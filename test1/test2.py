import time
from selenium import webdriver

driver=webdriver.PhantomJS()
driver.get('http://www.baidu.com')
print(driver.current_url)
time.sleep(5)
driver.quit()