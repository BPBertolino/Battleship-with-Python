from abc import ABC, abstractmethod

class Embarcacao(ABC):

    @abstractmethod
    def __init__(self):
        self.__posicoes_ocupadas = []
        self.__tamanho = 0
        self.__nome = ""

    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self,tamanho):
        self.__tamanho = tamanho
    
    @property
    def posicoes_ocupadas(self):
        return self.__posicoes_ocupadas
    
    @posicoes_ocupadas.setter
    def posicoes_ocupadas(self, posicoes_ocupadas):
        self.__posicoes_ocupadas = posicoes_ocupadas
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    #adicionar posicoes ocupadas - em ControleJogo
    @abstractmethod
    def ocupar_posicoes(self, x_inicial, y_inicial, direcao, tamanho):
        for i in range (tamanho):
            #caso horizontal
            if direcao == 0:
                self.posicoes_ocupadas.append([x_inicial,y_inicial+i])
            #caso vertical
            else:
                self.posicoes_ocupadas.append([x_inicial+i,y_inicial])
        return self.posicoes_ocupadas

