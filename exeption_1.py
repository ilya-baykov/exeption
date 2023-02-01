class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        if not len(currency) == 3:
            raise NameError("Неверная длина названия валюты")
        if not currency == currency.upper():
            raise ValueError("Назвние должно состоять из заглавных букв")
        self.currency = currency
        self.balance = balance

    def verify_currency(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                return other.balance
            else:
                raise ValueError("Нельзя сравнивать разные валюты")
        else:
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")

    def __eq__(self, other):
        return self.verify_currency(other) == self.balance

    def __add__(self, other):
        if self.verify_currency(other):
            return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if self.verify_currency(other):
            return Wallet(self.currency, self.balance - other.balance)
