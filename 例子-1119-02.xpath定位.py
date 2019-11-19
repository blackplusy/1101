#coding=utf-8

from selenium import webdriver
br=webdriver.Chrome()
br.get("https://www.baidu.com")
# br.find_element_by_xpath("//*[@id='kw']").send_keys("娃哈哈")
# br.find_element_by_xpath("//*[@autocomplete='off']").send_keys("小洋人")
# br.find_element_by_xpath("//a[@class='mnav'][1]").click()
br.find_element_by_xpath("//a[@class='mnav' and @name='tj_trnews']").click()