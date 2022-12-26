import time

import allure
import pytest
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
        # driver.get("https://demoqa.com/")
        driver.maximize_window()
        # driver.set_window_position(0, 0)
        # driver.set_window_size(1920, 1080)
        # driver.implicitly_wait(3)

    @classmethod
    def teardown_class(cls):
        driver.quit()

    @allure.title("TC01 - Drag and drop")
    @allure.description("This TC test a drag and drop in the app")
    def test_drag_and_drop(self):
        try:
            self.step_go_to_dnd_app()
            self.step_drag_and_drop()
            self.step_verify_dnd()
        except:
            pytest.fail("Test failed, see attached screen shot")
        finally:
            self.attach_file()

    @allure.step("Step1-Open drag and drop page")
    def step_go_to_dnd_app(self):
        driver.get("https://demoqa.com/droppable")
        driver.set_page_load_timeout(3)
        # driver.find_element(By.CSS_SELECTOR, "div.card.mt-4.top-card:nth-child(5)").click()
        # droppable_menu = WebDriverWait(driver, 5).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(5)>div>ul>li#item-3")))
        # driver.execute_script("arguments[0].click();", droppable_menu)
        driver.execute_script("document.getElementById('adplus-anchor').style.display = 'none';")
        driver.execute_script("document.getElementById('RightSide_Advertisement').style.display = 'none';")
        # Remove google ad that was interrupting

    @allure.step("Step2-Drag and drop")
    def step_drag_and_drop(self):
        action = ActionChains(driver)
        draggable = driver.find_element(By.ID, "draggable")
        droppable = driver.find_element(By.ID, "droppable")
        action.drag_and_drop(draggable, droppable).perform()
        time.sleep(5)

    @allure.step("Step3-Verify document dropped")
    def step_verify_dnd(self):
        droppable = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='drop-box ui-droppable ui-state-highlight']/p")))

        assert droppable.text == "Dropped!"

    def attach_file(self):
        image = "./screen-shots/screen.png"
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("TC02 - Select multiple")
    @allure.description("This TC test a multi select in a menu")
    def test_multy_select(self):
        try:
            self.step_go_to_multy_select()
            self.step_select_multiple_choices()
        except:
            pytest.fail("Test failed, see attached screen shot")
        finally:
            self.attach_file()

    @allure.step("Step1- Navigate to multy select menu")
    def step_go_to_multy_select(self):
        driver.get("https://demoqa.com/select-menu")
        driver.set_page_load_timeout(2)
        #driver.execute_script("document.getElementById('adplus-anchor').style.display = 'none';")

    @allure.step("Step2- Select 2 boxes")
    def step_select_multiple_choices(self):
        driver.execute_script("scrollTo(700,400)")
        action = ActionChains(driver)
        list1 = driver.find_elements(By.XPATH, "//select[@name='cars']/option")
        action.click_and_hold(list1[0]).click_and_hold(list1[1]).click().perform()




        #double click
        # dclick = driver.find_element("div:nth-child(4)>div>ul>li#item-8")
        # action.double_click(dclick).perform()
    #
    #     # right click
    #
    #     image = driver.find_element()
    #     action.context_click(image).perform()
