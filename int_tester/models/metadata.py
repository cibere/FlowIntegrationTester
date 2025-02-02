from __future__ import annotations
import uuid
from typing import Any
from pathlib import Path
from typing import Literal
from .base import Model

MISSING: Any = object()


class PluginMetadata(Model):
    id: uuid.UUID
    actionKeyword: str
    name: str
    description: str
    author: str
    version: str
    language: Literal[
        "csharp",
        "executable",
        "fsharp",
        "python",
        "javascript",
        "typescript",
        "python_v2",
        "executable_v2",
        "javascript_v2",
        "typescript_v2",
    ]
    website: str
    icoPath: Path
    executeFileName: str
    executeFilePath: Path
    pluginDirectory: Path
    disabled: bool
    actionKeywords: list[str] = MISSING
