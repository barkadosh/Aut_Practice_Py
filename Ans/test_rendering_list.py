import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestAutocomplete:
    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.walmart.com/cp/food/976759")
        driver.maximize_window()
        driver.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_rendering_list(self):
        search_bar = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_bar.send_keys("b")
        time.sleep(3)
        product1 = driver.find_elements(By.CSS_SELECTOR, "span.b.lh-title")[0].text
        print(product1)
        assert product1.__contains__("b")
        search_bar.send_keys("anana")
        time.sleep(5)
        product2 = driver.find_elements(By.CSS_SELECTOR, "span.b.lh-title")[0].text
        print(product2)
        assert product2.__contains__("banana")
        assert product1 != product2
        #search_bar.clear()     # not always works - can do refresh either, the site blocks automation
        driver.find_elements(By.CSS_SELECTOR, "i.ld.ld-Close")[1].click()
        time.sleep(3)
        search_bar.send_keys("b")
        product3 = driver.find_elements(By.CSS_SELECTOR, "span.b.lh-title")[0].text
        print(product3)
        assert product1 == product3




