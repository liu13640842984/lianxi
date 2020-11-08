# coding=UTF-8
import unittest,time,os
from BeautifulReport import BeautifulReport
from Case import testMy

current_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
report_path =  os.path.join(current_path, 'Report')
now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
# 报告地址&名称
report_title = 'Example报告' + now + ".html"  # 如果不能打开这个文件，可能是now的格式，不支持：和空格
if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(testMy))
    #运行用例filename=报告名称，description=所有用例总的名称，report_path=报告路径,如果不填写默认当前执行文件目录，theme=报告的主题，有四种可以选择：theme_default，theme_cyan，theme_candy，theme_memories  默认是第一种
    BeautifulReport(suite).report(filename="测试报告"+now, description='Test_01模块', log_path=report_path)




# coding=UTF-8
import unittest
from Utils.Report import *

class UnittestCaseSecond(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""

    def test_equal(self):
        """
        test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.assertTrue(1 == 1)

    # @BeautifulReport.add_test_img('测试报告.png')
    def test_is_none(self):
        """
        test None object
        :return:
        """
        # save_some_img('测试报告.png')
        self.assertIsNone(None)
