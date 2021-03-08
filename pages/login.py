from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage

class ConnectLoginPage(BasePage):
    URL = 'https://connect.sandbox.appetize-dev.com/login'
    TITLE_PAGE = (By.XPATH, '/html/head/title')
    USER_INPUT = (By.ID, 'login')
    PWD_INPUT = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '/html/body/div/div/form[1]/div[4]/button')



    def __init__(self, browser):
        #self.browser = browser
        super().__init__(browser)

    def load(self):
        self.browser.get(self.URL)
        assert "Appetize Connect - Login" in self.browser.title

    @classmethod
    def title_page(cls, title):
        xpath = f"/html/head/*[contains(text(), '{title}')]"
        return By.XPATH, xpath

    def title_connect(self, title):
        title_result = self.get_element(self.title_page(title))
        #return title_result.text
        return title_result.text

    @classmethod
    def LOGIN_RESULT(cls, phrase):
        xpath = f"/html/body/div/div/form[1]/div[4]/*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    def login_result_count(self, phrase):
        login_result = self.get_elements(self.LOGIN_RESULT(phrase))
        return len(login_result)

    def login_to_connect(self, username, password):
        self.type_on_element(self.USER_INPUT, username + Keys.RETURN)
        self.type_on_element(self.PWD_INPUT, password + Keys.RETURN)
        self.click_on_element(self.LOGIN_BTN)

    def writeuser(self, username):
        #user_input = self.browser.find_element(*self.USER_INPUT)
        #user_input.send_keys(username + Keys.RETURN)
        self.type_on_element(self.USER_INPUT, username + Keys.RETURN)

    def writepassword(self, password):
        self.type_on_element(self.PWD_INPUT, password + Keys.RETURN)

    def pressloginbtn(self):
        self.click_on_element(self.LOGIN_BTN)
