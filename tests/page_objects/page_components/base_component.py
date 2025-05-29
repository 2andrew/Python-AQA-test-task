from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseComponent:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_for_visible(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def find_in(self, parent, by, value):
        return parent.find_element(by, value)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def hover(self, element):
        self.wait.until(lambda d: element.is_displayed() and element.size['height'] > 0 and element.size['width'] > 0)
        self.scroll_into_view(element)
        ActionChains(self.driver).move_to_element(element).perform()
