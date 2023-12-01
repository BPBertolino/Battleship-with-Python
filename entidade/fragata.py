

import sys

from entidade.embarcacao import Embarcacao


class Fragata(Embarcacao):

    def __init__(self):
        super().__init__()
        self.tamanho = 3
        self.nome = "Fragata"
    
    def ocupar_posicoes(self, x_inicial, y_inicial, direcao, tamanho):
        super().ocupar_posicoes(x_inicial, y_inicial, direcao, tamanho)
