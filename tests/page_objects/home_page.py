from selenium.webdriver.common.by import By

from config import settings
from tests.page_objects.base_page import BasePage
from tests.page_objects.page_components.main_menu import MainMenu


class HomePage(BasePage):
    URL = settings.BASE_UI_URL
    WAIT_FOR_ELEMENTS = [(By.CLASS_NAME, "HeroContentContainer")]

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to(self, menu_item, menu_sub_item, exp_page):
        MainMenu(self.driver).navigate_to(menu_item, menu_sub_item)
        self.wait_till_url_contains(exp_page)
