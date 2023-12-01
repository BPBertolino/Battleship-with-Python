from entidade.embarcacao import Embarcacao


class Bote(Embarcacao):

    def __init__(self):
        super().__init__()
        self.tamanho = 1
        self.nome = "Bote"
    
    def ocupar_posicoes(self, x_inicial, y_inicial, direcao, tamanho):
        super().ocupar_posicoes(x_inicial, y_inicial, direcao, tamanho)


    
