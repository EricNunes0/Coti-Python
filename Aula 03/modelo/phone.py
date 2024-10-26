class Phone:
    def __init__(self, type=None, number=None):
        self._type = type
        self._number = number
        # Atributo relacional
        self._person = None
        pass

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, value):
        self._person = value
        pass

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
        pass

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
        pass

    def __str__(self):
        return f"{self._type}, {self._number}"

    pass