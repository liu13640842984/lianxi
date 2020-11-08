# coding=UTF-8
# import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding("utf-8")
from selenium.webdriver.common.by import By
from study.testCommon import testCommon
from Common.Db import DB


'''
获取公用的方法
'''
# testCommon = testCommon()#调用公共学习的文件
# driver = testCommon.getDriver()#获取驱动器


db = DB()
result = db.queryDb("select * from user")
print(result)






# bg_config = driver.find_element(By.CSS_SELECTOR,"span[name='tj_settingicon']")
# getActionChains.move_to_element(bg_config).perform()
# driver.find_element_by_link_text("搜索设置").click()
#
# time.sleep(2)
#
# ul_ele = driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/div/div/ul")
# li_eles = ul_ele.find_elements_by_xpath('li')
# li_eles_index = range(len(li_eles))#获取元素的步长值
#
#
#
# for i in li_eles:
#     print(i.text)
#     for step in li_eles_index:
#         if i.text=='高级搜索':
#             li_eles[step].click()




#一，元素定位八大方法：
# driver.find_element_by_id('kw').send_keys('abc')，Id定位
# driver.find_element_by_name('wd').send_keys('abcd')，Name定位
# driver.find_element_by_css_selector('.s_ipt').send_keys('abcd')，Css选择器定位
# driver.find_element_by_css_selector("input[name='wd']").send_keys('abcd')

# driver.find_element_by_css_selector('#kw').send_keys('abcd')
'''
Css选择器定位常用的属性方式
.intro，选择class=intro的所有元素
#firstname，选择id=firstname的所有元素
*，选择所有元素
p，选择所有<p>元素
div,p，选择所有<div>元素和所有<p>元素
div p，选择<div>元素内部的所有<p>元素
div>p，选择父元素为<div>元素的所有<p>元素
div+p，选择紧接在<div>元素之后的所有<p>元素
[target]，选择带有target属性的所有元素
[target=_blank]，选择target=_blank 的所有元素
[title~=flower]，选择title属性中包含单词"flower"的所有元素
'''

# driver.find_element_by_class_name('s_ipt').send_keys('ab')，Class名称定位
# driver.find_element_by_link_text('新闻').click() 超链接文字作为关键字来定位元素
# driver.find_element_by_partial_link_text('新').click() 超链接中部分文字作为关键字来定位元素
# driver.find_element_by_xpath("//*[@name='email']").send_keys('abc') 使用xpath方式进行定位
# driver.find_element_by_tag_name('form').get_attribute('name') 通过标签名定位




'''
# 二，常用方法
send_keys()：模拟键盘输入
text：获取文本值
get_attribute()：获取属性对应的值
maximize_window()：浏览器窗口最大化
current_window_handle：返回窗口句柄
driver.current_url：获取当前窗口URL
is_selected()：判断元素是否被选择
is_enabled()：判断页面元素是否可用
is_displayed()：判断页面元素是否显示
clear()：清除输入框的值
quit()：关闭浏览器
title：获取页面标题
refresh()：刷新页面
back()：浏览器工具栏向后操作
forward()：浏览器工具栏向前操作
'''


'''
三，鼠标悬停操作
    click：鼠标单击
    click_and_hold：鼠标单击并且按住不放
    double_click：鼠标双击
    context_click：鼠标右击
    drag_and_drop：鼠标拖拽
    key_down：按住某个键
    key_up：松开某给键
    move_to_element：将鼠标移动指定的某个页面元素
    move_to_element_with_offset：将鼠标移动指定的某个页面元素
    perform：ActionChains执行,结合drag_and_drop，move_to_element等方法使用
    release：释放按下的鼠标
'''


'''
四，Jquery操作页面元素
    jq1 ="$('#kw').val('selenium')"
    driver.execute_script(jq1)
    jq2 ="$('#su').click()"
    driver.execute_script(jq2)
'''

'''
五，常用鼠标事件
     context_click()：鼠标右击操作
     double_click()：鼠标双击操作
     drag_and_drop()：鼠标拖拽操作
     move_to_element()：鼠标悬停操作
'''

'''
六，常用的键盘事件
    Keys.BACK_SPACE：删除键
    Keys.SPACE：空格键
    Keys.TAB：Tab键
    Keys.ESCAPE：回车键
    。。。
'''

'''
七，Frame操作
    switch_to_frame：切换到frame内部操作元素
    switch_to_default_content：切换会原来到frame外部操纵元素
    
    还可以通过以下方式来定位
    1.通过index来定位，driver.switch_to_frame(0)
    2.通过属性来定位，driver.switch_to_frame("login_frame")
    3.通过WebElement对象模式来定位，driver.switch_to_frame(driver.find_element_by_id("login_frame"))
'''

'''
八，Selenium帮助文档
     Doc命令下运行，python -m pydoc -p4567
'''

'''
九，Cookie操作
'''