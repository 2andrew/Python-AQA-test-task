from enum import Enum
from typing import Type

from pydantic import BaseModel

from tests.models.api_models import Pet


class Endpoint(Enum):
    PET = ("/pet", Pet)

    def __init__(self, url: str, model_class: Type[BaseModel]):
        self.url = url
        self.model_class = model_class
