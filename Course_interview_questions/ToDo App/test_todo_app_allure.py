import sys

import allure
import pytest
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from TakeScreenShot import take_screenshot


# Ex - https://drive.google.com/file/d/1cONVuyyEd9u8Z95BBjdM0tvKFoNfaFzU/view
# To run with allure:  python -m pytest -v -s test_todo_app_allure.py --alluredir ./allure-results


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

    @allure.title("TC 01 - Create assignment")
    @allure.description("Creating a new assignment")
    def test_tc01(self):
        try:
            self.step_add_task()
            self.step_check_task_exist()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            take_screenshot(driver)

    @allure.step("Create test task")
    def step_add_task(self):
        todo_bar = driver.find_element(By.CLASS_NAME, "new-todo")
        todo_bar.send_keys("test" + Keys.RETURN)

    @allure.step("Validate the task was created and named 'test'")
    def step_check_task_exist(self):
        task = driver.find_element(By.CSS_SELECTOR, "div>label[data-reactid]")
        assert task.text == "test"

    @pytest.mark.xfail
    @allure.title("TC 02-A - Delete a task and check the task was deleted -fail")
    @allure.description("Create a new task and delete it")
    def test_tc02(self):
        try:
            self.step_add_task2()
            self.step_delete_task()
            self.step_check_task_delete()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            take_screenshot(driver)

    @allure.step("Create test2 task")
    def step_add_task2(self):
        todo_bar = driver.find_element(By.CLASS_NAME, "new-todo")
        todo_bar.send_keys("test2" + Keys.RETURN)

    @allure.step("Delete test")
    def step_delete_task(self):
        action = ActionChains(driver)
        task = driver.find_element(By.CSS_SELECTOR, ".view")
        action.move_to_element(task).perform()
        x_button = driver.find_element(By.CSS_SELECTOR, "button.destroy")
        x_button.click()

    @allure.step("Validate test2 was deleted")
    def step_check_task_delete(self):
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, "//*[text()='test2']")
            # Assertions about expected exceptions -
            # https://docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions

    @allure.title("TC 02-B - Delete a task and check the task was deleted -Success")
    @allure.description("Create a new task and delete it")
    def test_tc02(self):
        try:
            self.step_add_task2()
            self.step_delete_task()
            self.step_check_task_delete()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            take_screenshot(driver)

    @allure.step("Create test3 task")
    def step_add_task2(self):
        todo_bar = driver.find_element(By.CLASS_NAME, "new-todo")
        todo_bar.send_keys("test3" + Keys.RETURN)

    @allure.step("Delete test3")
    def step_delete_task(self):
        action = ActionChains(driver)
        task = driver.find_elements(By.CSS_SELECTOR, ".view")[1]
        action.move_to_element(task).perform()
        x_button = driver.find_element(By.CSS_SELECTOR, "button.destroy")
        x_button.click()

    @allure.step("Validate the test3 task was deleted")
    def step_check_task_delete(self):
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, "//*[text()='test3']")


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
