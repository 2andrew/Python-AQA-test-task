import allure
import pytest

from tests.api.base_api_test import BaseApiTest


class TestPetDeleteReq(BaseApiTest):

    @pytest.mark.positive
    def test_delete_pet_by_id(self):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        with allure.step("Delete Pet"):
            # Using retry because Petstore randomly return 404
            resp = self.retry_on_404(self.unchecked_pet_request.delete, max_attempts=5, delay=2, id=self.fake_pet.id)
            assert resp.status_code == 200, \
                f"Invalid status code: {resp.status_code}. Expected: 200"

    @pytest.mark.negative
    def test_delete_pet_by_non_exist_id(self):
        with allure.step("Delete Pet"):
            resp = self.unchecked_pet_request.delete(id=self.fake_pet.id * 2)
            assert resp.status_code == 404, \
                f"Invalid status code: {resp.status_code}. Expected: 404"

    @pytest.mark.parametrize("test_id", ["test", "-6"])
    @pytest.mark.negative
    def test_delete_pet_by_invalid_id(self, test_id):
        with allure.step("Delete Pet"):
            resp = self.unchecked_pet_request.delete(id=test_id)
            assert resp.status_code == 404, \
                f"Invalid status code: {resp.status_code}. Expected: 404"
