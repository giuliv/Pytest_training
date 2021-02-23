from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ItemDeleteItem:
    ITEM_LIST = (By.CSS_SELECTOR, '#tr > tbody')
    SEARCH_BAR = (By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div[2]/div[1]/div/input')
    SEARCH_BAR = (By.NAME, 'search_text')
    ITEM_NAME = 'autogiuli'
    def __init__(self, browser):
        super().__init__(browser)

    def delete(self):
        search_br = self.get_element(self.SEARCH_BAR)
        #search_bar = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[1]/div[2]/div[1]/div/input')
        search_br.send_keys(self.ITEM_NAME + Keys.RETURN)
        time.sleep(2)
        result_item_search = browser.find_elements_by_css_selector(
           'body > div.container-fluid.page-wrapper.js-wrapper > main > div.listing.js-listing > div.table-responsive > table > tbody > tr')
        assert len(result_item_search) > 0
        # result_item_search = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/table/tbody/tr')
        # body > div.container - fluid.page - wrapper.js - wrapper > main > div.listing.js - listing > div.table - responsive > table > tbody > tr
        # assert len(result_item_search) > 0

        options_item = browser.find_element_by_xpath(
           '/html/body/div[1]/main/div[2]/div[2]/table/tbody/tr[1]/td[7]/div[2]/span/i')
        options_item.click()
        time.sleep(2)

        delete_btn = browser.find_element_by_xpath(
           '/html/body/div[1]/main/div[2]/div[2]/table/tbody/tr[1]/td[7]/div[2]/ul/li[2]/a')
        delete_btn.click()
        time.sleep(3)

        # confirm_delete_btn = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
        confirm_delete_btn = browser.find_element_by_css_selector(
            'body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-danger')
        confirm_delete_btn.click()
        time.sleep(6)

