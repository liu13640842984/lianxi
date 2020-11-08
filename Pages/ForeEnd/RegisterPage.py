# coding=UTF-8
from Base.BasePage import BasePage

#注册页
class RegisterPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.username_inputbox = {'element_name':'输入用户名', 'locater_type':'xpath', 'locater_value':"//input[@id='username']", 'timeout':15}
        self.password_inputbox = {'element_name':'输入密码', 'locater_type':'xpath', 'locater_value':'//input[@id="password"]', 'timeout':15}
        self.code_inputbox =     {'element_name':'输入验证码', 'locater_type':'xpath', 'locater_value':'//input[@id="code"]', 'timeout':15}
        self.invite_code_inputbox = {'element_name':'推荐人邀请码', 'locater_type':'xpath', 'locater_value':'//input[@id="inviteCode"]', 'timeout':15}
        self.company_inputbox = {'element_name':'输入公司名', 'locater_type':'xpath', 'locater_value':'//input[@id="inviteCode"]', 'timeout':15}
        self.checkbox = {'element_name':'注册复选框', 'locater_type':'xpath', 'locater_value':"//*[@id='agreement-checkbox']", 'timeout':15}
        self.register_button = {'element_name':'注册按钮', 'locater_type':'xpath', 'locater_value':'//*[@class="btn-center"]/button', 'timeout':15}

    def input_username(self, content):
        self.input(self.username_inputbox, content)

    def input_password(self, content):
        self.input(self.password_inputbox, content)
        # self.driver.find_element(By.XPATH, self.password_inputbox['locater_value']).send_keys(content)

    def input_code(self, content):
        self.input(self.code_inputbox, content)


    def input_invite_code(self, content):
        self.input(self.invite_code_inputbox, content)


    def input_company(self, content):
        self.input(self.company_inputbox, content)

    def Register(self):
        self.click(self.register_button)
        # self.driver.find_element(By.XPATH, self.login_button['locater_value']).click()