from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    """
    Universal API response class
    """

    data: T
    meta: dict = {}


class APIFilter:
    """
    Api filter class for pagination
    """

    def __init__(self, page: int, size: int):
        self.page = page
        self.size = size
        self.offset = (page - 1) * size