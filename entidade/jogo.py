from entidade.oceano import Oceano


class Jogo:
    
    def __init__(self, num_jogo, usuario0, usuario1, dimensao_N, dimensao_L, pontuacao_jogador):
        self.__num_jogo = num_jogo
        self.__usuario0 = usuario0
        self.__usuario1 = usuario1
        self.__oceano0 = Oceano(dimensao_N, dimensao_L)
        self.__oceano1 = Oceano(dimensao_N, dimensao_L)
        self.__pontuacao_jogador = pontuacao_jogador

    @property
    def num_jogo(self):
        return self.__num_jogo

    @property
    def usuario0(self):
        return self.__usuario0
    
    @property
    def usuario1(self):
        return self.__usuario1
    
    @property
    def oceano0(self):
        return self.__oceano0
    
    @property
    def oceano1(self):
        return self.__oceano1
    
    @property
    def pontuacao_jogador(self):
        return self.__pontuacao_jogador
    
    @num_jogo.setter
    def num_jogo(self, num_jogo):
        self.__num_jogo = num_jogo
    
    @usuario0.setter
    def usuario0(self, usuario0):
        self.__usuario0 = usuario0
    
    @usuario1.setter
    def usuario1(self, usuario1):
        self.__usuario1 = usuario1
        
    @oceano0.setter
    def oceano0(self, oceano0):
        self.__oceano0 = oceano0
    
    @oceano1.setter
    def oceano1(self, oceano1):
        self.__oceano1 = oceano1
        
    @pontuacao_jogador.setter
    def pontuacao_jogador(self, pontuacao_jogador):
        self.__pontuacao_jogador = pontuacao_jogador

    def listar_jogadores(self):
        return self.__usuario0.nome, self.__usuario1.nome
