import allure


def take_screenshot(driver):
    image = "./screen-shots/screen.png"
    driver.get_screenshot_as_file(image)
    allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
