import json
from dataclasses import dataclass

from django.db import models


@dataclass
class PlaneRedisModel:
    model_key: str
    plane_name: str
    plane_active: bool

    def to_json(self) -> json:
        data = {"model_key": self.model_key, "plane_name": self.plane_name, "plane_active": self.plane_active}
        return data
