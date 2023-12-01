

class Jogada:

    def __init__(self, num_jogada, jogador, x_atingido, y_atingido, pontuacao):
        self.__num_jogada = num_jogada
        self.__jogador = jogador
        self.__x = x_atingido
        self.__y = y_atingido
        self.__pontos = pontuacao

    @property
    def num_jogada(self):
        return self.__num_jogada
    
    @num_jogada.setter
    def num_jogada(self,num_jogada):
        self.__num_jogada = num_jogada

    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def jogador(self,jogador):
        self.__jogador = jogador

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x_atingido):
        self.__x = x_atingido

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,y_atingido):
        self.__y = y_atingido

    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self,pontuacao):
        self.__pontos = pontuacao
