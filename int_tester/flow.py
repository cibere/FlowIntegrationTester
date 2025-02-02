from .tree import build_filetree
from pathlib import Path
from yarl import URL
from .zip import extract_zip


class FlowEnv:
    def __init__(self) -> None:
        self.filetree_is_built: bool = False
        self.base_dir = Path("FlowLauncher")
        self.settings_dir = self.base_dir / "Settings"
        self.python_environment_dir = (
            self.base_dir / "Environments" / "Python" / "PythonEmbeddable-v3.11.4"
        )

    async def ensure_built(self) -> None:
        if self.filetree_is_built is False:
            await build_filetree()
            self.filetree_is_built = True

    def _remove_ext(self, before: str) -> str:
        parts = before.split(".")
        parts.pop(-1)
        return ".".join(parts)

    async def install_plugin(self, loc: Path | URL) -> Path:
        await self.ensure_built()

        dir = Path("FlowLauncher", "Plugins", self._remove_ext(loc.name))
        dir.mkdir()

        await extract_zip(loc, dir)

        return dir

    def clear(self):
        self.base_dir.unlink(missing_ok=True)
