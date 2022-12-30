import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Ex - https://drive.google.com/file/d/1cONVuyyEd9u8Z95BBjdM0tvKFoNfaFzU/view

def screenshot():
    image = "./screen-shots/screen.png"
    driver.get_screenshot_as_file(image)
    allure.attach.file(image, attachment_type=allure.attachment_type.PNG)


class TestToDoActionsApp:
    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://todomvc.com/examples/react/#/completed")
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

    except:
        pytest.fail("View screen shot")

    finally:
        screenshot()

@allure.step("")
def step_(self):


@allure.step("")
def step_(self):


@allure.title("TC 02 - Delete an assignment")
@allure.description("Create a new assignment and delete it")
def test_tc02(self):
    try:

    except:
        pytest.fail("View screen shot")

    finally:
        screenshot()

@allure.step("")
def step_(self):

@allure.step("")
def step_(self):



@allure.title("TC 03 - Rename an assignment")
@allure.description("Create new assignment and rename it")
def test_tc02(self):
    try:

    except:
        pytest.fail("View screen shot")

    finally:
        screenshot()

@allure.step("")
def step_(self):

@allure.step("")
def step_(self):



@allure.title("TC 04 - Mark assignment as completed")
@allure.description("Create new assignment and mark it as completed")
def test_tc02(self):
    try:

    except:
        pytest.fail("View screen shot")

    finally:
        screenshot()

@allure.step("")
def step_(self):

@allure.step("")
def step_(self):




@allure.title("TC 05 - Filter the assignment list")
@allure.description("Create active and completed assignments, filter the "
                    "assignments list to: Completed, Active and All and "
                    "asure relevant assignments appear")
def test_tc02(self):
    try:

    except:
        pytest.fail("View screen shot")

    finally:
        screenshot()

@allure.step("")
def step_(self):

@allure.step("")
def step_(self):




@allure.title("TC 06 - Clear Completed assignments list")
@allure.description("Create completed assignment and clear"
                    " the completed assignments list")
def test_tc02(self):
    try:

    except:
        pytest.fail("View screen shot")

    finally:
        screenshot()

@allure.step("")
def step_(self):

@allure.step("")
def step_(self):