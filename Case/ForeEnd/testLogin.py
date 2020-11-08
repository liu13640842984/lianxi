# coding=UTF-8
from Pages.ForeEnd import LoginPage
from Utils.Browser import Browser
from Pages.ForeEnd.LoginPage import *
import unittest
import time

class testLogin(unittest.TestCase):
    def setUp(self):
        self.driver = Browser().open('chrome')
        Browser().visit('http://testsaas.yunjes.cn/user/login')

    def test_login(self):
        LoginPage(self.driver).input_username('13640842984')
        LoginPage(self.driver).input_password('123456')
        LoginPage(self.driver).Click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()