from .flow import FlowEnv
from pathlib import Path
from .models.manifest import PluginManifest
from .models.metadata import PluginMetadata
from yarl import URL
from .testers import fetch as fetch_tester
from .settings import SettingsTemplate
from ._types.json import Jsonable


class Plugin:
    def __init__(self, plugin_zip: Path | URL) -> None:
        self.plugin_zip = plugin_zip
        self._plugin_path: Path | None = None
        self.env = FlowEnv()

    def init_settings(self) -> dict[str, Jsonable]:
        manifest = self.get_manifest()

        file = self.plugin_path / "SettingsTemplate.yaml"
        settings_dir = self.env.settings_dir / manifest.Name
        settings_dir.mkdir()

        template = SettingsTemplate(file)
        data = template.create_default_settings()
        template.dump_settings(settings_dir, data)
        return data

    @property
    def plugin_path(self) -> Path:
        if self._plugin_path is None:
            raise RuntimeError("Plugin has not been installed yet")
        return self._plugin_path

    @property
    def manifest_path(self) -> Path:
        return self.plugin_path / "plugin.json"

    async def install(self) -> None:
        self._plugin_path = await self.env.install_plugin(self.plugin_zip)

    def get_manifest(self) -> PluginManifest:
        with self.manifest_path.open("rb") as f:
            data = f.read()
        return PluginManifest.decode(data)

    async def test(self) -> None:
        manifest = self.get_manifest()
        TesterClass = fetch_tester(manifest.Language)
        tester = TesterClass(self)

        async with tester:
            await tester.start()

    def build_metadata(self) -> PluginMetadata:
        manifest = self.get_manifest()
        return PluginMetadata(
            id=manifest.ID,
            actionKeyword=manifest.ActionKeyword,
            actionKeywords=manifest.ActionKeywords,
            name=manifest.Name,
            description=manifest.Description,
            author=manifest.Author,
            version=manifest.Version,
            language=manifest.Language,
            website=manifest.Website,
            icoPath=manifest.IcoPath,
            executeFileName=manifest.ExecuteFileName.name,
            executeFilePath=manifest.ExecuteFileName.resolve(),
            disabled=False,
            pluginDirectory=self.plugin_path,
        )
