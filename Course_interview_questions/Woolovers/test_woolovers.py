import allure
import time
import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Ex - https://drive.google.com/file/d/1Jw0W6z7PRwRc4NwonVybZY2txpkcFxoh/view
# Apllitools - visual testing - taking screenshots after changes, comparing the changes with past runs
eyes = Eyes()


class TestWooLoversWeb:
    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.wooloverslondon.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        #eyes.api_key =

    @classmethod
    def teardown_class(cls):
        driver.quit()
        #eyes.abort()

    @allure.title("TC 01 - Change filters")
    @allure.description("Change the currency to $, gender to male and price range from low to high")
    def test_change_filters(self):
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        driver.find_element(By.XPATH, "//input[@type='button']").click()
        eyes.open(driver, "Change filters", "Change the currency to $, gender to male and price range from low to high")
        driver.find_element(By.XPATH, "//a[@class='font-weight-bold']").click()
        eyes.check_window("Before changing the currency")
        driver.find_element(By.XPATH, "//img[@src='//gepi.global-e.com/content/images/flags/il.png']").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "glPopupContent")))
        currency = Select(driver.find_element(By.ID, "gle_selectedCurrency"))
        currency.select_by_visible_text("US Dollar")
        driver.find_element(By.XPATH, "//input[@data-key='SavenClose']").click()
        eyes.check_window("After changing the currency, Before changing the gender")
        driver.find_element(By.ID, "dd-Gender").click()
        driver.find_element(By.CSS_SELECTOR, "div.d-lg-flex.filter-group__scroll>a[data-filter-id='161']").click()
        driver.find_element(By.CSS_SELECTOR, "div.d-lg-flex.filter-group__scroll>a[data-filter-id='160']").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "div.filter-group__close-all.hidden-xs.hidden-sm").click()
        eyes.check_window("After changing the gender, Before changing price range")
        driver.find_element(By.ID, "dd-Sort By").click()
        driver.find_element(By.CSS_SELECTOR, "div.d-lg-flex.filter-group__scroll>a[data-filter-id='0']").click()
        driver.find_element(By.CSS_SELECTOR, "div.d-lg-flex.filter-group__scroll>a["
                                             "href='?f=t&filtered&sortby=1&gender=161,&show=24&category=0']").click()
        driver.find_elements(By.XPATH, "//div[text()='Done']")[15].click()
        eyes.check_window("After changing price range from low to high")
        eyes.close()

    @allure.title("TC 01 - Verify Price")
    @allure.description("Verify the price of the products in the store are lower than 150$")
    def test_verify_price(self):
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        driver.find_element(By.XPATH, "//input[@type='button']").click()
        driver.find_element(By.XPATH, "//a[@class='font-weight-bold']").click()
        driver.find_element(By.XPATH, "//img[@src='//gepi.global-e.com/content/images/flags/il.png']").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "glPopupContent")))
        currency = Select(driver.find_element(By.ID, "gle_selectedCurrency"))
        currency.select_by_visible_text("US Dollar")
        driver.find_element(By.XPATH, "//input[@data-key='SavenClose']").click()
        time.sleep(1)
        driver.find_element(By.ID, "dd-Gender").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div.d-lg-flex.filter-group__scroll>a[data-filter-id='161']").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "div.d-lg-flex.filter-group__scroll>a[data-filter-id='160']").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "div.filter-group__close-all.hidden-xs.hidden-sm").click()
        driver.find_element(By.ID, "dd-Sort By").click()
        driver.find_element(By.CSS_SELECTOR, "div.d-lg-flex.filter-group__scroll>a[data-filter-id='0']").click()
        driver.find_element(By.CSS_SELECTOR, "div.d-lg-flex.filter-group__scroll>a["
                                             "href='?f=t&filtered&sortby=1&gender=161,&show=24&category=0']").click()
        driver.find_elements(By.XPATH, "//div[text()='Done']")[15].click()
        product_price = driver.find_elements(By.CSS_SELECTOR, "div.container.products-container span.pricing__price.pricing__price--new:last-of-type")[1]
        print(product_price.text)


