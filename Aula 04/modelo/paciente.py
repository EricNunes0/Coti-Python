class Paciente:
    def __init__(self, name=None, gender=None, age=None):
        self._name = name
        self._gender = gender
        self._age = age
        # Atributo relacional
        self._medicos = None

    @property
    def medicos(self):
        return self._medicos

    @medicos.setter
    def medicos(self, value):
        self._medicos = value
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        pass

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
        pass

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        pass

    def __str__(self):
        return f'{self._name}, {self._gender}, {self._age}'

    def __repr__(self):
        return f'{self._name}, {self._gender}, {self._age}'