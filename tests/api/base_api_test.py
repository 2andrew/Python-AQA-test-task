import time

import pytest

from tests.base_test import BaseTest
from tests.models.api_models import Pet
from tests.requests.checked_crud_request import CheckedRequest
from tests.requests.endpoints import Endpoint
from tests.requests.unchecked_crud_request import UncheckedRequest
from tests.util.test_data_generator import TestDataGenerator
from tests.util.test_data_storage import TstDataStorage


class BaseApiTest(BaseTest):

    @pytest.fixture(autouse=True)
    def api_setup(self):
        self.fake_pet = TestDataGenerator().generate_fake_model(Pet)

        # usually this kind of variable is specified in test, but we're testing CRUD only for 1 entity, so let's simplify
        self.pet_request = CheckedRequest(Endpoint.PET.url)
        self.unchecked_pet_request = UncheckedRequest(Endpoint.PET.url)

        yield
        TstDataStorage.get_storage().delete_created_entities()

    def retry_on_404(self, func, max_attempts=5, delay=2, *args, **kwargs):
        for attempt in range(1, max_attempts + 1):
            response = func(*args, **kwargs)
            if response.status_code != 404:
                return response
            print(f"[Retry {attempt}] Received 404. Retrying in {delay}s...")
            time.sleep(delay)
        return response
