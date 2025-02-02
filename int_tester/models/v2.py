from .base import Model
from typing import Literal, Any
from .metadata import PluginMetadata
from .._types.json import Jsonable


class Base(Model):
    jsonrpc: Literal["2.0"]
    id: int


class Request(Base):
    method: str
    params: Jsonable


class InitializationPayload(Model):
    currentPluginMetadata: PluginMetadata
    api: dict[str, Any] = {}


class InitalizationRequest(Base):
    params: list[InitializationPayload]
    method: Literal["initialize"] = "initialize"


class CloseRequest(Base):
    method: Literal["close"] = "close"
    params: Jsonable = []


class ExecutePayload(Base):
    hide: bool


class ExecuteResponse(Base):
    result: ExecutePayload
