from selenium.webdriver.common.by import By

from config import settings
from tests.page_objects.base_page import BasePage


class CareersPage(BasePage):
    URL = settings.BASE_UI_URL + "careers"
    WAIT_FOR_ELEMENTS = [(By.XPATH, "//div[@data-id='eba6aac']")]

    BLOCKS = ["Locations", "Life", "Teams", "Insider"]
    BLOCK_LOCATORS = ["//div[@data-id='38b8000']", "//div[@data-id='87842ec']",
                      "//div[@data-id='b6c45b2']", "//section[@data-id='efd8002']"]

    def __init__(self, driver):
        super().__init__(driver)

    def check_blocks_visibility(self):
        results = []

        for name, xpath in zip(self.BLOCKS, self.BLOCK_LOCATORS):
            try:
                element = self.wait_for_element(By.XPATH, xpath)
                is_visible = element.is_displayed()
            except Exception:
                is_visible = False

            results.append((name, is_visible))

        return results
