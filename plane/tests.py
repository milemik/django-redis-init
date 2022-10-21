from unittest.mock import patch

import redis
from django.conf import settings
from django.test import TestCase

from plane.redis_plane_helper import PlanesRedis

redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


class TestPlanesRedis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pr = PlanesRedis()
        pr.KEY = "test"
        cls.planes_redis = pr
        cls.plane_data = {"model_key": "123a", "plane_name": "Ai14", "plane_active": True}

    def test_get_key(self):
        test_key = "first"
        result = self.planes_redis.get_key(model_key=test_key)
        self.assertEqual(result, "test_first")

    def test_get_planes(self) -> None:
        result = self.planes_redis.get_planes()
        self.assertEqual(result, [])

    def test_add_plane(self):
        self.planes_redis.add_plane(data=self.plane_data)
        result = self.planes_redis.get_planes()
        self.assertEqual(result, [self.plane_data])
        self.tearDownClass()

    def test_add_plane_no_model_key(self):
        plane = self.plane_data.copy()
        plane.pop("model_key")
        with self.assertRaises(TypeError):
            self.planes_redis.add_plane(data=plane)

    def test_add_plane_no_plane_name(self):
        plane = self.plane_data.copy()
        plane.pop("plane_name")
        with self.assertRaises(TypeError):
            self.planes_redis.add_plane(data=plane)

    def test_add_plane_no_plane_active(self):
        plane = self.plane_data.copy()
        plane.pop("plane_active")
        with self.assertRaises(TypeError):
            self.planes_redis.add_plane(data=plane)

    def test_edit_plane(self):
        self.planes_redis.add_plane(self.plane_data)
        new_plane_data = self.plane_data.copy()
        new_plane_data.pop("plane_active")
        new_plane_data["plane_name"] = "NEW"

        self.planes_redis.edit_plane(new_plane_data)

        result = self.planes_redis.get_planes()

        new_plane_data["plane_active"] = True

        self.assertEqual(result, [new_plane_data])
        self.tearDownClass()

    @classmethod
    def tearDownClass(cls) -> None:
        all_test_keys = redis_cli.keys("test_*")
        for test_key in all_test_keys:
            redis_cli.delete(test_key)
