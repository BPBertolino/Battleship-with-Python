

class DataNascimentoInvalidaException(Exception):
    def __init__(self):
        super().__init__("A data de nascimento não é válida.")