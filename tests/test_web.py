import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
import logging

from pages.crud_item import CrudItem
from pages.login import ConnectLoginPage
from pages.login_venue import LoginToVenue


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login(browser):
    #URL =
    USERNAME = 'qaregressionteam'
    PWD = '@ppetiz3!'
    VENUE = '393'
    NAME_ITEM = 'autogiuli'
    COST_ITEM = '11'
    TYPE_ITEM = 'drink'

    login_page = ConnectLoginPage(browser)
    login_page.load()
    login_page.writeuser(USERNAME)



    # browser.get(URL)
    #
    # login_input = browser.find_element_by_id('login')
    # login_input.send_keys(USERNAME + Keys.RETURN)

    pwd_input = browser.find_element_by_id('password')
    pwd_input.send_keys(PWD + Keys.RETURN)
    pwd_input.send_keys(Keys.RETURN)

    login_page.writepassword(PWD)
    login_page.pressloginbtn()


    #btn = browser.find_elements_by_xpath('/html/body/div/div/form[1]/div[4]/button')
    #btn = browser.find_element_by_xpath('/html/body/div/div/form[1]/div[4]/button')
    #btn.click()

    #login to venue

    time.sleep(5)

    venues = LoginToVenue(browser)
    venues.searchvenue(VENUE)

    #search_bar = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/input')
    #search_bar.send_keys(VENUE + Keys.RETURN)

    time.sleep(3)

    venues.clickLogin()

    #btn_v_login = browser.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[5]/div/button[2]')
    #assert btn_v_login.get_attribute('data-venue') == VENUE

    #btn_v_login.click()
    time.sleep(3)
    venues.clickbody()
    #body = browser.find_element_by_xpath('/html/body/div[1]/main')
    #body.click()
    #btn_v_login.send_keys(Keys.RETURN)
    time.sleep(13)

    item = CrudItem(browser)
    item.clickItem()

    #item_btn = browser.find_element_by_xpath('/html/body/div[1]/aside/div/nav/ul/li[7]/a')
    #item_btn.click()
    time.sleep(3)

    #item_item = browser.find_element_by_xpath('/html/body/div[1]/aside/div/nav/ul/li[7]/ul/li[1]/a')
    #item_item.click()
    item.clickITEM_I()
    time.sleep(8)

    #item_create = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[1]/div[2]/div[2]/button')
    #item_create.click()
    item.clickCreate()
    time.sleep(2)

    #name_item = browser.find_element_by_id('name')
    #name_item.send_keys(NAME_ITEM)
    item.NameItem(NAME_ITEM)

    item.CostItem(COST_ITEM)

    #price_item = browser.find_element_by_id('cost')
    #price_item.send_keys(COST_ITEM)
    item.TypeItem()

    #type_dropdown = browser.find_element_by_id('type')
    #type_dropdown.click()

    #type_drink = browser.find_element_by_xpath('//*[@id="type"]/option[4]')
    #type_drink.click()
    item.DrinkType()
    time.sleep(2)

    #save_item = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[2]/button[2]')
    #save_item.click()
    item.SaveItem()
    time.sleep(8)


    #search_bar = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[1]/div[2]/div[1]/div/input')
    #search_bar.send_keys(NAME_ITEM + Keys.RETURN)
    item.SearchItem(NAME_ITEM)
    time.sleep(2)
    ##UPDATE ITEM



    #item.ItemLocated(NAME_ITEM)
    result_item_search = browser.find_elements_by_css_selector('body > div.container-fluid.page-wrapper.js-wrapper > main > div.listing.js-listing > div.table-responsive > table > tbody > tr')
    #assert len(item.ItemLocated()) > 0
    # result_item_search = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/table/tbody/tr')
    # body > div.container - fluid.page - wrapper.js - wrapper > main > div.listing.js - listing > div.table - responsive > table > tbody > tr
    assert len(result_item_search) > 0

    item.ItemSearched()
    item.EditPrice()
    new_price = '20'
    item.WriteNewPrice(new_price)
    time.sleep(3)
    item.ReturnItemsList()


    ##DELETE

    time.sleep(2)
    item.clickOption()
    #options_item = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/table/tbody/tr[1]/td[7]/div[2]/span/i')
    #options_item.click()
    time.sleep(2)

    #/ html / body / div[1] / main / div[2] / div[2] / table / tbody / tr[1] / td[7] / div[2] / ul / li[2] / a
    #delete_btn = browser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/table/tbody/tr[1]/td[7]/div[2]/ul/li[2]/a')
    #delete_btn = browser.find_element_by_css_selector('body > div.container-fluid.page-wrapper.js-wrapper > main > div.listing.js-listing > div.table-responsive > table > tbody > tr:nth-child(1) > td.listing-actions > div.inline-button.dropdown.open > ul > li:nth-child(2) > a')
    #delete_btn.click()
    item.clickDelete()
    time.sleep(1)

    #confirm_delete_btn = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
    #confirm_delete_btn = browser.find_element_by_css_selector('body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-danger')
    #confirm_delete_btn.click()
    item.delete_item()
    time.sleep(3)







