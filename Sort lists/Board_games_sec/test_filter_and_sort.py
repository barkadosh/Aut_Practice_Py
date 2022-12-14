import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
import xml.etree.ElementTree as ET
#https://docs.python.org/3/library/xml.etree.elementtree.html
#from my_event_listener import EventListener


class TestSortBoardGames:
    @classmethod
    def setup_class(cls):
        global driver
        #edriver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = EventFiringWebDriver(edriver, EventListener())
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.miniaturemarket.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_sort_boardgames(self):
        # Click on Board Games
        driver.find_element(By.XPATH, "//a[@href='https://www.miniaturemarket.com/board-games.html']").click()
        # Accept cookies
        cookies = driver.find_element(By.CSS_SELECTOR, "button#onetrust-accept-btn-handler")
        cookies.click()
        # Filter by Age
        driver.find_element(By.PARTIAL_LINK_TEXT, "3 and up").click()
        # Sort by lowest price
        driver.find_element(By.CSS_SELECTOR, ".sort-mode.control-set").click()
        driver.find_element(By.CSS_SELECTOR, "[title='Price ($ - $$$)']").click()
        # Get price on first product
        product_1 = \
        driver.find_elements(By.XPATH, "//span[text()='Our Price:']/following-sibling::span[@class='price']")[0].text
        # Get price on second product
        product_2 = \
        driver.find_elements(By.XPATH, "//span[text()='Our Price:']/following-sibling::span[@class='price']")[1].text

        # Check the first price is lower than the second price
        assert float(product_1.replace('$', '')) <= float(product_2.replace('$', ''))

    def test_fail_check_lowest_prices(self):
        try:
            # Click on Board Games
            driver.find_element(By.XPATH, "//a[@href='https://www.miniaturemarket.com/board-games.html']").click()
            # Accept cookies
            cookies = driver.find_element(By.CSS_SELECTOR, "button#onetrust-accept-btn-handler")
            cookies.click()
            # Filter by Age
            driver.find_element(By.PARTIAL_LINK_TEXT, "3 and up").click()
            # Sort by lowest price
            driver.find_element(By.CSS_SELECTOR, ".sort-mode.control-set").click()
            driver.find_element(By.CSS_SELECTOR, "[title='Price ($ - $$$)']").click()
            # Get price on first product
            product_1 = \
                driver.find_elements(By.XPATH, "//span[text()='Our Price:']/following-sibling::span[@class='price']")[
                    0].text
            # Check if element is the lowest value
            assert product_1 == "$4.49"
            print("Test passed")

        except Exception as e:
            print("Test Failed, see error", str(e))
            pytest.fail()


def get_data(node_name):
    root = ET.parse('./Congif.xml').getroot()
    return root.find(".//" + node_name).text


class TestFromFile:
    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(get_data('Url'))
        driver.maximize_window()
        driver.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_fail_check_lowest_price_from_a_file(self):
        driver.find_element(By.XPATH, "//a[@href='https://www.miniaturemarket.com/board-games.html']").click()
        cookies = driver.find_element(By.CSS_SELECTOR, "button#onetrust-accept-btn-handler")
        cookies.click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "3 and up").click()
        driver.find_element(By.CSS_SELECTOR, ".sort-mode.control-set").click()
        driver.find_element(By.CSS_SELECTOR, "[title='Price ($ - $$$)']").click()
        product_1 = \
            driver.find_elements(By.XPATH, "//span[text()='Our Price:']/following-sibling::span[@class='price']")[
                0].text

        assert product_1 == get_data('Expected_min_price')

