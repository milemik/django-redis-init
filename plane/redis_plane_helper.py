import json

import redis

from core import settings
from plane.models import PlaneRedisModel

redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


class PlanesRedis:
    KEY = "planes"

    def get_key(self, model_key: str) -> str:
        return f"{self.KEY}_{model_key}"

    def get_planes(self) -> list:
        all_planes = redis_cli.keys(f"{self.KEY}_*")
        result = list()
        for plane in all_planes:
            result.append(json.loads(redis_cli.get(plane)))
        return result

    def add_plane(self, data) -> None:
        new_plane = PlaneRedisModel(**data)
        redis_cli.set(f"{self.KEY}_{new_plane.model_key}", json.dumps(new_plane.to_json()))

    def edit_plane(self, new_data: dict) -> None:
        plane_key = self.get_key(model_key=new_data.get("model_key"))
        old_data = redis_cli.get(plane_key)
        if old_data is None:
            raise ValueError(f"PLANE DOESN'T EXIST {new_data.get('model_key')}")
        old_data_dict = json.loads(old_data)

        for k, v in new_data.items():
            if k in old_data_dict:
                old_data_dict[k] = v

        redis_cli.set(plane_key, json.dumps(old_data_dict))
