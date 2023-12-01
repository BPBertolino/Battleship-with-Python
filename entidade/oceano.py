from entidade.bote import Bote
from entidade.submarino import Submarino
from entidade.fragata import Fragata
from entidade.porta_avioes import Porta_avioes
from entidade.embarcacao import Embarcacao

class Oceano:
    def __init__(self, dimensao_N, dimensao_L):
        self.__dimensao_N = dimensao_N
        self.__dimensao_L = dimensao_L
        self.__lista_barcos = []
        self.__pontos_ocupados_oceano = []
        self.__matriz_oceano = []

    @property
    def dimensao_N(self):
        return self.__dimensao_N
    
    @property
    def dimensao_L(self):
        return self.__dimensao_L
    
    @property
    def lista_barcos(self):
        return self.__lista_barcos
    
    @property
    def pontos_ocupados_oceano(self):
        return self.__pontos_ocupados_oceano
    
    @property
    def matriz_oceano(self):
        return self.__matriz_oceano
    
    @matriz_oceano.setter
    def matriz_oceano(self, matriz_oceano):
        self.__matriz_oceano = matriz_oceano
    
    def criar_matriz_oceano(self):
        for linha in range(self.__dimensao_N):
            l = [0]*self.__dimensao_L
            self.__matriz_oceano.append(l)

    def posiconar_matriz_embarcacoes(self, pontos_ocupados_embarcacao):
        for posicao in pontos_ocupados_embarcacao:
            x = posicao[0]
            y = posicao[1]
            self.__matriz_oceano[x][y] = "E"

    #em controleJogo    
    #a frota é criada junto com criação de jogo e oceano
    #a frota é sempre a mesma
    def criar_frota(self):
        bote1 = Bote()
        bote2 = Bote()
        bote3 = Bote()
        submarino1 = Submarino()
        submarino2 = Submarino()
        fragata1 = Fragata()
        fragata2 = Fragata()
        porta_avioes1 = Porta_avioes()
        self.__lista_barcos.append(bote1)
        self.__lista_barcos.append(bote2)
        self.__lista_barcos.append(bote3)
        self.__lista_barcos.append(submarino1)
        self.__lista_barcos.append(submarino2)
        self.__lista_barcos.append(fragata1)
        self.__lista_barcos.append(fragata2)
        self.__lista_barcos.append(porta_avioes1)

        return self.__lista_barcos

    #em controleJogo
    #quando o usuario colocar alguma posicoes de barco, esses serao add na lista
    def povoar_oceano(self, pontos_ocupados_embarcacao):
        for posicao in pontos_ocupados_embarcacao:
            self.__pontos_ocupados_oceano.append(posicao)
        
        return self.__pontos_ocupados_oceano   

    #em controleJogada
    def verificar_tiro(self, x_atingido, y_atingido):
        pontuacao_tiro = 0
        self.__matriz_oceano[x_atingido][y_atingido] = "x"
        for i in range(len(self.__pontos_ocupados_oceano)):
            if self.__pontos_ocupados_oceano[i] == [x_atingido,y_atingido]:
                self.__pontos_ocupados_oceano.remove([x_atingido,y_atingido])
                self.__matriz_oceano[x_atingido][y_atingido] = "B"
                #procurar qual embarcacao foi atingida
                for barco in self.__lista_barcos:
                    if [x_atingido,y_atingido] in barco.posicoes_ocupadas:
                        pontuacao_tiro = 1
                        barco.posicoes_ocupadas.remove([x_atingido,y_atingido])
                        if barco.posicoes_ocupadas == []:
                            pontuacao_tiro = 4
                        return pontuacao_tiro
                pontuacao_tiro = 1
                return pontuacao_tiro
        return pontuacao_tiro
        

