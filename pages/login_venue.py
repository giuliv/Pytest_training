from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage

class LoginToVenue(BasePage):
    SEARCH_BAR = (By.XPATH, '/html/body/div[1]/main/div[2]/div/input')
    BTN_VENUE = (By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[5]/div/button[2]')
    BODY = (By.XPATH, '/html/body/div[1]/main')

    def searchvenue(self, venue):
        self.type_on_element(self.SEARCH_BAR, venue + Keys.RETURN)
        #self.browser.get(self.SEARCH_BAR, venue + Keys.RETURN)

    def clickLogin(self):
        self.click_on_element(self.BTN_VENUE)

    def clickbody(self):
        self.click_on_element(self.BODY)
