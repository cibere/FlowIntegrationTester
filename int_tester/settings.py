import yaml
import json
from pathlib import Path
from ._types.settings_template import SettingsTemplate as SettingsTemplatePayload
from ._types.json import Jsonable


class SettingsTemplate:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.data: SettingsTemplatePayload = yaml.safe_load(self.path.read_text())

    def create_default_settings(self) -> dict[str, Jsonable]:
        data = {}

        for input in self.data["body"]:
            name = input["attributes"].get("name")
            default_value = input["attributes"].get("defaultValue")
            if name is not None and default_value is not None:
                data[name] = default_value
        return data

    def dump_settings(self, folder: Path, settings: dict[str, Jsonable]) -> None:
        if not folder.is_dir():
            raise ValueError("Can only dump to a folder")

        files = [
            folder / "Settings.json",
            folder / "Settings.json.bak",
        ]
        content = json.dumps(settings)

        for file in files:
            file.write_text(content)
