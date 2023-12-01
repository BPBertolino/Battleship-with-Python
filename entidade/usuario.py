

class Usuario:
    
    def __init__(self, cpf = 0, nome = "", data_nascimento = "1 de janeiro de 1900", pontuacao = 0, pontuacao_acumulada = 0):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__pontuacao = 0
        self.__pontuacao_acumulada = 0

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def pontuacao(self):
        return self.__pontuacao

    @property
    def pontuacao_acumulada(self):
        return self.__pontuacao_acumulada
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
        
    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao
        
    @pontuacao_acumulada.setter
    def pontuacao_acumulada(self, pontuacao_acumulada):
        self.__pontuacao_acumulada = pontuacao_acumulada
