import allure
import pytest

from tests.api.base_api_test import BaseApiTest
from tests.models.api_models import Pet


class TestPetPostReq(BaseApiTest):

    @pytest.mark.positive
    def test_post_pet(self):
        with allure.step("Create Pet"):
            resp = self.pet_request.create(self.fake_pet.model_dump())

            pet = Pet.model_validate(resp.json())
            assert self.fake_pet == pet, \
                f"Pet entity body is invalid after POST request"

    @pytest.mark.positive
    def test_post_pet_empty_fields(self):
        self.fake_pet.tags = []
        self.fake_pet.photoUrls = []
        with allure.step("Create Pet"):
            resp = self.pet_request.create(self.fake_pet.model_dump())

            pet = Pet.model_validate(resp.json())
            assert self.fake_pet == pet, \
                f"Pet entity body is invalid after POST request with empty fields"

    @pytest.mark.negative
    def test_post_pet_wrong_id(self):
        self.fake_pet.id = "test"
        with allure.step("Create Pet"):
            resp = self.unchecked_pet_request.create(self.fake_pet.model_dump())
            assert resp.status_code == 500, \
                f"Invalid status code: {resp.status_code}. Expected: 500"

    @pytest.mark.negative
    def test_post_pet_wrong_photoUrls(self):
        self.fake_pet.photoUrls = "56"
        with allure.step("Create Pet"):
            resp = self.unchecked_pet_request.create(self.fake_pet.model_dump())
            assert resp.status_code == 500, \
                f"Invalid status code: {resp.status_code}. Expected: 500"

    @pytest.mark.negative
    def test_post_pet_wrong_tags(self):
        self.fake_pet.tags = "56"
        with allure.step("Create Pet"):
            resp = self.unchecked_pet_request.create(self.fake_pet.model_dump())
            assert resp.status_code == 500, \
                f"Invalid status code: {resp.status_code}. Expected: 500"
