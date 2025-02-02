from int_tester.plugin import Plugin
from yarl import URL

import asyncio


async def main():
    plugin = Plugin(
        URL(
            "https://github-artifact-downloader.cibere.dev/Flow.Launcher.Plugin.rtfm/2521989760/rtfm.zip"
        )
    )
    await plugin.install()
    await plugin.test()


asyncio.run(main(), debug=True)
