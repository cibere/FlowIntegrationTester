from __future__ import annotations
from pathlib import Path
from typing import Any
import json
from yarl import URL
from .default_flow_settings import default_flow_settings
from .zip import extract_zip

Filetree = dict[str, "Filetree | str | URL"]
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
        "Environments": {
            "Python": {
                "PythonEmbeddable-v3.11.4": URL(
                    "https://www.python.org/ftp/python/3.11.4/python-3.11.4-embed-amd64.zip"
                )
            }
        },
    }
}


async def build_filetree(tree: Filetree = MISSING, parent: Path = MISSING):
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
        elif isinstance(value, URL):
            path.mkdir()
            await extract_zip(value, path)
        else:
            path.mkdir(exist_ok=True)
            await build_filetree(value, path)
