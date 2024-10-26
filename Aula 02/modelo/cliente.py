from abc import ABC, abstractmethod

class Cliente(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass

    def __init__(self, name = None, email = None):
        self._name = name
        self._email = email
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        pass

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
        pass

    def __str__(self):
        return f"{self.name}, {self.email}"

    pass

class ClienteFisico(Cliente):
    def calculate_discount(self):
        return 20.0

    def __init__(self, name=None, email=None, cpf=None, gender=None):
        Cliente.__init__(self, name, email)
        self._cpf = cpf
        self._gender = gender
        pass

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value
        pass

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self.gender = value
        pass

    def __str__(self):
        return f"{Cliente.__str__(self)}, {self._cpf}, {self._gender}"

    pass

class ClienteJuridico(Cliente):
    def calculate_discount(self):
        return 30.0

    def __init__(self, name=None, email=None, cnpj=None, ramo=None):
        Cliente.__init__(self, name, email)
        self._cnpj = cnpj
        self._ramo = ramo

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, value):
        self._cnpj = value
        pass

    @property
    def ramo(self):
        return self._ramo

    @ramo.setter
    def ramo(self, value):
        self._ramo = value
        pass

    def __str__(self):
        return f"{Cliente.__str__(self)}, {self._cnpj}, {self._ramo}"
    pass