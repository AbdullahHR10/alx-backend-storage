#!/usr/bin/env python3
""" Module that contains Cache class. """
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """ Cache class. """
    def __init__(self):
        """ The constructor. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a random key and return the key."""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key