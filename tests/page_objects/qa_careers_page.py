from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config import settings
from tests.page_objects.base_page import BasePage
from tests.page_objects.open_positions_page import OpenPositionsPage


class QACareersPage(BasePage):
    URL = settings.BASE_UI_URL + "careers/quality-assurance/"
    WAIT_FOR_ELEMENTS = [(By.XPATH, "//div[@data-id='f659aaa']")]

    ALL_JOBS_BUTTON = (By.XPATH, "//a[normalize-space(text())='See all QA jobs']")

    EXP_SUBPAGE = "qualityassurance"

    def __init__(self, driver):
        super().__init__(driver)

    def see_all_jobs(self):
        self.wait_for_visible(*self.ALL_JOBS_BUTTON)

        button = self.driver.find_element(*self.ALL_JOBS_BUTTON)
        self.wait.until(EC.element_to_be_clickable(self.ALL_JOBS_BUTTON))
        button.click()

        open_positions_page = OpenPositionsPage(self.driver)
        self.wait_till_url_contains(open_positions_page.URL.format(self.EXP_SUBPAGE))
        return open_positions_page
