import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from ScreenShot import screenshot


# Ex - https://drive.google.com/file/d/1cONVuyyEd9u8Z95BBjdM0tvKFoNfaFzU/view
# To run with allure:  pytest -v -s test_todo_app_allure.py --alluredir ./allure-results


class TestToDoActionsApp:
    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://todomvc.com/examples/react")
        driver.maximize_window()
        # driver.set_window_position(0, 0)
        # driver.set_window_size(1920, 1080)
        driver.implicitly_wait(3)

    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        driver.quit()

    todo_bar = driver.find_element(By.CLASS_NAME, "new-todo")
    task = driver.find_element(By.CSS_SELECTOR, "div>label[data-reactid]")

    @allure.title("TC 01 - Create assignment")
    @allure.description("Creating a new assignment")
    def test_tc01(self):
        try:
            self.step_add_assignment()
            screenshot(driver)
            self.step_check_task_exist()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            screenshot(driver)

    @allure.step("Create test task")
    def step_add_assignment(self):
        self.todo_bar.send_keys("test")

    @allure.step("Validate the task was created and named 'test'")
    def step_check_task_exist(self):
        assert self.task.text == "test"

    # @allure.title("TC 02 - Delete an assignment")
    # @allure.description("Create a new assignment and delete it")
    # def test_tc02(self):
    #     try:
    #
    #     except:
    #         pytest.fail("View screen shot")
    #
    #     finally:
    #         screenshot()
    #
    # @allure.step("")
    # def step_(self):
    #
    # @allure.step("")
    # def step_(self):
    #
    #
    #
    # @allure.title("TC 03 - Rename an assignment")
    # @allure.description("Create new assignment and rename it")
    # def test_tc02(self):
    #     try:
    #
    #     except:
    #         pytest.fail("View screen shot")
    #
    #     finally:
    #         screenshot()
    #
    # @allure.step("")
    # def step_(self):
    #
    # @allure.step("")
    # def step_(self):
    #
    #
    #
    # @allure.title("TC 04 - Mark assignment as completed")
    # @allure.description("Create new assignment and mark it as completed")
    # def test_tc02(self):
    #     try:
    #
    #     except:
    #         pytest.fail("View screen shot")
    #
    #     finally:
    #         screenshot()
    #
    # @allure.step("")
    # def step_(self):
    #
    # @allure.step("")
    # def step_(self):
    #
    #
    #
    #
    # @allure.title("TC 05 - Filter the assignment list")
    # @allure.description("Create active and completed assignments, filter the "
    #                     "assignments list to: Completed, Active and All and "
    #                     "asure relevant assignments appear")
    # def test_tc02(self):
    #     try:
    #
    #     except:
    #         pytest.fail("View screen shot")
    #
    #     finally:
    #         screenshot()
    #
    # @allure.step("")
    # def step_(self):
    #
    # @allure.step("")
    # def step_(self):
    #
    #
    #
    #
    # @allure.title("TC 06 - Clear Completed assignments list")
    # @allure.description("Create completed assignment and clear"
    #                     " the completed assignments list")
    # def test_tc02(self):
    #     try:
    #
    #     except:
    #         pytest.fail("View screen shot")
    #
    #     finally:
    #         screenshot()
    #
    # @allure.step("")
    # def step_(self):
    #
    # @allure.step("")
    # def step_(self):
