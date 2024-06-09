from BaseApp import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    LOCATOR_CLOSE_CITY = (By.CSS_SELECTOR, "#on_geocity > button")
    LOCATOR_NAV_BAR = (By.ID, "menu-header")
    LOCATOR_CITY_SELECT_BUTTON = (By.CLASS_NAME, "cityselect")
    LOCATOR_CITYES = (By.CSS_SELECTOR, "ul.cityselect__options")
    LOCATOR_KOSTROMA = (By.XPATH, "/html/body/div[1]/div/div/header/div[1]/div[4]/div/div/div[2]/ul/li[3]/a")
    # LOCATOR_KOSTROMA = (By.CSS_SELECTOR, ".cityselect__optwrapper li")

    def check_on_close_button(self):
        return self.find_element(MainPage.LOCATOR_CLOSE_CITY)

    def click_on_city_select(self):
        return self.find_element(MainPage.LOCATOR_CITY_SELECT_BUTTON).click()

    def check_nav_bar(self):
        bar_list = self.find_elements(MainPage.LOCATOR_NAV_BAR)
        nav_bar_menu = []
        for i in bar_list:
            nav_bar_menu.append(i.text)
        # nav_bar_menu = [x.text for x in bar_list if len(x.text) > 0]
        return nav_bar_menu


    def check_cityes(self):
        all_list = self.find_elements(MainPage.LOCATOR_CITYES)
        cityes_menu = [x.text for x in all_list]
        return cityes_menu

    def check_kostroma_page(self):
        return self.find_element(MainPage.LOCATOR_KOSTROMA)


    # def click_on_button(self):
    #     return self.find_element(LOCATOR, time=2).click()
    # def check_nav_bar(self):
    #     all_list = self.find_elements(TopLocators.LOCATOR)
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     return nav_bar_menu
