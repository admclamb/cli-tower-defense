class Wallet:
    def __init__(self, default_currency):
        self.currency = default_currency

    def take(self, amount):
        if amount > self.currency:
            print("Amount is greater than players currency")
            return None
        
        self.currency -= amount