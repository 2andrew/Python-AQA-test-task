import copy

import allure
import pytest

from tests.api.base_api_test import BaseApiTest
from tests.models.api_models import Pet
from tests.util.test_data_generator import TestDataGenerator


class TestPetPutReq(BaseApiTest):

    @pytest.mark.positive
    def test_put_pet(self):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        with allure.step("Update Pet"):
            new_fake_pet = TestDataGenerator().generate_fake_model(Pet)
            new_fake_pet.id = self.fake_pet.id

            resp = self.pet_request.update(new_fake_pet.model_dump())
            pet = Pet.model_validate(resp.json())
            assert new_fake_pet == pet, \
                f"Pet entity body is invalid after PUT request"

    @pytest.mark.positive
    def test_put_pet_partial(self):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        with allure.step("Update Pet"):
            new_fake_pet = TestDataGenerator().generate_fake_model(Pet)
            pet_to_update = copy.copy(self.fake_pet)

            pet_to_update.name = new_fake_pet.name
            pet_to_update.tags = new_fake_pet.tags
            pet_to_update.status = new_fake_pet.status

            resp = self.pet_request.update(pet_to_update.model_dump())
            pet = Pet.model_validate(resp.json())
            assert pet_to_update == pet, \
                f"Pet entity body is invalid after PUT request"

    @pytest.mark.positive
    def test_put_pet_empty_fields(self):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        self.fake_pet.tags = []
        self.fake_pet.photoUrls = []
        with allure.step("Create Pet"):
            resp = self.pet_request.create(self.fake_pet.model_dump())

            pet = Pet.model_validate(resp.json())
            assert self.fake_pet == pet, \
                f"Pet is not created with empty fields"

    @pytest.mark.negative
    def test_put_pet_wrong_id(self):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        with allure.step("Update Pet"):
            pet_to_update = copy.copy(self.fake_pet)
            pet_to_update.id = "test"
            resp = self.unchecked_pet_request.update(pet_to_update.model_dump())
            assert resp.status_code == 500, \
                f"Invalid status code: {resp.status_code}. Expected: 500"

    @pytest.mark.negative
    def test_put_pet_wrong_photoUrls(self):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        with allure.step("Update Pet"):
            pet_to_update = copy.copy(self.fake_pet)
            pet_to_update.photoUrls = "56"
            resp = self.unchecked_pet_request.update(pet_to_update.model_dump())
            assert resp.status_code == 500, \
                f"Invalid status code: {resp.status_code}. Expected: 500"

    @pytest.mark.negative
    def test_put_pet_wrong_tags(self):
        with allure.step("Prepare Pet"):
            self.pet_request.create(self.fake_pet.model_dump())

        with allure.step("Update Pet"):
            pet_to_update = copy.copy(self.fake_pet)
            pet_to_update.tags = "56"
            resp = self.unchecked_pet_request.update(pet_to_update.model_dump())
            assert resp.status_code == 500, \
                f"Invalid status code: {resp.status_code}. Expected: 500"
