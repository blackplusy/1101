#coding=utf-8
import time
from selenium import  webdriver
br=webdriver.Chrome()
url="https://www.baidu.com"
br.get(url)
time.sleep(3)
url2="https://www.4399.com"
br.get(url2)
time.sleep(1)
br.back()
time.sleep(1)
br.forward()
time.sleep(1)
br.refresh()
br.get_screenshot_as_file("D:\\memeda.png")
br.quit()
# br.set_window_size(480,800)  #设置浏览器像素宽480
# time.sleep(1)
# br.maximize_window()
# time.sleep(1)
# br.minimize_window()

