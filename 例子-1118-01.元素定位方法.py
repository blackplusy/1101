#coding=utf-8

#导入webdriver，用于调用
from selenium import webdriver
#加载驱动，浏览器是什么类型驱动就必须是什么类型
br=webdriver.Chrome()
#打开目标网页
br.get("https://www.baidu.com")
#1.通过id进行定位并且发送数据
#find       搜索
#element    元素
#by         通过
# br.find_element_by_id("kw").send_keys("黑哥真帅！！")
#2.通过name进行定位
# br.find_element_by_name("wd").send_keys("猪肉降价")
#3.通过class进行定位
# br.find_element_by_class_name("s_ipt").send_keys("丢雷老谋")
#4.tag定位
# br.find_element_by_tag_name("input").send_keys("aaa")
#5.通过link定位
# br.find_element_by_link_text("新闻").click()
#6.通过partial_link定位
# br.find_element_by_partial_link_text("闻").click()
#7.xpath定位
# br.find_element_by_xpath("//*[@id='kw']").send_keys("aaa")
#8.CSS定位
br.find_element_by_css_selector("#kw").send_keys("乔碧罗")
