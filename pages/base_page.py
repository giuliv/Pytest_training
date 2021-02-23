class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def get_element(self, element):
        return self.browser.find_element(*element)

    def get_elements(self, element):
        return self.browser.find_elements(*element)

    def click_on_element(self, element):
        self.get_element(element).click()

    def click_on_element_dd(self, element):
        self.get_element(*element).click()

    def type_on_element(self, element, value):
        elem = self.get_element(element)
        elem.clear()
        elem.send_keys(value)