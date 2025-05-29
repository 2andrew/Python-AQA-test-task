from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config import settings
from tests.page_objects.base_page import BasePage


class OpenPositionsPage(BasePage):
    URL = settings.BASE_UI_URL + "careers/open-positions/?department={}"

    LOCATION_DR = (By.ID, "filter-by-location")
    LOCATION_DR_CONTAINER = (By.ID, "select2-filter-by-location-container")
    DEPARTMENT_DR = (By.ID, "filter-by-department")
    DEPARTMENT_DR_CONTAINER = (By.ID, "select2-filter-by-department-container")

    JOB_LIST_CONTAINER = (By.ID, "jobs-list")
    VIEW_ROLE_BTN = (By.XPATH, '//a[contains(text(),"View Role")]')
    CARD_ITEM = (By.CSS_SELECTOR, "#jobs-list .position-list-item")
    POSITION_TITLE_LOC = (By.CSS_SELECTOR, ".position-title")
    POSITION_LOCATION_LOC = (By.CSS_SELECTOR, ".position-location")

    WAIT_FOR_ELEMENTS = [(By.CLASS_NAME, ".career-open-position"), JOB_LIST_CONTAINER]

    def __init__(self, driver):
        super().__init__(driver)

    def select_location(self, text):
        return self.select_dr_value(text, self.LOCATION_DR, self.LOCATION_DR_CONTAINER)

    def select_department(self, text):
        return self.select_dr_value(text, self.DEPARTMENT_DR, self.DEPARTMENT_DR_CONTAINER)

    def is_job_list_visible(self):
        element = self.wait_for_visible(*self.JOB_LIST_CONTAINER)
        return element.is_displayed()

    def get_all_jobs(self):
        self.wait.until(EC.presence_of_all_elements_located(self.CARD_ITEM))

        # ideally we need proper waiting for network request to be finished, or UI condition, but it would be complex
        # simplifying it for now, but generally it's a bad practice
        sleep(5)

        job_items = self.driver.find_elements(*self.CARD_ITEM)
        job_pairs = []

        for item in job_items:
            title = item.find_element(*self.POSITION_TITLE_LOC)
            department = item.find_element(*self.POSITION_LOCATION_LOC)

            job_pairs.append((title.text, department.text))

        return job_pairs

    def click_view_role(self, exp_url, idx=0):
        job_items = self.driver.find_elements(*self.CARD_ITEM)

        original_window = self.driver.current_window_handle

        self.scroll_into_view(job_items[idx])
        self.actions.move_to_element(job_items[idx]).perform()

        _button = job_items[idx].find_element(*self.VIEW_ROLE_BTN)
        self.scroll_into_view(_button)
        _button.click()

        self.wait.until(lambda d: len(d.window_handles) == 2)

        new_window = [h for h in self.driver.window_handles if h != original_window][0]
        self.driver.switch_to.window(new_window)

        self.wait_till_url_starts(exp_url)
