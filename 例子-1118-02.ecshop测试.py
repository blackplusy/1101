#coding=utf-8

from selenium import  webdriver
browser=webdriver.Chrome()
browser.get("http://192.168.6.178/ecshop1/user.php")
browser.find_element_by_name("username").send_keys("kouniqiwa")
browser.find_element_by_name("password").send_keys("123456")
browser.find_element_by_name("submit").click()