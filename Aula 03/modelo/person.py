class Person:
    def __init__(self, name = None, email = None):
        self._name = name
        self._email = email
        # Atributo relacional
        self._address = None
        self._phones = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
        pass

    @property
    def phones(self):
        return self._phones

    @phones.setter
    def phones(self, value):
        self._phones = value
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

    def __repr__(self):
        return f"{self.name}, {self.email}"

    pass