from entidade.embarcacao import Embarcacao


class Submarino(Embarcacao):

    def __init__(self):
        super().__init__()
        self.tamanho = 2
        self.nome = "Submarino"
    
    def ocupar_posicoes(self, x_inicial, y_inicial, direcao, tamanho):
        super().ocupar_posicoes(x_inicial, y_inicial, direcao, tamanho)


    
