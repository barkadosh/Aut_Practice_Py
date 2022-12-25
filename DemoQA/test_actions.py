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
import SaveScreenShot


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

    @allure.title("TC01 - Drag and drop")
    @allure.description("This test a drag and drop in the app")
    def test_drag_and_drop(self):
        try:
            self.step_go_to_dnd_app()
            self.step_drag_and_drop()
            self.step_verify_dnd()
        except:
            SaveScreenShot.attach_file(self)
            pytest.fail("Test failed, see attached screen shot")

    @allure.step("Step1-Open drag and drop page")
    def step_go_to_dnd_app(self):
        driver.find_element(By.CSS_SELECTOR, "div.card.mt-4.top-card:nth-child(5)").click()
        droppable_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(5)>div>ul>li#item-3")))
        driver.execute_script("arguments[0].click();", droppable_menu)

    @allure.step("Step2-Drag and drop")
    def step_drag_and_drop(self):
        action = ActionChains(driver)
        draggable = driver.find_element(By.ID, "draggable")
        droppable = driver.find_element(By.ID, "droppable")
        action.drag_and_drop(draggable, droppable).perform()

    @allure.step("Step3-Verify document dropped")
    def step_verify_dnd(self):
        droppable = driver.find_element(By.XPATH, "//div[@class='drop-box ui-droppable ui-state-highlight']/p")
        assert droppable.text == "Dropped!"
    #
    # def attach_file(self):
    #     image = "./screen-shots/screen.png"
    #     driver.get_screenshot_as_file(image)
    #     allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
