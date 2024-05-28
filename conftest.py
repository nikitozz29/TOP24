import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()