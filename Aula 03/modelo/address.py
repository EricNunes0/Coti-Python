class Address:
    def __init__(self, cidade=None, bairro=None, rua=None):
        self._cidade = cidade
        self._bairro = bairro
        self._rua = rua
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
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, value):
        self._cidade = value
        pass

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, value):
        self._bairro = value
        pass

    @property
    def rua(self):
        return self._rua

    @rua.setter
    def rua(self, value):
        self._rua = value
        pass

    def __str__(self):
        return f"{self.cidade}, {self.bairro}, {self.rua}"

    def __repr__(self):
        return f"{self.cidade}, {self.bairro}, {self.rua}"

    pass