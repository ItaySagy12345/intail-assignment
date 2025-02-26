import redis.asyncio as redis
from typing import Union, Any
from src.config.config import CONFIG


class RedisCache:
    _instance = None

    def __new__(cls) -> None:
        """
        Redis Cache singleton class
        """
            
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """
        Instantiates a Redis instance if there is none
        Return None
        """
        
        redis_url: str = CONFIG["cache"]["redis_url"]
        if not hasattr(self, "client"):
            self.client = redis.from_url(redis_url, decode_responses=True)

    async def get(self, key: str) -> Union[Any, None]:
        """
        Returns an item from the cache by key
        Param: key [String]: The key of the item to get
        Return [Any, None]: The item stored under the given key
        """
                
        return await self.client.get(key)

    async def set(self, key: str, value: str, expire: int = 1 * 60 * 60 * 24) -> Any:
        """
        Stores an item in the cache by key
        Ex: {"record_type":slug} or {"author":"J. K. Rowling"}
        Param: key [String]: The key of the item to store
        Param: value [String]: The item to store
        Return None
        """
                
        await self.client.set(key, value, ex=expire)

    async def delete(self, key: str) -> None:
        """
        Deletes and item in the cache by key
        Param: key [String]: The key of the item to delete
        Return None
        """
                
        await self.client.delete(key)

    async def close(self) -> None:
        """
        Closes the Redis Cache instance
        Return None
        """
                
        await self.client.close()


redis_cache = RedisCache()