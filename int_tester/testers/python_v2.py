from __future__ import annotations
from int_tester.plugin import Plugin
from typing import Self
import asyncio
import sys
from asyncio.streams import StreamReader, StreamWriter
from int_tester.models.v2 import (
    CloseRequest,
    Base as BaseV2Model,
)
import json


class V2PythonPluginTester:
    process: asyncio.subprocess.Process

    def __init__(self, plugin: Plugin) -> None:
        self.plugin = plugin
        self._id = 0
        self.close_request_id: int = 0
        self.init_request_future = asyncio.Future()
        self.close_request_future = asyncio.Future()
        self.polling_task: asyncio.Task

    @property
    def reader(self) -> StreamReader:
        reader = self.process.stdout
        assert reader
        return reader

    @property
    def writer(self) -> StreamWriter:
        writer = self.process.stdin
        assert writer
        return writer

    @property
    def id(self) -> int:
        self._id += 1
        return self._id

    @id.setter
    def id(self, val):
        self._id = val

    async def write(self, msg: bytes):
        print(f"Writing {msg}")
        self.writer.write(msg + b"\r\n")
        await self.writer.drain()

    async def poll_lines(self):
        print("starting to poll lines")
        async for line in self.reader:
            print(f"Received {line!r}")
            data = json.loads(line)
            if "id" in data:
                self.id = data["id"]
                if data["id"] == self.close_request_id:
                    self.close_request_future.set_result(line)

    async def run_close(self) -> None:
        self.close_request_id = self.id
        request = CloseRequest(jsonrpc="2.0", id=self.close_request_id)

        await self.write(request.encode())
        line = await self.close_request_future
        print("Validating close response")
        response = BaseV2Model.decode(line)
        assert response.id == request.id

    async def start(self) -> None:
        self.polling_task = asyncio.create_task(self.poll_lines())
        print("testing close")
        await self.run_close()
        print("Done with close")
        self.polling_task.cancel()

    async def __aenter__(self) -> Self:
        manifest = self.plugin.get_manifest()
        exe_path = self.plugin.plugin_path / manifest.ExecuteFileName

        self.process = await asyncio.create_subprocess_exec(
            sys.executable,
            exe_path,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
        )
        return self

    async def __aexit__(self, *args) -> bool:
        self.process.kill()
        return False


tester = V2PythonPluginTester
