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
from TakeScreenShot import take_screenshot

# Ex - https://drive.google.com/file/d/1Jw0W6z7PRwRc4NwonVybZY2txpkcFxoh/view
# Apllitools - visual testing
eyes = Eyes()


class TestWooLoversWeb:
    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.wooloverslondon.com/")
        driver.maximize_window()
        driver.implicitly_wait(3)
        eyes.api_key = 'rCfg7VUAMD1y9jG97L8H101bVw0yaF0RQuC2ZWo0q47pCs110'

    @classmethod
    def teardown_class(cls):
        driver.quit()
        eyes.abort()

    @allure.title("TC 01 - Change currency")
    @allure.description("Change the currency of the prices US Dollar")
    def test_change_currency(self):
        try:
            self.step_close_popups()
            self.step_change_currency()
        except Exception as error:
            print(error)
            pytest.fail()
        finally:
            take_screenshot(driver)

    @allure.step("Approve and close 2 popups")
    def step_close_popups(self):
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        driver.find_element(By.XPATH, "//input[@value='המשך לקנות']").click()

    @allure.step("Change the currency to US Dollar")
    def step_change_currency(self):
        eyes.open(driver, "Change currency", "Change currency on page to US Dollar")
        driver.find_element(By.CLASS_NAME, "font-weight-bold").click()
        eyes.check_window("Before changing the currency")
        driver.find_element(By.XPATH, "//img[@src='//gepi.global-e.com/content/images/flags/il.png']").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "glPopupContent")))
        currency = Select(driver.find_element(By.ID, "gle_selectedCurrency"))
        currency.select_by_visible_text("US Dollar")
        driver.find_element(By.XPATH, "//input[@value='שמירה']").click()
        eyes.check_window("After changing the currency")
        eyes.close()

    @allure.title("TC 02 - Change gender")
    @allure.description("Change the currency of the prices US Dollar")
    def test_change_gender(self):
        try:
            self.step_close_popups()
            self.step_change_gender()
        except Exception as error:
            print(error)
            pytest.fail()
        finally:
            take_screenshot(driver)

    @allure.step("Approve and close 2 popups")
    def step_close_popups(self):
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        driver.find_element(By.XPATH, "//input[@value='המשך לקנות']").click()

    @allure.step("Change the gender to Male")
    def step_change_gender(self):
        driver.find_element(By.CLASS_NAME, "font-weight-bold").click()
        driver.find_element(By.ID, "dd-Gender").click()
        driver.find_element(By.XPATH, "//a[@data-filter-id='161']").click()
        driver.find_element(By.XPATH, "//a[@data-filter-id='160']").click()
        driver.find_element(By.CLASS_NAME, "btn btn-block filter-group__close-btn js-toggle-close-all]").click()





