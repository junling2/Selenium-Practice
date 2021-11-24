from locator import *
from element import *

class SearchTextElement(BasePageElement):
    locator = "q"

class BasePage():

    def __init__(self, driver) -> None:
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_match(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocator.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found" not in self.driver.page_source