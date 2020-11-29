import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('driver/chromedriver', chrome_options=options)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    
    def test_search_in_google(self):
        driver = self.driver
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        assert "selenium" in driver.page_source

    def test_search_in_amazon(self):
        driver = self.driver
        driver.get("http://www.amazon.com.br")
        elem = driver.find_element_by_id("twotabsearchtextbox")
        elem.send_keys("monitor")
        elem.send_keys(Keys.RETURN)
        brand = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/div[3]/span/div[1]/span/div/div/div[4]/ul/li[1]/span/a/div/label/i").click()
        time.sleep(10)
        assert "LG" in driver.page_source
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()