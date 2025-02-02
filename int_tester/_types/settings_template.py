from typing import TypedDict


class InputAttributes(TypedDict, total=False):
    description: str
    name: str
    defaultValue: str | bool
    options: list[str]


class Input(TypedDict):
    type: str
    attributes: InputAttributes


class SettingsTemplate(TypedDict):
    body: list[Input]
