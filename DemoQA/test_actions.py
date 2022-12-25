import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestActionsChains:
    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demoqa.com/")
        driver.maximize_window()
        # driver.set_window_position(0, 0)
        # driver.set_window_size(1920, 1080)
        driver.implicitly_wait(3)

    @classmethod
    def teardown_class(cls):
        time.sleep(5)
        driver.quit()

    def test_opentab(self):
        driver.find_element(By.CSS_SELECTOR, "div.card.mt-4.top-card:nth-child(5)").click()
        droppable_menu = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(5)>div>ul>li#item-3")))
        driver.execute_script("arguments[0].click();", droppable_menu)
        action = ActionChains(driver)
        draggable = driver.find_elements(By.CSS_SELECTOR, "img")[0]
        droppable = driver.find_element(By.CSS_SELECTOR, "div.trash")
        action.drag_and_drop(draggable, droppable).perform()


    # @allure.title("Drag and drop")
    # @allure.description("This test a drag and drop in the app")
    # def test_drag_and_drop(self):
    #     try:
    #         self.step_drag_and_drop()
    #         self.step_verify_dnd()
    #     except:
    #         self.attach_file()
    #         pytest.fail("Test failed, see attached screen shot")
    #
    # @allure.step("Open drag and drop page")
    # def step_open_dnd_url(self):
    #     driver.find_element(By.XPATH,"//div/h5[text()='Interactions']"
    #                                  "/preceding-sibling::div[@class='card mt-4 top-card']").click()
    #
    # @allure.step("Drag and drop")
    # def step_drag_and_drop(self):
    #     action = ActionChains(driver)
    #     draggable = driver.find_elements(By.CSS_SELECTOR, "img")[0]
    #     droppable = driver.find_element(By.CSS_SELECTOR, "div.trash")
    #     action.drag_and_drop(draggable, droppable).perform()
    #
    # @allure.step("Verify document dropped")
    # def step_verify_dnd(self):
    #     droppable = driver.find_element(By.CSS_SELECTOR, "div.trash")
    #     assert droppable.get_attribute("class") == "trash full"
    #
    # def attach_file(self):
    #     image = "./screen-shots/screen.png"
    #     driver.get_screenshot_as_file(image)
    #     allure.attach.file(image, attachment_type=allure.attachment_type.PNG)


