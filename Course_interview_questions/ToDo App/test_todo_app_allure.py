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
            self.step_check_task_appears()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            take_screenshot(driver)

    @allure.step("Create new task")
    def step_add_task(self):
        time.sleep(2)
        todo_bar = driver.find_element(By.CLASS_NAME, "new-todo")
        todo_bar.send_keys("New Task" + Keys.RETURN)

    @allure.step("Validate the task was created and named 'New Task'")
    def step_check_task_appears(self):
        task = driver.find_element(By.CSS_SELECTOR, "div>label[data-reactid]")
        assert task.text == "New Task"

    @allure.title("TC 02 - Delete a task and check the task was deleted")
    @allure.description("Create a new task and delete it")
    def test_tc02(self):
        try:
            self.step_add_task2()
            take_screenshot(driver)
            self.step_delete_task()
            self.step_check_task_delete()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            take_screenshot(driver)

    @allure.step("Create new task")
    def step_add_task2(self):
        todo_bar = driver.find_element(By.CLASS_NAME, "new-todo")
        todo_bar.send_keys("Task to delete" + Keys.RETURN)

    @allure.step("Delete 'Task to delete'")
    def step_delete_task(self):
        action = ActionChains(driver)
        task = driver.find_element(By.XPATH, "//*[text()='Task to delete']")
        action.move_to_element(task).perform()
        x_button = driver.find_elements(By.CSS_SELECTOR, "button.destroy")[1]
        x_button.click()

    @allure.step("Validate 'Task to delete' was deleted")
    def step_check_task_delete(self):
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, "//*[text()='Task to delete']")
            # Assertions about expected exceptions -
            # https://docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions

    @allure.title("TC 03 - Rename a task")
    @allure.description("Create new task and rename it")
    def test_tc03(self):
        try:
            self.step_add_task3()
            take_screenshot(driver)
            self.step_rename_task()
            self.step_validate_name_changed()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            take_screenshot(driver)

    @allure.step("Create new task")
    def step_add_task3(self):
        todo_bar = driver.find_element(By.CLASS_NAME, "new-todo")
        todo_bar.send_keys("Task to rename" + Keys.RETURN)

    @allure.step("Rename 'Task to rename' to 'Renamed Task' ")
    def step_rename_task(self):
        action = ActionChains(driver)
        task_field = driver.find_elements(By.XPATH, "//div[@class='view']/label")[1]
        action.double_click(task_field).perform()
        textfield = driver.find_elements(By.CSS_SELECTOR, "input.edit")[1]
        textfield.send_keys(Keys.BACKSPACE * 14, "Renamed Task", Keys.RETURN)

    @allure.step("Check the task title changed to 'Renamed Task'")
    def step_validate_name_changed(self):
        task_field = driver.find_elements(By.XPATH, "//div[@class='view']/label")[1]
        assert task_field.text == "Renamed Task"

    @allure.title("TC 04 - Mark task as completed")
    @allure.description("Create new task and mark it as completed")
    def test_tc04(self):
        try:
            self.step_add_task4()
            take_screenshot(driver)
            self.step_mark_task_complete()
            self.step_validate_task_in_complete_state()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            take_screenshot(driver)

    @allure.step("Create new task")
    def step_add_task4(self):
        todo_bar = driver.find_element(By.CLASS_NAME, "new-todo")
        todo_bar.send_keys("Completed Task" + Keys.RETURN)

    @allure.step("Click on the checkbox to mark the task as completed")
    def step_mark_task_complete(self):
        driver.find_elements(By.CSS_SELECTOR, "input.toggle")[2].click()

    @allure.step("Validate task marked as completed")
    def step_validate_task_in_complete_state(self):
        assert driver.find_element(By.CSS_SELECTOR, "ul.todo-list>li.completed")

    @allure.title("TC 05 - Filter the task list")
    @allure.description("Filter the tasks list to: Completed, Active and All and "
                        "check relevant tasks appear with each filter")
    def test_tc05(self):
        try:
            self.step_filter_to_active()
            self.step_validate_no_completed_tasks()
            take_screenshot(driver)
            self.step_filter_to_completed()
            self.step_validate_no_active_tasks()
            take_screenshot(driver)
            self.step_filter_to_all()
            self.step_validate_all_tasks_appear()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            take_screenshot(driver)

    @allure.step("Filter list to show only active tasks")
    def step_filter_to_active(self):
        driver.find_element(By.CSS_SELECTOR, "a[href='#/active']").click()

    @allure.step("Check only active tasks appear in the list")
    def step_validate_no_completed_tasks(self):
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CSS_SELECTOR, "ul.todo-list>li.completed")
        first_task = driver.find_elements(By.CSS_SELECTOR, "div>label[data-reactid]")[0]
        second_task = driver.find_elements(By.CSS_SELECTOR, "div>label[data-reactid]")[1]
        assert first_task.is_displayed(), second_task.is_displayed()

    @allure.step("Filter list to show only completed tasks")
    def step_filter_to_completed(self):
        driver.find_element(By.CSS_SELECTOR, "a[href='#/completed']").click()

    @allure.step("Check only completed tasks appear in the list")
    def step_validate_no_active_tasks(self):
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, "//*[text()='New task']")
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.XPATH, "//*[text()='Renamed Task']")
        assert driver.find_element(By.CSS_SELECTOR, "ul.todo-list>li.completed").is_displayed()

    @allure.step("Filter list to show all tasks")
    def step_filter_to_all(self):
        driver.find_element(By.CSS_SELECTOR, "a[href='#/']").click()

    @allure.step("Check all tasks appear in the list")
    def step_validate_all_tasks_appear(self):
        first_task = driver.find_elements(By.CSS_SELECTOR, "ul.todo-list>li")[0]
        second_task = driver.find_elements(By.CSS_SELECTOR, "ul.todo-list>li")[1]
        completed_task = driver.find_element(By.CSS_SELECTOR, "ul.todo-list>li.completed")
        assert first_task.is_displayed() and second_task.is_displayed() and completed_task.is_displayed()

    @allure.title("TC 06 - Clear Completed tasks list")
    @allure.description("Clear the completed task from the list")
    def test_tc06(self):
        try:
            take_screenshot(driver)
            self.step_clear_completed()
            self.step_validate_completed_delete()

        except Exception as error:
            print(error)
            pytest.fail("View screen shot")

        finally:
            take_screenshot(driver)

    @allure.step("Clear completed task from the list")
    def step_clear_completed(self):
        driver.find_element(By.CSS_SELECTOR, "button.clear-completed").click()

    @allure.step("Check the completed task is deleted from the list")
    def step_validate_completed_delete(self):
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CSS_SELECTOR, "ul.todo-list>li.completed")
