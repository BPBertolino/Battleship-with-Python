from entidade.embarcacao import Embarcacao


class Porta_avioes(Embarcacao):

    def __init__(self):
        super().__init__()
        self.tamanho = 4
        self.nome = "Porta aviões"
    
    def ocupar_posicoes(self, x_inicial, y_inicial, direcao, tamanho):
        super().ocupar_posicoes(x_inicial, y_inicial, direcao, tamanho)


    
