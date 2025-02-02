import asyncio
from yarl import URL
from pathlib import Path
from .plugin import Plugin

__all__ = ("test",)


async def _async_test_plugin(loc: Path | URL) -> None:
    plugin = Plugin(loc)

    await plugin.install()
    await plugin.test()


def _convert_loc(raw_loc: str) -> Path | URL:
    if raw_loc.startswith(("http://", "https://")):
        return URL(raw_loc)
    path = Path(raw_loc)
    if path.exists():
        return path

    raise ValueError("Invalid location or no location given")


def test(loc: str) -> None:
    asyncio.run(_async_test_plugin(_convert_loc(loc)))
