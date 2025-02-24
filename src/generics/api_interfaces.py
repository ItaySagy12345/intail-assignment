from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    """
    Universal API response class
    """

    data: T
    meta: dict = {}


class ApiFilter(BaseModel):
    """
    Api filter class for pagination
    """

    page: int
    size: int