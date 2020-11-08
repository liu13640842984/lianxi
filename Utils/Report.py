# coding=UTF-8
import unittest,time,os
from BeautifulReport import BeautifulReport


class Report:
    #生成报告类，Object为加载的测试类, ModelName为被测试的模块名称
    def getReport(self, Object):
        print(Object)
        current_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        report_path = os.path.join(current_path, 'Report')
        now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
        report_title = 'Example报告' + now + ".html"  # now时间格式，不支持：和空格


        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTests(loader.loadTestsFromTestCase(Object))
        # 运行用例filename=报告名称，description=所有用例总的名称，report_path=报告路径,如果不填写默认当前执行文件目录，theme=报告的主题，有四种可以选择：theme_default，theme_cyan，theme_candy，theme_memories  默认是第一种
        BeautifulReport(suite).report(filename="测试报告" + now, description='我的模块', log_path=report_path)