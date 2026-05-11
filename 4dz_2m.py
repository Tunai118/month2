rates = {
    "KGS": 1, "EUR": 96, "RUB": 1.2, "USD": 89
}


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        sum1 = self.convert_to_kgs()
        sum2 = other.convert_to_kgs()
        return Money(sum1 + sum2, "KGS")

    def __sub__(self, other):
        sum1 = self.convert_to_kgs()
        sum2 = other.convert_to_kgs()
        return Money(sum1 - sum2, "KGS")

    def __mul__(self, number):
        return Money(self.amount * number, self.currency)

    def __truediv__(self, number):
        return Money(self.amount / number, self.currency)

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")
result = money1 + money2
print(result)
money3 = Money(10, "EUR")
print(money3 * 5)
