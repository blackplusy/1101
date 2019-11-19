#coding=utf-8
from selenium import  webdriver
br=webdriver.Chrome()
br.get("https://www.baidu.com")
#1.单一属性定位
# br.find_element_by_css_selector('input').send_keys("aa")
# br.find_element_by_css_selector("#kw").send_keys("888")
# br.find_element_by_css_selector(".s_ipt").send_keys("hongkong")
# br.find_element_by_css_selector("[name='wd']").send_keys("python")
#2.组合属性定位
# br.find_element_by_css_selector("input#kw").send_keys("simida")
# br.find_element_by_css_selector("input.s_ipt").send_keys("www")
# br.find_element_by_css_selector("input[name='wd']").send_keys("baidu")
# br.find_element_by_css_selector('input[autocomplete]').send_keys("中国足球")
# br.find_element_by_css_selector("[name='wd'][autocomplete='off']").send_keys("何日出头")
br.find_element_by_css_selector("input[class*='ipt']").send_keys("周琦")
# br.find_element_by_css_selector("input[class^='bg']").click()
br.find_element_by_css_selector("input[class$='btnhover']").click()