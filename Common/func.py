# coding=UTF-8
import time
import requests
import sys
import os
import json
import configparser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Utils.Excel import *
from Common.var import *




# 本文件专供测试使用
class Common:
    def __init__(self):
        pass

    def getDriver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        return self.driver

    def myQuit(self):
        '''
        退出浏览器
        :return:
        '''
        self.driver.quit()

    def getActionChains(self, driver):
        return ActionChains(driver)

    def getTimeSleep(self, obj):
        '''
        :param obj:传入的时间(秒)
        :return:
        '''
        return time.sleep(obj)

    def find_element(self, *ele_param):
        # 获取定位的元素
        return self.driver.find_element(*ele_param)

    def sendKeys(self, input_Content, *ele_param):
        '''
        :param input_Content:输入的参数
        :param ele_param: 定位的元素
        :return:
        '''
        self.find_element(*ele_param).send_keys(input_Content)

    def click(self, *element):
        '''
        :param element: 定位的元素
        :return:
        '''
        self.find_element(*element).click()

    def perform(self, driver, *param):
        '''
        执行ActionChains链式操作
        :param driver:驱动器
        :param ele: 定位的元素
        :return:
        '''
        ele = self.find_element(*param)
        return self.getActionChains(driver).move_to_element(ele).perform()

    # 接口测试专用方法
    def testRequest(self, method, url, data):
        '''
        测试接口
        :return:
        '''
        if method == 'get':
            res = requests.get(url, data)

        elif method == 'post':
            data = str(data).replace("'", '"').replace('\\', '\\\\')
            if self.is_json(data):
                res = requests.post(url=url, json=data)
            res = requests.post(url, data)

        elif method == 'param':
            res = requests.post(url=url, param=data)

        print(res.text)

    def is_json(self, data):
        import json
        '''
        是否为json字符串
        :return:
        '''
        try:
            jsonData = json.loads(data)
        except ValueError as e:
            return False
        return True

    #获取配置文件信息
    def get_conf_info(filename, encoding="utf-8"):
            dictData = {}
            curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            cfgpath = os.path.join(curpath, filename)
            conf = configparser.ConfigParser()
            conf.read(cfgpath, encoding)
            sections = conf.sections()
            itemList = []
            [itemList.append(dict(conf.items(item))) for item in sections]
            for index1, value1 in enumerate(sections):
                for index2, value2 in enumerate(itemList):
                    if index1 == index2:
                        dictData.update({value1:value2})
            return dictData
            # return itemList


    def getError(self, param):
        try:
            param
        except Exception as e:
            print(format(e))


# 获取Excel表格数据
def get_excel_data(**kwargs):
    excel = ReadExcel.get_request_data(**kwargs)
    return excel

#返回实际结果
# def decorator_func(url, method, payload):
#     res = RequestHandler()
#     login_res = res.visit(method, url, json=payload)
#     return json.loads(login_res.text)

# 返回预期结果
# def expect_res(case_id):
#     res = json.loads(excel[case_id]['预期结果'])
#     return res['message']


if __name__ == '__main__':
    excel = get_excel_data(sheetName=excel_sheet_name_Sheet1)
    print(excel)
