from __future__ import annotations
from typing import Protocol, TYPE_CHECKING, Self

if TYPE_CHECKING:
    from ..plugin import Plugin


class PluginTester(Protocol):
    plugin: Plugin

    def __init__(self, plugin: Plugin) -> None: ...

    async def start(self) -> None: ...

    async def __aenter__(self) -> Self: ...

    async def __aexit__(self, *args) -> bool: ...
