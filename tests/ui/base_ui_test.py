import pytest

from tests.base_test import BaseTest


class BaseUITest(BaseTest):

    @pytest.fixture(autouse=True)
    def ui_setup(self, init_driver):
        self.driver = init_driver

        yield

        self.driver.quit()
