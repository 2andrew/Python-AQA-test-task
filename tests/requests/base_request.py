from abc import ABC, abstractmethod


class Request:
    def __init__(self, endpoint):
        self.endpoint = endpoint


class BaseCRUDRequest(ABC):

    @abstractmethod
    def create(self, model):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def update(self, model):
        pass

    @abstractmethod
    def delete(self, id):
        pass
