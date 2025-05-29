from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from tests.page_objects.page_components.base_component import BaseComponent
from tests.page_objects.page_components.cookie_banner import CookieBanner


class BasePage(BaseComponent):
    URL = None
    WAIT_FOR_ELEMENTS = []

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(self.driver)

    @classmethod
    def open(cls, driver):
        driver.get(cls.URL)
        page = cls(driver)
        page.wait_for_page_loaded()
        cookie_banner = CookieBanner(driver)
        if cookie_banner.is_visible():
            cookie_banner.accept()
        return page

    def wait_for_page_loaded(self):
        for by, locator in self.WAIT_FOR_ELEMENTS:
            self.wait_for_visible(by, locator)

    def wait_for_more_than_x_options(self, select_locator, min_options=1):
        def _condition(driver):
            select_element = driver.find_element(*select_locator)
            options = select_element.find_elements(By.TAG_NAME, "option")
            return len(options) > min_options

        return self.wait.until(_condition)

    def wait_till_url_equals(self, url):
        self.wait.until(EC.url_to_be(url))

    def wait_till_url_contains(self, part):
        self.wait.until(EC.url_contains(part))

    def wait_till_url_starts(self, val):
        def _condition(driver):
            return driver.current_url.startswith(val)

        self.wait.until(_condition)

    def normalize_text(self, text):
        new_text = text.replace("\n", "")
        new_text = new_text.replace("×", "")
        return new_text

    def select_dr_value(self, text, select_locator, dropdown_locator):
        self.wait_for_more_than_x_options(select_locator)
        _el = self.driver.find_element(*select_locator)
        try:
            select_element = Select(_el)
            select_element.select_by_visible_text(text)
            return select_element.first_selected_option.get_attribute("value")
        except:  # select is not clickable in Firefox due to some reasons
            self.driver.find_element(*dropdown_locator).click()
            self.driver.find_element(By.XPATH, f"//li[text()='{text}']").click()
            return self.normalize_text(self.driver.find_element(*dropdown_locator).text)
