from __future__ import annotations

from .base import YamlModel as Model


class _BaseAttributesWoDefValue(Model):
    name: str
    label: str
    description: str | None = None


class BaseAttributes(_BaseAttributesWoDefValue):
    defaultValue: str | None = None


class TextBlockFieldAttrs(Model):
    description: str


class TextBlockField(Model, tag="textBlock"):
    attributes: TextBlockFieldAttrs


class InputField(Model, tag="input"):
    attributes: BaseAttributes


class TextareaField(Model, tag="textarea"):
    attributes: BaseAttributes


class CheckboxFieldAttributes(_BaseAttributesWoDefValue):
    defaultValue: bool | None = None


class CheckboxField(Model, tag="checkbox"):
    attributes: CheckboxFieldAttributes


class DropdownFieldAttributes(BaseAttributes):
    options: list[str] = []

    def __post_init__(self) -> None:
        if self.defaultValue and self.defaultValue not in self.options:
            raise ValueError(
                f"Default value {self.defaultValue!r} is not in option list"
            )


class DropdownField(Model, tag="dropdown"):
    attributes: DropdownFieldAttributes


class SettingsTemplate(Model):
    body: list[
        TextBlockField | InputField | TextareaField | CheckboxField | DropdownField
    ]

    def __post_init__(self) -> None:
        names = []
        for field in self.body:
            name = getattr(field.attributes, "name", None)
            if name is None:
                continue
            if name in names:
                raise ValueError(f"Duplicate Name: {name!r}")
            names.append(name)
