from .tree import build_filetree
from pathlib import Path
import zipfile
import aiohttp
from yarl import URL


class FlowEnv:
    def __init__(self) -> None:
        self.filetree_is_built: bool = False
        self.base_dir = Path("FlowLauncher")
        self.settings_dir = self.base_dir / "Settings"

    def ensure_built(self) -> None:
        if self.filetree_is_built is False:
            build_filetree()
            self.filetree_is_built = True

    def _remove_ext(self, before: str) -> str:
        parts = before.split(".")
        parts.pop(-1)
        return ".".join(parts)

    async def install_plugin(self, loc: Path | URL) -> Path:
        self.ensure_built()

        if isinstance(loc, URL):
            temp_plugins_dir = self.base_dir / "Cache" / ".temp.plugins"
            serialized_filename = (
                "_".join(loc.parts).replace("/", "-").replace("\\", "-")
            )
            file = temp_plugins_dir / serialized_filename

            async with aiohttp.ClientSession() as cs:
                async with cs.get(loc) as res:
                    file.write_bytes(await res.read())
        else:
            file = loc

        dir = Path("FlowLauncher", "Plugins", self._remove_ext(file.name))
        dir.mkdir()

        with zipfile.ZipFile(file, "r") as zf:
            print(f"Extracting plugin from {file.absolute()}")
            zf.extractall(dir)

        return dir

    def clear(self):
        self.base_dir.unlink(missing_ok=True)
