import allure
import pytest

from tests.page_objects.careers_page import CareersPage
from tests.page_objects.home_page import HomePage
from tests.page_objects.qa_careers_page import QACareersPage
from tests.ui.base_ui_test import BaseUITest


@pytest.mark.browsers("chrome,firefox")
class TestMainScenario(BaseUITest):
    menu_level_1 = "Company"
    menu_level_2 = "Careers"

    exp_page_1 = "/careers/"
    exp_subpage = "qualityassurance"

    exp_location = "Istanbul, Turkiye"
    exp_department = "Quality Assurance"

    exp_ext_url = "https://jobs.lever.co/"

    @pytest.mark.regression
    def test_home_and_career_pages(self):
        with allure.step("Open and check home page"):
            home_page = HomePage.open(self.driver)
            assert home_page.URL == self.driver.current_url, \
                f"Invalid url {self.driver.current_url}. Expected: {home_page.URL}"

        with (allure.step("Open and check Careers page")):
            home_page.navigate_to(self.menu_level_1, self.menu_level_2, self.exp_page_1)
            assert self.exp_page_1 in self.driver.current_url, \
                f"Invalid url {self.driver.current_url}. Expected: {self.exp_page_1}"

        with allure.step("Check careers page blocks"):
            careers_page = CareersPage(self.driver)
            visibility_results = careers_page.check_blocks_visibility()

            for name, is_visible in visibility_results:
                assert is_visible, f"Block '{name}' is not visible"

    @pytest.mark.regression
    def test_qa_careers_pages(self):
        with allure.step("Open and check qa careers page"):
            qa_careers_page = QACareersPage.open(self.driver)
            assert qa_careers_page.URL == self.driver.current_url, \
                f"Invalid url {qa_careers_page.URL}. Expected: {self.driver.current_url}"

            open_positions_page = qa_careers_page.see_all_jobs()
            assert self.driver.current_url.startswith(open_positions_page.URL.format(self.exp_subpage)), \
                f"Invalid url {self.driver.current_url}. Expected: {open_positions_page.URL.format(self.exp_subpage)}"

            assert open_positions_page.select_location(self.exp_location) == self.exp_location, \
                "Location is not chosen or dropdown has wrong value"
            assert open_positions_page.select_department(self.exp_department) == self.exp_department, \
                "Department is not chosen or dropdown has wrong value"

            assert open_positions_page.is_job_list_visible(), \
                "Job list is not visible"

        with (allure.step("Check job list")):
            jobs_list = open_positions_page.get_all_jobs()
            for pos, loc in jobs_list:
                assert self.exp_department in pos and self.exp_location in loc, \
                    f"Block '{pos} - {loc}' doesn't match expected ones: {self.exp_department} - {self.exp_location}"

        with (allure.step("Check View Role button")):
            open_positions_page.click_view_role(self.exp_ext_url)
            assert self.driver.current_url.startswith(self.exp_ext_url), \
                f"Invalid url {self.driver.current_url}. Expected: {self.driver.exp_ext_url}"
