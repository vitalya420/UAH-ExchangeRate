import time
from threading import Thread

from .client import APIClient


class APIClientThreaded(APIClient, Thread):
    def __init__(self, delay: int = 3600):
        super().__init__(delay)
        Thread.__init__(self)

    def start_polling(self):
        self.start()

    def run(self):
        self._handle_start()
        while True:
            rate = self.get_exchange_rate()
            self._handle_update(rate)
            self.last_update = rate
            time.sleep(self.delay)

    def _handle_start(self):
        handler = self.handlers.get("started")
        if handler:
            handler()

    def _handle_update(self, rate):
        if rate != self.last_update:
            handler = self.handlers.get("updated")
            if handler:
                handler(rate)
