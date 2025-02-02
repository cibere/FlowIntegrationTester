from __future__ import annotations
from pathlib import Path
from typing import Any

Filetree = dict[str, "Filetree | str"]
MISSING: Any = object()

raw_filetree: Filetree = {
    "FlowLauncher": {
        "Cache": {
            ".temp.plugins": {},
        },
        "Logs": {},
        "Plugins": {},
        "Settings": {},
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
        else:
            path.mkdir(exist_ok=True)
            build_filetree(value, path)
