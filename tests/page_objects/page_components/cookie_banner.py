from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.page_objects.page_components.base_component import BaseComponent


class CookieBanner(BaseComponent):
    TIMEOUT = 3
    container_locator = (By.ID, "cookie-law-info-bar")
    accept_btn_locator = (By.ID, "wt-cli-accept-all-btn")
    decline_btn_locator = (By.ID, "wt-cli-reject-btn")

    def __init__(self, driver):
        super().__init__(driver)
        # using custom wait because we need to handle the banner just once (when session started)
        self.custom_wait = WebDriverWait(self.driver, 3)

    def is_visible(self):
        print("checking cookie banner")
        try:
            element = self.custom_wait.until(EC.presence_of_element_located(self.container_locator))
            return element.is_displayed()
        except Exception as e:
            print(e)
            return False

    def click_button(self, locator):
        self.custom_wait.until(EC.presence_of_element_located(locator))
        _button = self.driver.find_element(*self.accept_btn_locator)
        _button.click()

    def accept(self):
        print("accepting cookie banner")
        self.click_button(self.accept_btn_locator)

    def decline(self):
        print("declining cookie banner")
        self.click_button(self.decline_btn_locator)
