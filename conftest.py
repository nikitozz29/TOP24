import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


chrome_options = Options()
chrome_options.add_argument("--start-maximized")

firefox_options = Options()
firefox_options.add_argument("--start-maximized")


@pytest.fixture(scope="session")
def chrome():
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.close()


@pytest.fixture(scope="session")
def firefox():
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.close()
