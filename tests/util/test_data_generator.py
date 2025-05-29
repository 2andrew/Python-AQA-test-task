import random
from typing import get_type_hints, get_args, get_origin

from faker import Faker
from pydantic import BaseModel

fake = Faker()


class TestDataGenerator:
    def generate_value(self, field_type):
        origin = get_origin(field_type)
        args = get_args(field_type)

        if field_type == int:
            return random.randint(1, 1000)
        elif field_type == str:
            return fake.word()
        elif origin == list and args:
            element_type = args[0]
            return [self.generate_value(element_type) for _ in range(2)]
        elif isinstance(field_type, type) and issubclass(field_type, BaseModel):
            return self.generate_fake_model(field_type)
        else:
            return None

    def generate_fake_model(self, model_class):
        type_hints = get_type_hints(model_class)
        values = {}
        for field_name, field_type in type_hints.items():
            values[field_name] = self.generate_value(field_type)
        return model_class(**values)
