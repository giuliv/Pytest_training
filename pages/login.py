from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage

class ConnectLoginPage(BasePage):
    #URL =

    USER_INPUT = (By.ID, 'login')
    PWD_INPUT = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '/html/body/div/div/form[1]/div[4]/button')

    def __init__(self, browser):
        #self.browser = browser
        super().__init__(browser)

    def load(self):
        self.browser.get(self.URL)

    def writeuser(self, username):
        #user_input = self.browser.find_element(*self.USER_INPUT)
        #user_input.send_keys(username + Keys.RETURN)
        self.type_on_element(self.USER_INPUT, username + Keys.RETURN)

    def writepassword(self, password):
        self.type_on_element(self.PWD_INPUT, password + Keys.RETURN)

    def pressloginbtn(self):
        self.click_on_element(self.LOGIN_BTN)
