from BaseApp import BasePage
from selenium.webdriver.common.by import By

# class TopLocators:
#     LOCATOR = (By.CSS_SELECTOR, "")
#
# class SearchHelper(BasePage):
#
#     def click_on_button(self):
#         return self.find_element(LOCATOR, time=2).click()
#     def check_nav_bar(self):
#         all_list = self.find_elements(TopLocators.LOCATOR)
#         nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
#         return nav_bar_menu