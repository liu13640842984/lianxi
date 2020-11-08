# coding=UTF-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://testsaas.yunjes.cn/user/register')
checkbox = driver.find_element_by_xpath("//*[@id='agreement-checkbox']")
if checkbox.is_selected():
    print('被选中')
    checkbox.click()