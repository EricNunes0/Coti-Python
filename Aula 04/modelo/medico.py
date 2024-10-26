class Medico:
    def __init__(self, name=None, especializacao=None):
        self._name = name
        self._especializacao = especializacao
        self._pacientes = None

    @property
    def pacientes(self):
        return self._pacientes

    @pacientes.setter
    def pacientes(self, value):
        self._pacientes = value
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        pass

    @property
    def especializacao(self):
        return self._especializacao

    @especializacao.setter
    def especializacao(self, value):
        self._especializacao = value
        pass

    def __str__(self):
        return f'{self._name}, {self._especializacao}'

    def __repr__(self):
        return f'{self._name}, {self._especializacao}'