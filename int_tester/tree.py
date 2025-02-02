from __future__ import annotations
from pathlib import Path
from typing import Any
import json
from .default_flow_settings import default_flow_settings

Filetree = dict[str, "Filetree | str"]
MISSING: Any = object()


raw_filetree: Filetree = {
    "FlowLauncher": {
        "Cache": {
            ".temp.plugins": {},
        },
        "Logs": {},
        "Plugins": {},
        "Settings": {
            "History.json": json.dumps({"Items": []}),
            "TopMostRecord.json": json.dumps({"records": {}}),
            "UserSelectedRecord.json": json.dumps({"recordsWithQuery": {}}),
            "Settings.json": default_flow_settings,
            "Plugins": {},
        },
        "Themes": {},
    }
}


def build_filetree(tree: Filetree = MISSING, parent: Path = MISSING):
    if tree is MISSING:
        tree = raw_filetree

    print(f"Building tree for {tree!r} with {parent!r}")

    for dir, value in tree.items():
        path = Path(dir) if parent is MISSING else parent / dir

        if isinstance(value, str):
            print(f"Writing to {path!r}")
            with path.open("w", encoding="UTF-8") as f:
                f.write(value)
            if path.name.endswith(".json"):
                print(f"Creating backup file for {path!r}")
                backup_file = path.with_suffix(".bak")
                with backup_file.open("w", encoding="UTF-8") as f:
                    f.write(value)
        else:
            path.mkdir(exist_ok=True)
            build_filetree(value, path)
