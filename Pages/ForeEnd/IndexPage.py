# coding=UTF-8
from Base.BasePage import BasePage

#网站首页
class IndexPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.username_inputbox = {'element_name':'用户名输入框', 'locater_type':'xpath', 'locater_value':"//input[@id='username']", 'timeout':15}
        self.password_inputbox = {'element_name':'密码输入框', 'locater_type':'xpath', 'locater_value':'//input[@id="password"]', 'timeout':15}
        self.login_button = {'element_name':'登陆按钮', 'locater_type':'xpath', 'locater_value':'/html/body/div[1]/div[3]/div/div/div/button', 'timeout':15}

    def input_username(self, content):
        self.input(self.username_inputbox, content)
        # self.driver.find_element(By.XPATH, self.username_inputbox['locater_value']).send_keys(content)

    def input_password(self, content):
        self.input(self.password_inputbox, content)
        # self.driver.find_element(By.XPATH, self.password_inputbox['locater_value']).send_keys(content)

    def Click(self):
        self.click(self.login_button)
        # self.driver.find_element(By.XPATH, self.login_button['locater_value']).click()