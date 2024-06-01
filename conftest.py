import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
