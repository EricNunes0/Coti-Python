class Produto:
    def __init__(self, name=None, price=None, quantity=None):
        self._name = name
        self._price = price
        self._quantity = quantity
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        pass

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        pass

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        pass

    def __str__(self):
        return f"{self._name}, {self._price: .2f}, {self._quantity}"
    pass