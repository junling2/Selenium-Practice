import unittest
from selenium import webdriver
import page

PATH = r"C:\Users\Junling\bin\chromedriver.exe"
TARGET = "https://www.python.org"

class PythonOrgSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(TARGET)
    
    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_match()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()