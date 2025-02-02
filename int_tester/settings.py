from __future__ import annotations
import json
from pathlib import Path
from .models.settings_template import (
    SettingsTemplate as SettingsTemplatePayload,
    BaseAttributes,
)
from ._types.json import Jsonable


class SettingsTemplate:
    def __init__(self, raw: bytes) -> None:
        data = SettingsTemplatePayload.decode(raw)
        self.fields = data.body

    @classmethod
    def from_path(cls, path: Path) -> SettingsTemplate:
        return cls(path.read_bytes())

    def create_default_settings(self) -> dict[str, Jsonable]:
        data = {}

        for field in self.fields:
            if isinstance(field.attributes, BaseAttributes):
                name = field.attributes.name
                default_value = field.attributes.defaultValue
                if name is not None and default_value is not None:
                    data[name] = default_value
        return data


def dump_settings(folder: Path, settings: dict[str, Jsonable]) -> None:
    if not folder.is_dir():
        raise ValueError("Can only dump to a folder")

    files = [
        folder / "Settings.json",
        folder / "Settings.json.bak",
    ]
    content = json.dumps(settings)

    for file in files:
        file.write_text(content)
