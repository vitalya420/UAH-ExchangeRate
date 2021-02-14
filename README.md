# UAH-ExchangeRate
Get exchange rate for UAH asynced or multithreaded

Example async:
```
import asyncio

from APIClient import APIClientAsync, Calculator

api_client = APIClientAsync()


@api_client.on("updated")
async def on_exchange_updated(rate):
    calc = Calculator(rate)
    print(calc.get_direction("UAH", "EUR"))


@api_client.on("started")
async def polling_started():
    print("Polling started")

loop = asyncio.get_event_loop()
loop.run_until_complete(api_client.start_polling())

```

Example threded

```
from APIClient import APIClientThreaded, Calculator

api_client = APIClientThreaded()


@api_client.on("updated")
def on_exchange_updated(rate):
    calc = Calculator(rate)
    print(calc.get_direction("UAH", "EUR"))


@api_client.on("started")
def polling_started():
    print("Polling started")


api_client.start_polling()

```
