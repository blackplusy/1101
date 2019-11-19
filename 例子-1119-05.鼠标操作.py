#coding=utf-8
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
br=webdriver.Chrome()
# br.get("https://www.baidu.com")
#基础操作
# element=br.find_element_by_link_text("设置")
# #单击元素(click)
# ActionChains(br).click(element).perform()
# #元素上按下左键不放(click_and_hold)
# ActionChains(br).click_and_hold(element).perform()
# #元素上单击右键
# ActionChains(br).context_click(element).perform()
#拖拽1
# source=br.find_element_by_link_text("hao123")
# target=br.find_element_by_link_text("设置")
# ActionChains(br).drag_and_drop(source,target).perform()
#拖拽2
br.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
br.maximize_window()
br.switch_to.frame('iframeResult')
source=br.find_element_by_id("draggable")
target=br.find_element_by_id("droppable")
actions=ActionChains(br)
actions.drag_and_drop(source,target)
actions.perform()
