import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.fixture(scope="session")
def firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.close()
