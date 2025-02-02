from .base import Model
from .._types.json import Jsonable


class Request(Model):
    method: str
    parameters: list[str]
    settings: dict[str, Jsonable]
