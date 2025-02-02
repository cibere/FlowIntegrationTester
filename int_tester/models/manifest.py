from __future__ import annotations
import uuid
from typing import Any
from pathlib import Path
from typing import Literal
from .base import Model

MISSING: Any = object()


class PluginManifest(Model):
    ID: uuid.UUID
    ActionKeyword: str
    Name: str
    Description: str
    Author: str
    Version: str
    Language: Literal[
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
    Website: str
    IcoPath: Path
    ExecuteFileName: Path
    ActionKeywords: list[str] = MISSING

    def __post_init__(self):
        if len(self.ID.bytes) != 16:
            raise ValueError("Invalid ID")
        # if not self.ExecuteFileName.exists():
        #    raise ValueError("Could not find executefilename")
        # if not self.IcoPath.exists():
        #    raise ValueError("Could not find icon")
        if self.ActionKeywords is MISSING:
            self.ActionKeywords = [self.ActionKeyword]
