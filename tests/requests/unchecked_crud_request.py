import requests

from config import settings
from tests.requests.base_request import BaseCRUDRequest, Request


class UncheckedRequest(BaseCRUDRequest, Request):
    BASIC_HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self, endpoint):
        super().__init__(endpoint)

    def read(self, locator):
        response = requests.get(f"{settings.BASE_API_URL}{self.endpoint}/{locator}", headers=self.BASIC_HEADERS)
        print(f"GET {settings.BASE_API_URL}{self.endpoint}/{locator}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response

    def update(self, model):
        response = requests.put(f"{settings.BASE_API_URL}{self.endpoint}", json=model, headers=self.BASIC_HEADERS)
        print(f"PUT {settings.BASE_API_URL}{self.endpoint}")
        print(f"BODY {model}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response

    def delete(self, id):
        response = requests.delete(f"{settings.BASE_API_URL}{self.endpoint}/{id}", headers=self.BASIC_HEADERS)
        print(f"DELETE {settings.BASE_API_URL}{self.endpoint}/{id}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response

    def create(self, model):
        from tests.util.test_data_storage import TstDataStorage
        response = requests.post(f"{settings.BASE_API_URL}{self.endpoint}", json=model, headers=self.BASIC_HEADERS)
        print(f"POST {settings.BASE_API_URL}{self.endpoint}")
        print(f"BODY {model}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        TstDataStorage.get_storage().add_created_entity(self.endpoint, model)
        return response
