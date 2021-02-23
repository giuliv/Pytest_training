from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class CrudItem(BasePage):
    ITEM_BTN = (By.XPATH, '/html/body/div[1]/aside/div/nav/ul/li[7]/a')
    ITEM_UP_BTN = (By.XPATH, '/html/body/div[1]/main/div/div[1]/h1/a')
    ITEM_ITEM_BTN = (By.XPATH, '/html/body/div[1]/aside/div/nav/ul/li[7]/ul/li[1]/a')
    CREATE_BTN = (By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div[2]/div[2]/button')
    ITEM_NAME = (By.ID, 'name')
    IType_drop = (By.ID, 'type')
    ITEM_COST = (By.ID, 'cost')
    PHRASE = 'drink'
    DRINK_BTN = (By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[1]/div[2]/div/select/option[4]')
    SAVE_BTN = (By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[2]/button[2]')
    DrinkType = (By.XPATH, '//*[@id="type"]/option[4]')
    SEARCH_BAR = (By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div[2]/div[1]/div/input')
    result_item_search = (By.CSS_SELECTOR,
                          'body > div.container-fluid.page-wrapper.js-wrapper > main > div.listing.js-listing > div.table-responsive > table > tbody > tr')
    confirm_delete_btn = (By.CSS_SELECTOR,
                          'body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-danger')
    DELETE_BTN = (By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/table/tbody/tr[1]/td[7]/div[2]/ul/li[2]/a')
    OPTIONS_ITEMS = (By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/table/tbody/tr[1]/td[7]/div[2]/span/i')
    ITEM_SEARCHED = (By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/table/tbody/tr[1]')
    PEN_BTN = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/form[1]/div/div[2]/div[1]/div[2]/div/div/button')
    PRICE_FIELD = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/form[1]/div/div[2]/div[1]/div[2]/div/input')

    @classmethod
    def Type_RESULTS(cls, PHRASE):
        # *[contains(text(), '{PHRASE}')]
        xpath = f"//*[@id='type']/option[4]//"
        return (By.XPATH, xpath)

    def clickItem(self):
        self.click_on_element(self.ITEM_BTN)

    def clickITEM_I(self):
        self.click_on_element(self.ITEM_ITEM_BTN)

    def clickCreate(self):
        self.click_on_element(self.CREATE_BTN)

    def NameItem(self, itemName):
        self.type_on_element(self.ITEM_NAME, itemName + Keys.RETURN)

    def CostItem(self, itemCost):
        self.type_on_element(self.ITEM_COST, itemCost + Keys.RETURN)

    def TypeItem(self):
        self.click_on_element(self.IType_drop)

    def DrinkType(self):
        # tp_results = self.click_on_element(self.Type_RESULTS(phrase))
        # return len(tp_results)
        self.click_on_element(self.DRINK_BTN)
        # type_results = self.browser.find_elements(*self.Type_RESULTS(phrase))
        # type_results.click()
        # return len(type_results)
        # self.get_element(self.DrinkType)

    def SaveItem(self):
        self.click_on_element(self.SAVE_BTN)

    def SearchItem(self, itemName):
        # self.get_element(self.result_item_search, itemName + Keys.RETURN)
        self.type_on_element(self.SEARCH_BAR, itemName + Keys.RETURN)

    def ItemLocated(self, itemName):
        item_result = self.click_on_element(self.get_elements(self.result_item_search))
        return len(item_result)

    def ItemSearched(self):
        self.click_on_element(self.ITEM_SEARCHED)

    def EditPrice(self):
        self.click_on_element(self.PEN_BTN)

    def WriteNewPrice(self,new_price):
        self.type_on_element(self.PRICE_FIELD, new_price + Keys.RETURN)

    def ReturnItemsList(self):
        self.click_on_element(self.ITEM_UP_BTN)

    def clickOption(self):
        self.click_on_element(self.OPTIONS_ITEMS)


    def clickDelete(self):
        self.click_on_element(self.DELETE_BTN)

    def delete_item(self):
        self.click_on_element(self.confirm_delete_btn)
