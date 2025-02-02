from __future__ import annotations
from typing import Self, Any
import msgspec
from pathlib import Path


def dec_hook(type: type, obj: Any) -> Any:
    if type is Path:
        return Path(obj)


def enc_hook(obj: Any) -> Any:
    if isinstance(obj, Path):
        return str(obj)
    return str(obj)


class Model(msgspec.Struct):
    @classmethod
    def decode(cls: type[Self], data: bytes) -> Self:
        return msgspec.json.decode(data, type=cls, dec_hook=dec_hook)

    def encode(self) -> bytes:
        return msgspec.json.encode(self, enc_hook=enc_hook)
