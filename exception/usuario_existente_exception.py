

class UsuarioExistenteException(Exception):
    def __init__(self):
        super().__init__("O usuário já existe.")
