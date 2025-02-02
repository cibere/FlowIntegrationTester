from __future__ import annotations
from int_tester.plugin import Plugin
from typing import Self
import asyncio
import sys
from int_tester.models.v1 import Request as RequestPayload
import json


class V1PythonPluginTester:
    def __init__(self, plugin: Plugin) -> None:
        self.plugin = plugin

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *args) -> bool:
        return False

    async def start(self) -> None:
        manifest = self.plugin.get_manifest()
        exe_path = self.plugin.plugin_path / manifest.ExecuteFileName
        settings = self.plugin.init_settings()

        payload = RequestPayload(method="query", parameters=[""], settings=settings)

        proc = await asyncio.create_subprocess_exec(
            sys.executable,
            "-S",
            exe_path,
            payload.encode().decode(),
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        exit_code = await proc.wait()

        print(f"Stdout: {stdout}")
        print(f"Stderr: {stderr}")

        json.loads(stdout)
        assert exit_code == 0


tester = V1PythonPluginTester
