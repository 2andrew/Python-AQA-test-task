import allure
import pytest

from tests.api.base_api_test import BaseApiTest
from tests.models.api_models import Pet


class TestPetGetReq(BaseApiTest):

    @pytest.mark.positive
    def test_find_pet_by_id(self):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        with allure.step("Read Pet"):
            # Using retry because Petstore randomly return 404
            resp = self.retry_on_404(self.unchecked_pet_request.read, max_attempts=5, delay=2, locator=self.fake_pet.id)
            assert resp.status_code == 200, \
                f"Invalid status code: {resp.status_code}. Expected: 200"

            pet = Pet.model_validate(resp.json())
            assert self.fake_pet == pet, \
                f"Pet entity body is invalid"

    @pytest.mark.negative
    def test_find_pet_by_non_exist_id(self):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        with allure.step("Read Pet"):
            resp = self.unchecked_pet_request.read(locator=self.fake_pet.id * 2)
            assert resp.status_code == 404, \
                f"Invalid status code: {resp.status_code}. Expected: 404"

    @pytest.mark.parametrize("test_id", ["test", "-6"])
    @pytest.mark.negative
    def test_find_pet_by_invalid_id(self, test_id):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        with allure.step("Read Pet"):
            resp = self.unchecked_pet_request.read(locator=test_id)
            assert resp.status_code == 404, \
                f"Invalid status code: {resp.status_code}. Expected: 404"
