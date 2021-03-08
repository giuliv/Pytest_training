import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.wait import WebDriverWait
from generics.config import TestData
from pages.crud_item import CrudItem
from pages.login import ConnectLoginPage
from pages.login_venue import LoginToVenue


@pytest.fixture
def browser():
    driver = Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login(browser):
    PHRASE = 'Login'
    VENUE = '393'

    login_page = ConnectLoginPage(browser)
    login_page.load()

    time.sleep(3)

    login_page.title_connect(TestData.TITLE)
    assert login_page.login_result_count(PHRASE) == 1, "Login button hasn't been found"
    login_page.login_to_connect(TestData.USERNAME, TestData.PWD)

    time.sleep(5)
    venues = LoginToVenue(browser)
    venues.searchvenue(TestData.VENUE)

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
def test_create_item(browser):
    test_login(browser)

    item = CrudItem(browser)
    item.clickCreate()
    time.sleep(2)

    item.NameItem(TestData.NAME_ITEM)

    item.CostItem(TestData.COST_ITEM)

    item.TypeItem()

    item.DrinkType()
    time.sleep(2)

    item.SaveItem()
    time.sleep(8)

    item.SearchItem(TestData.NAME_ITEM)
    time.sleep(2)

    ##UPDATE ITEM
def test_update_item(browser):

    test_create_item(browser)
    result_item_search = browser.find_elements_by_css_selector('body > div.container-fluid.page-wrapper.js-wrapper > main > div.listing.js-listing > div.table-responsive > table > tbody > tr')
    assert len(result_item_search) > 0, "There are no results of the searched item"

    item = CrudItem(browser)
    item.ItemSearched()
    item.EditPrice()
    new_price = '20'
    item.WriteNewPrice(new_price)
    time.sleep(3)
    item.ReturnItemsList()


    ##DELET
def test_delete_item(browser):

    test_update_item(browser)
    item = CrudItem(browser)
    time.sleep(2)
    item.clickOption()

    time.sleep(2)

    item.clickDelete()
    time.sleep(1)

    item.delete_item()
    time.sleep(3)







