import asyncio
import json

import aiohttp

from APIClient.client import APIClient


class APIClientAsync(APIClient):
    def __init__(self, delay: int = 3600):
        super().__init__(delay)
        self.session = aiohttp.ClientSession()

    async def get_exchange_rate(self) -> list:
        async with self.session:
            async with self.session.get(self.url) as resp:
                json_ = json.loads(await resp.text())
                return json_

    async def start_polling(self):
        await self._handle_start()
        while True:
            rate = await self.get_exchange_rate()
            await self._handle_update(rate)
            self.last_update = rate
            await asyncio.sleep(self.delay)

    async def _handle_update(self, rate):
        if rate != self.last_update:
            handler = self.handlers.get("updated")
            if handler:
                await handler(rate)

    async def _handle_start(self):
        handler = self.handlers.get("started")
        if handler:
            await handler()
