import pytest


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, request):
        print(f"Running test {request.node.name}")
