from collections import defaultdict
from typing import Set, Dict, Optional

from pydantic import BaseModel

from tests.requests.endpoints import Endpoint
from tests.requests.unchecked_crud_request import UncheckedRequest


class TstDataStorage:
    _instance = None

    def __init__(self):
        self.created_entities_map: Dict[Endpoint, Set[str]] = defaultdict(set)

    @classmethod
    def get_storage(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _add_created_entity(self, endpoint: Endpoint, entity_id: Optional[str]):
        if entity_id:
            self.created_entities_map[endpoint].add(entity_id)

    def _get_entity_id_or_locator(self, model) -> str:
        for field in ['id', 'locator']:
            if isinstance(model, BaseModel):
                if hasattr(model, field):
                    value = getattr(model, field)
                    if value is not None:
                        return str(value)
            elif isinstance(model, dict):
                if field in model and model[field] is not None:
                    return str(model[field])
        raise ValueError("Cannot get 'id' or 'locator' of entity")

    def add_created_entity(self, endpoint: Endpoint, model: BaseModel):
        entity_id = self._get_entity_id_or_locator(model)
        self._add_created_entity(endpoint, entity_id)

    def delete_created_entities(self):
        for endpoint, ids in self.created_entities_map.items():
            for entity_id in ids:
                UncheckedRequest(endpoint).delete(entity_id)
        self.created_entities_map.clear()
