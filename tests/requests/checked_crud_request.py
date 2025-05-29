from tests.requests.base_request import BaseCRUDRequest, Request
from tests.requests.unchecked_crud_request import UncheckedRequest


class CheckedRequest(BaseCRUDRequest, Request):

    def __init__(self, endpoint):
        self.unchecked_request = UncheckedRequest(endpoint)
        super().__init__(endpoint)

    def create(self, model):
        response = self.unchecked_request.create(model)
        assert response.status_code == 200, \
            f"Invalid status code: {response.status_code}. Expected: 200"
        return response

    def read(self, id):
        response = self.unchecked_request.read(id)
        assert response.status_code == 200, \
            f"Invalid status code: {response.status_code}. Expected: 200"
        return response

    def update(self, model):
        response = self.unchecked_request.update(model)
        assert response.status_code == 200, \
            f"Invalid status code: {response.status_code}. Expected: 200"
        return response

    def delete(self, id):
        response = self.unchecked_request.delete(id)
        assert response.status_code == 200, \
            f"Invalid status code: {response.status_code}. Expected: 200"
        return response
