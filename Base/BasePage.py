# coding=UTF-8
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Utils.Logger import Logger
import os
import time



#页面继承类
# logger = Logger(logger='BasePage页面基类').getlog()
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

        # 元素定位， element_info字典类型的数据
    def find_element(self, element_info):
        locater_type_name = element_info['locater_type']
        locater_value = element_info['locater_value']
        locator_timeout = element_info['timeout']

        locator={
            'id':By.ID,
            'name':By.NAME,
            'class_name':By.CLASS_NAME,
            'tab_name':By.TAG_NAME,
            'css_selector':By.CSS_SELECTOR,
            'link_text':By.LINK_TEXT,
            'xpath':By.XPATH
        }

        if locater_type_name in locator:
            locater_type = locator[locater_type_name]

        # if locater_type_name == 'id':
        #     locater_type = By.ID
        # elif locater_type_name == 'name':
        #     locater_type = By.NAME
        # elif locater_type_name == 'class_name':
        #     locater_type = By.CLASS_NAME
        # elif locater_type_name == 'tab_name':
        #     locater_type = By.TAG_NAME
        # elif locater_type_name == 'css_selector':
        #     locater_type = By.CSS_SELECTOR
        # elif locater_type_name == 'link_text':
        #     locater_type = By.LINK_TEXT
        # elif locater_type_name == 'xpath':
        #     locater_type = By.XPATH

        element = WebDriverWait(self.driver, locator_timeout).until(
            lambda x:x.find_element(locater_type, locater_value)
        )
        # logger.info('[%s]元素识别成功'%element_info['element_name'])
        return element




    # 获取单个页面元素对象
    @classmethod
    def getElement(driver, localtorType, localtorExpression):
        try:
            element = WebDriverWait(driver, 5).until(
                lambda x: x.find_element(by=localtorType, value=localtorExpression))
            return element
        except Exception as e:
            raise e


    # 获取多个页面元素对象
    @classmethod
    def getElement(driver, localtorType, localtorExpression):
        try:
            elements = WebDriverWait(driver, 5).until(
                lambda x: x.find_elements(by=localtorType, value=localtorExpression))
            return elements
        except Exception as e:
            raise e


        #切换到其他页面窗口句柄
    def window_handler(self, handle_type):
        if handle_type == 'all':
            return self.driver.window_handles
        elif handle_type == 'cur':
            return self.driver.current_window_handle


    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)


        #切换至其他的frame， element_info为frame的id值 或index值 字典类型值
    def switch_to_frame(self, locatorType, element_info):
        if locatorType == 'webEle_Type':
            self.driver.switch_to.frame(self.driver.find_element(element_info))
        elif locatorType == 'other':
            self.driver.switch_to.frame(element_info)# 传入frame的index 或 frame的Id


        #切换回原来的frame
    def switch_to_default_content(self, *args):
        # 切换frame
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e



        # 获取某元素属性值 value='用户名'，element_info为字典类型数据，content某元素属性的key
    def get_attr(self, element_info, content):
        element = self.find_element(element_info)
        return element.get_attribute(content)


        # 获取URL元素文本值，element_info为字典类型数据
    def text(self, element_info):
        try:
            element = self.find_element(element_info)
        except Exception as e:
            return element.text



#鼠标事件
        # 点击事件 使用时，请在相应的页面类，增加元素属性字典，element_info为字典类型数据
    def click(self, element_info):
        self.find_element(element_info).click()
        # logger.info('点击了[%s]元素'%element_info['element_name'])


        # 鼠标右键事件context，   鼠标双击事件double，一般用在新闻链接点击上
    def context_or_double_click(self, click_type, element_info, content):
        element = self.driver.find_element(element_info, content)
        if click_type=='context':
            ActionChains(self.driver).context_click(element).perform()
        elif click_type=='double':
            ActionChains(self.driver).double_click(element).perform()

#键盘事件
        # 输入事件 使用时，请在相应的页面类，增加元素属性字典，element_info为字典类型数据
    def input(self, element_info, content):
        '''
        如果content + Keys.BACK_SPACE，可以组合成键盘事件
        SPACE：空格键  TAB：TAB键，ESCAPE：回退键，ENTER：回车键
        '''
        element = self.find_element(element_info)
        element.send_keys(content)
        # logger.info('[%s]元素了[%s]'%(element_info['element_name'], content))



        # 输入内容的清除事件， element_info为字典类型数据
    def clear(self, element_info):
        # 清空输入框默认内容
        try:
            element = self.find_element(element_info)
            element.clear()
        except Exception as e:
            raise e


        # 判断元素是否被选择，element_info为字典类型数据
    def is_selected(self, element_info):
        try:
            element = self.find_element(element_info)
        except Exception as e:
            raise e
        return element.is_selected()


        # 判断元素是否可用，element_info为字典类型数
    def is_enabled(self, element_info):
        try:
            element = self.find_element(element_info)
        except Exception as e:
            raise e
        return element.is_enabled()


        # 判断元素在页面中是否显示，element_info为字典类型
    def is_displayed(self, element_info):
        try:
            element = self.find_element(element_info)
        except Exception as e:
            raise e
        return element.is_displayed()

        # 获取当前文件根目录
    def file_path(self, dirName):
        cur_file_path = os.path.dirname(os.path.dirname(__file__))
        return os.path.join(cur_file_path, dirName)

        #获取当前时间
    def getTime(self):
        return time.strftime('%Y-%m-%d %H-%M-%S')


        #截图，dirName：保存的目录, fileName：文件名 + 后缀名
    def save_screenshot(self, dirName, fileName):
        filePath = self.file_path(dirName)
        self.driver.save_screenshot(filePath + "/" + ("%s_%s"%(self.getTime(), fileName)))

    #验证码处理

if __name__ == "__main__":
    pass
        # from selenium import webdriver
        # # 进行单元测试
        # driver = webdriver.Chrome(executable_path="E:\SeleniumProject\driver\chromedriver.exe")
        # driver.maximize_window()
        # driver.get("https://mail.126.com/")
        # time.sleep(2)
        # lb = getElement(driver, "id", "lbNormal")
        # print(lb)
        # driver.quit()