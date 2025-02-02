from yarl import URL
from pathlib import Path
import aiohttp
import zipfile
from io import BytesIO


async def extract_zip(loc: Path | URL, target: Path) -> None:
    if isinstance(loc, URL):
        file = BytesIO()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(loc) as res:
                file.write(await res.read())
    else:
        file = loc

    with zipfile.ZipFile(file, "r") as zf:
        zf.extractall(target)
