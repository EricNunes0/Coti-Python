class Cliente:

    # Construtor
    def __init__(self, name = None, email = None):
        # Atributos -> Instância - privados (_)
        self._name = name
        self._email = email
        pass

    # Propriedades de entrada e saída
    # setters -> entrada, getters -> saída
    # props
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
        return f'{self.name}, {self.email}'

    pass