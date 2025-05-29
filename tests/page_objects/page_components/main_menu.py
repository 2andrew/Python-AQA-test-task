from selenium.webdriver.common.by import By

from tests.page_objects.page_components.base_component import BaseComponent


class MainMenu(BaseComponent):
    menu_item_xpath = "//a[@id='navbarDropdownMenuLink' and normalize-space(text())='{}']"
    menu_sub_item_xpath = "//li[contains(@class, 'nav-item')]/div//a[normalize-space(text())='{}']"

    def __init__(self, driver):
        super().__init__(driver)
        self.parent_el = self.wait_for_element(By.ID, "navbarNavDropdown")

    def navigate_to(self, menu_item, menu_sub_item):
        menu_item_el = self.find_in(self.parent_el, By.XPATH, self.menu_item_xpath.format(menu_item))
        self.hover(menu_item_el)

        menu_sub_item_el = self.wait_for_visible(By.XPATH, self.menu_sub_item_xpath.format(menu_sub_item))
        menu_sub_item_el.click()
