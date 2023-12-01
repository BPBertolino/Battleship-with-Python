

class UsuarioInvalidoException(Exception):
    def __init__(self):
        super().__init__("O usuário não é válido.")