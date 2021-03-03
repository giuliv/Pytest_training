import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
import logging

from selenium.webdriver.support.wait import WebDriverWait

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
    URL = 'https://connect.sandbox.appetize-dev.com/login'
    USERNAME = 'qaregressionteam'
    PWD = '@ppetiz3!'
    PHRASE = 'Login'
    VENUE = '393'
    NAME_ITEM = 'autogiuli'
    COST_ITEM = '11'
    TYPE_ITEM = 'drink'
    TITLE_PAGE = (By.XPATH, '/html/head/')
    TITLE = 'Appetize Connect - Login'
    TITLE1 = 'Appetize Connect - Login'
    VENUE_SEARCH_BAR = (By.XPATH, '/html/body/div[1]/main/div[2]/div/input')

    login_page = ConnectLoginPage(browser)
    login_page.load()

    time.sleep(3)

    login_page.title_connect(TITLE)
    assert login_page.login_result_count(PHRASE) == 1, "Login button hasn't been found"
    login_page.writeuser(USERNAME)


    pwd_input = browser.find_element_by_id('password')
    pwd_input.send_keys(PWD + Keys.RETURN)
    pwd_input.send_keys(Keys.RETURN)

    login_page.writepassword(PWD)
    login_page.pressloginbtn()

    #login to venue

    time.sleep(5)
    venues = LoginToVenue(browser)
    venues.searchvenue(VENUE)

    time.sleep(3)

    venues.clickLogin()

    time.sleep(3)
    venues.clickbody()
    my_venue = WebDriverWait(browser, 16).until(EC.presence_of_all_elements_located(('id', 'stat-avg_order_size')))
    print('Esperando explicitamente')

    item = CrudItem(browser)
    item.clickItem()

    time.sleep(3)

    item.clickITEM_I()
    time.sleep(8)

    #CREATE ITEM

    item.clickCreate()
    time.sleep(2)

    item.NameItem(NAME_ITEM)

    item.CostItem(COST_ITEM)

    item.TypeItem()

    item.DrinkType()
    time.sleep(2)

    item.SaveItem()
    time.sleep(8)


    item.SearchItem(NAME_ITEM)
    time.sleep(2)

    ##UPDATE ITEM

    result_item_search = browser.find_elements_by_css_selector('body > div.container-fluid.page-wrapper.js-wrapper > main > div.listing.js-listing > div.table-responsive > table > tbody > tr')
    assert len(result_item_search) > 0, "There are no results of the searched item"

    item.ItemSearched()
    item.EditPrice()
    new_price = '20'
    item.WriteNewPrice(new_price)
    time.sleep(3)
    item.ReturnItemsList()


    ##DELETE

    time.sleep(2)
    item.clickOption()

    time.sleep(2)

    item.clickDelete()
    time.sleep(1)

    item.delete_item()
    time.sleep(3)







