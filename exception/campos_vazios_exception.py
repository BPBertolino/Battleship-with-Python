

class CamposVaziosException(Exception):
    def __init__(self):
        super().__init__("Os dados não foram fornecidos.")