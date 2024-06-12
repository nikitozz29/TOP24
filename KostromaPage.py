from BaseApp import BasePage
from selenium.webdriver.common.by import By


class KostromaPage(BasePage):
    LOCATOR_CLOSE_CITY = (By.CSS_SELECTOR, "#on_geocity > button")
    LOCATOR_CLOSE_TELEGRAMM_BUTTON = (By.CLASS_NAME, "fixtg__close")
    LOCATOR_NAV_BAR = (By.ID, "menu-header")

    def check_on_close_button(self):
        return self.find_element(KostromaPage.LOCATOR_CLOSE_CITY)

    def check_on_tg_close(self):
        return self.find_element(KostromaPage.LOCATOR_CLOSE_TELEGRAMM_BUTTON)

    def check_nav_bar(self):
        bar_list = self.find_elements(KostromaPage.LOCATOR_NAV_BAR)
        nav_bar_menu = [x.text for x in bar_list]
        return nav_bar_menu
