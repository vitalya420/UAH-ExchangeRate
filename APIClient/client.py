from abc import ABC, abstractmethod

import requests


class APIClient(ABC):
    def __init__(self, delay: int = 3600):
        """API client to getting exchange rate from PrivatBank API

        :param delay: delay in seconds
        """
        self.delay = delay
        self.session = requests.Session()
        self.handlers = {}
        self.url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        self.last_update = None

    def on(self, event, handler=None):
        """Register an event handler.

        :param event: The event name. Any string.
        :param handler: The function that should be invoked to handle the
                        event. When this parameter is not given, the method
                        acts as a decorator for the handler function.

        Example usage:

            # using as decorator
            @APIClient.on("updated")
            def on_exchange_updated():
                print("Exchange rate was updated")

            # using as method
            def polling_started():
                print("Polling requests started")
            APIClient.on("started", polling_started)

        """

        def set_handler(handler_):
            if callable(handler_):
                self.handlers[event] = handler_
            return handler_

        if handler is None:
            return set_handler
        set_handler(handler)

    def get_exchange_rate(self) -> list:
        """Get a actual from api service

        :return: new exchange rate
        """
        response = self.session.get(self.url).json()
        return response

    @abstractmethod
    def start_polling(self):
        pass

    @abstractmethod
    def _handle_start(self):
        pass

    @abstractmethod
    def _handle_update(self, rate):
        pass
