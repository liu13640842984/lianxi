# coding=utf-8
import time
import unittest
import sys
from selenium import webdriver
from imp import reload


class BaiduSearch(unittest.TestCase):
    '''         定义一个普通方法test_1     '''

    def test_1(self):
        print('test_1')

    def two(self):
        print('two')

    def setUp(self):
        print("开始")
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.set_up = 'set_up'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get('https://www.baidu.com')

    def tearDown(self):
        self.driver.quit()
        self.driver.implicitly_wait()

        # print(self.set_up)#可以直接打印框架内部的方法属性,
        # print(self.two)#可以打印普通方法的属性<bound method BaiduSearch.two of <__main__.BaiduSearch testMethod=test_baidu>>
        # print(self.test_1)#也可以打印测试用例方法的属性<bound method BaiduSearch.test_1 of <__main__.BaiduSearch testMethod=test_baidu>>
        # self.test_1() #可以直接调用测试用例方法
        # self.two()#可以直接普通方法 或 框架内的方法

    def test_baidu(self):
        print(self.driver.title)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)
        try:
            assert '百度一下，你就知道' in self.driver.title
        except Exception as e:
            print('test fail', format(e))


if __name__ == '__main__':     unittest.main()




'''

unittest几大组成部分：
                    TestCase: 用例对象，编写测试用例时要继承该类，以具有TestCase的属性和方法
                    TestSuite: 测试集或测试套件，测试用例的集合，用来组织用例，支持嵌套
                    TestLoader: 用例加载器，用于向TestSuite中添加用例
                    TextTestRunner: 用例执行器（输出文本结果），一般以TestSuite为单位执行用例
                    TestResult: 测试结果
'''




'''
用例断言 unittest提供了丰富的断言方法，常用为以下几种：

判断相等
assertEqual(a,b)/assertNotEqual(a,b): 断言值是否相等
assertIs(a,b)/assertIsNot(a,b): 断言是否同一对象（内存地址一样）
assertListEqual(list1, list2)/assertItemNotEqual(list1, list2): 断言列表是否相等
assertDictEqual(dict1, dict2)/assertDictNotEqual(dict1, dict2): 断言字典是否相等
是否为空
assertIsNone(a)/assertIsNotNone(a)
判断真假
assertTrue(a)/assertFalse(a)
是否包含
assertIn(a,b)/assertNotIn(a,b) # b中是否包含a
大小判断
assertGreater(a,b)/assertLess(a,b) : 断言a>b / 断言a<b
assertGreaterEqual(a,b)/assertLessEqual: 断言a>=b / 断言a<=b
类型判断
assertIsInstance(a,dict)/assertNotIsInstance(a,list) # 断言a为字典 / 断言a非列表
'''


# 执行指定测试用例
# suite = unittest.TestSuite()
#     suite.addTests([testMy("test_four"),testMy("test_three")])
#     with open('a.txt', 'a') as f:
#         runner = unittest.TextTestRunner(stream=f, verbosity=2)
#         runner.run(suite)

