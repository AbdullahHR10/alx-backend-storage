#!/usr/bin/env python3
""" Module that contains Cache class. """
import redis
from uuid import uuid4
from typing import Any, Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator for Cache class methods to track call count. """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """ Wraps called method and adds its call count redis before execution.
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """ Cache class. """
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        """ Constructor allowing optional Redis connection configuration. """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a random key and return the key."""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and optionally
            apply a callable to convert the data.
        - If key does not exist, return None (like Redis.get).
        - If fn is provided, apply it to the result before returning.
        """
        value = self._redis.get(key)
        if value is None:
            return None

        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """ Parametrize get method to return a string (decoding UTF-8). """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """ Parametrize get method to return an integer. """
        return self.get(key, fn=int)