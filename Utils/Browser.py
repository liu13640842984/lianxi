# coding=UTF-8
import time
from Base.BasePage import *
from Common.var import *
from Utils.FromatTime import *
from Utils.WaitUtil import *
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


# 浏览器类，封装各种操作关键字
class Browser:
    driver = None
    waitUtil = None

    def __init__(self):
        pass

    def open(self, browserName):
        # 打开浏览器
        global driver, waitUtil
        try:
            if browserName.lower() == "ie":
                print("打开IE浏览器")
                driver = webdriver.Ie(executable_path=ieDriverFilePath)
            elif browserName.lower() == "chrome":
                print("打开谷歌浏览器")
                # 创建Chrome浏览器的一个Options实例对象
                chrome_options = Options()
                # 添加屏蔽--ignore--certificate--errors提示信息的设置参数项
                chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                # executable_path = chromeDriverFilePath, chrome_options = chrome_options
                driver = webdriver.Chrome(chrome_options=chrome_options)
            else:
                print("打开火狐浏览器")
                driver = webdriver.Firefox(executable_path=firefoxDriverFilePath)
            # driver对象创建成功后，创建等待类实例对象
            waitUtil = WaitUtil(driver)
        except Exception as e:
            raise e
        return driver

    def visit(self, url):
        # 访问某个网站
        global driver
        try:
            driver.get(url)
            print("访问%s网站" % (url))
        except Exception as e:
            raise e
        return driver

    def assert_string_in_pagesource(self, assertString, *args):
        # 断言页面源码是否存在某个关键字或关键字符串
        global driver
        try:
            assert assertString in driver.page_source, u"%s not found in page source!" % assertString
        except AssertionError as e:
            raise AssertionError(e)
        except Exception as e:
            raise e

    def assert_title(self, titleStr, *args):
        # 断言页面标题是否存在给定的关键字符串
        global driver
        try:
            assert titleStr in driver.title, u"%s not found in page title!" % titleStr
        except AssertionError as e:
            raise AssertionError(e)
        except Exception as e:
            raise e

    def getTitle(self, *args):
        # 获取浏览器的页面标题
        global driver
        try:
            return driver.title
        except Exception as e:
            raise e

    def refresh(self, *args):
        # 刷新浏览器
        global driver
        try:
            driver.refresh()
        except Exception as e:
            raise e

    def back(self, *args):
        # 浏览器向后操作
        global driver
        try:
            driver.back()
        except Exception as e:
            raise e

    def forward(self, *args):
        # 浏览器向前操作
        global driver
        try:
            driver.forward()
        except Exception as e:
            raise e

    def getPageSource(self, *args):
        # 获取页面源码
        global driver
        try:
            return driver.page_source
        except Exception as e:
            raise e

    def cur_window_handle(self):
        # 获取当前浏览器句柄
        global driver
        try:
            return driver.current_window_handle
        except Exception as e:
            raise e

    def cur_url(self):
        # 获取当前窗口URL
        global driver

        try:
            return driver.current_url
        except Exception as e:
            raise e

    def sleep(self, sleepSeconds):
        # 强制等待
        global driver
        try:
            time.sleep(int(sleepSeconds))
        except Exception as e:
            raise e

    def close_browser(self, *args):
        # 关闭浏览器
        global driver
        try:
            driver.quit()
        except Exception as e:
            raise e

    # def paste_string(pasteString, *args):
    #     # 模拟Ctrl+V操作
    #     try:
    #         Clipboard.setText(pasteString)
    #         # 等待2秒，防止代码执行过快，而未成功粘贴内容
    #         time.sleep(2)
    #         KeyBoardKeys.twoKeys("ctrl", "v")
    #     except Exception as e:
    #         raise e

    # def press_tab_key(*args):
    #     # 模拟tab键
    #     try:
    #         KeyBoardKeys.oneKey("tab")
    #     except Exception as e:
    #         raise e

    # def press_enter_key(*args):
    #     # 模拟enter键
    #     try:
    #         KeyBoardKeys.oneKey("enter")
    #     except Exception as e:
    #         raise e

    def maximize(self, *args):
        # 窗口最大化
        global driver
        try:
            driver.maximize_window()
        except Exception as e:
            raise e

    def capture(self, file_path):
        try:
            driver.save_screenshot(file_path)
        except Exception as e:
            raise e

    def waitPresenceOfElementLocated(self, locationType, locatorExpression, *args):
        """显式等待页面元素出现在DOM中，但不一定可见，存在则返回该页面元素对象"""
        global waitUtil
        try:
            waitUtil.presenceOfElementLocated(locationType, locatorExpression)
        except Exception as e:
            raise e

    def waitFrameToBeAvailableAndSwitchToIt(self, locationType, locatorExprssion, *args):
        """检查frame是否存在，存在则切换进frame控件中"""
        global waitUtil
        try:
            waitUtil.frameToBeAvailableAndSwitchToIt(locationType, locatorExprssion)
        except Exception as e:
            raise e

    def waitVisibilityOfElementLocated(self, locationType, locatorExpression, *args):
        """显式等待页面元素出现在Dom中，并且可见，存在返回该页面元素对象"""
        global waitUtil
        try:
            waitUtil.visibilityOfElementLocated(locationType, locatorExpression)
        except Exception as e:
            raise e