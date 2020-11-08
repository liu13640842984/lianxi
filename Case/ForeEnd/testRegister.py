# coding=UTF-8
from Pages.ForeEnd import RegisterPage
from Utils.Browser import Browser
from Pages.ForeEnd.RegisterPage import *
from Common.func import *
import time
import unittest
import warnings

class testRegister(unittest.TestCase):
    def setUp(self):
        self.excel = get_excel_data(sheetName=excel_sheet_name_Sheet1)
        self.url = self.excel['login001']['请求url']
        warnings.simplefilter('ignore', ResourceWarning)

        self.driver = Browser().open('chrome')
        Browser().visit('http://testsaas.yunjes.cn/user/login')

    def test_login(self):
        RegisterPage(self.driver).input_username('13640842984')
        RegisterPage(self.driver).input_password('123456')
        RegisterPage(self.driver).Click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()