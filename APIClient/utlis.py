class Calculator:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def get_direction(self, base, dest):
        if base == dest:
            return {"buy": 1.0, "sale": 1.0}
        for rate in self.exchange_rate:
            cc = (rate["base_ccy"], rate["ccy"])
            if base in cc and dest in cc:
                if (base, dest) == cc:
                    return {"buy": float(rate["buy"]), "sale": float(rate["sale"])}
                return {"buy": round(1 / float(rate["buy"]), 4),
                        "sale": round(1 / float(rate["sale"]), 4)}
