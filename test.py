# Import the 'modules' that are required for execution

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

global url_under_test


# We make use of the parameterized decorator to supply input arguments
# to the test function


@pytest.mark.parametrize("input_browser", ['chrome', 'firefox'])
@pytest.mark.parametrize("input_url", ['https://lambdatest.github.io/sample-todo-app/'])

def test_url_on_browsers(input_browser, input_url):
    global driver
    if input_browser == "chrome":
        driver = webdriver.Chrome()
    if input_browser == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(input_url)
    print(driver.title)
    sleep(5)

    # Click on check box
    check_box_one = driver.find_element(By.NAME, "li1")
    check_box_one.click()

    # Click on check box
    check_box_two = driver.find_element(By.NAME, "li2")
    check_box_two.click()

    # Enter item in textfield
    textfield = driver.find_element(By.ID, "sampletodotext")
    textfield.send_keys("Yey, Let's add it to list")

    # Click on add button
    add_button = driver.find_element(By.ID, "addbutton")
    add_button.click()

    # Verified added item

    added_item = driver.find_element(By.XPATH, "//span[@class='done-false']").text

    print(added_item)

    sleep(5)

    driver.close()
