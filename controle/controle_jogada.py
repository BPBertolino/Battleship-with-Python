import random
from entidade.oceano import Oceano
from entidade.jogada import Jogada
from limite.tela_jogada import TelaJogada
from DAOs.jogada_dao import JogadaDAO

class ControladorJogada:

    def __init__(self, jogador_inicial, jogador_pc, oceano0, oceano1):
        
        self.__jogada_DAO = JogadaDAO()        

        self.__jogador0 = jogador_inicial
        self.__jogador1 = jogador_pc

        self.__oceano0 = oceano0
        self.__oceano1 = oceano1
        self.__tela_jogada = TelaJogada(self.__oceano0.dimensao_N, self.__oceano0.dimensao_L)
        self.__lista_jogadas = []

        self.__pontuacao_maxima = 41

    @property
    def jogada_DAO(self):
        return self.__jogada_DAO
        
    def solicitar_barcos(self):
        lista_barcos = self.__oceano0.criar_frota()
        self.__oceano0.criar_matriz_oceano()
        #Print somente para apresentação!
        print("matriz pc:", self.__oceano1.matriz_oceano)
        for b in lista_barcos:
            lista_eventos = self.__tela_jogada.posicionamento_inicial(self.__oceano0.matriz_oceano, b.nome, b.tamanho, True)
            #caso usuario não selecione posicoes
            while lista_eventos == 0:
                lista_eventos = self.__tela_jogada.posicionamento_inicial(self.__oceano0.matriz_oceano, b.nome, b.tamanho, True)
            if lista_eventos == "Cancelar":
                return False
            lista_eventos.sort()
            direcao = self.adivinha_direcao(lista_eventos)
            b.ocupar_posicoes(lista_eventos[0][0], lista_eventos[0][1], direcao, b.tamanho)
            self.__oceano0.povoar_oceano(b.posicoes_ocupadas)
            self.__oceano0.posiconar_matriz_embarcacoes(b.posicoes_ocupadas)
        return True

    #identificar qual direcao o barco foi posicionado
    def adivinha_direcao(self, lista):
        if len(lista) > 1:
            if lista[0][0] == lista[1][0]:
                return 0
            else:
                return 1
        return 0

    #fazer jogada do usuario pessoa
    def fazer_jogada(self, num_jogada = 1):
        end_game = False
        jogador = True
        #jogada do usuario pessoa
        x_escolhido, y_escolhido = self.solicita_jogada(num_jogada)
        if x_escolhido == "Cancelar":
            return False
        pontuacao_jogada = self.verifica_tiro(jogador, x_escolhido, y_escolhido)
        self.add_jogada(num_jogada, self.__jogador0, x_escolhido, y_escolhido, pontuacao_jogada) 
        end_game = self.le_pontuacao(jogador)
        if  end_game == True:
            return end_game
        elif pontuacao_jogada > 0:
            self.__tela_jogada.mostrar_mensagem("Você acertou tiro! Jogue novamente")
            num_jogada += 1
            self.fazer_jogada(num_jogada)
        else:
            self.__tela_jogada.mostrar_mensagem("Você errou o tiro! Aguarde PC jogar.")
            num_jogada += 1
            self.fazer_jogada_pc(num_jogada)

    def fazer_jogada_pc(self, num_jogada):
        jogador = False
        self.__tela_jogada.mostrar_mensagem("O PC está fazendo a jogada!")
        x_escolhido, y_escolhido  = self.tiro_aleatorio()
        pontuacao_jogada = self.verifica_tiro(jogador, x_escolhido, y_escolhido)
        self.add_jogada(num_jogada, self.__jogador1, x_escolhido, y_escolhido, pontuacao_jogada) 
        end_game = self.le_pontuacao(jogador)

        if  end_game:
            return end_game
        elif pontuacao_jogada > 0:
            self.__tela_jogada.mostrar_mensagem("PC acertou tiro! PC joga novamente")
            num_jogada += 1
            self.fazer_jogada_pc(num_jogada)
        else:
            self.__tela_jogada.mostrar_mensagem("PC errou tiro! Jogue novamente.")
            num_jogada += 1
            self.fazer_jogada(num_jogada)
    
    def tiro_aleatorio(self):
        x_escolhido = random.randint(0,self.__oceano1.dimensao_N-1)
        y_escolhido = random.randint(0,self.__oceano1.dimensao_L-1)
        if [x_escolhido,y_escolhido] in self.__lista_jogadas:
            if self.__lista_jogadas.jogador == self.__jogador1:
                self.tiro_aleatorio()
        return x_escolhido, y_escolhido

    def solicita_jogada(self, num_jogada):
        lista_eventos = self.__tela_jogada.tela_fazer_jogada(self.__oceano1.matriz_oceano, self.__oceano0.matriz_oceano, 
                                                             self.__jogador0.nome, self.__jogador0.pontuacao, self.__jogador1.pontuacao, num_jogada)
        while lista_eventos == 0:
            lista_eventos = self.__tela_jogada.tela_fazer_jogada(self.__oceano1.matriz_oceano, self.__oceano0.matriz_oceano, 
                                                             self.__jogador0.nome, self.__jogador0.pontuacao,self.__jogador1.pontuacao, num_jogada)
        if lista_eventos == "Cancelar":
            return "Cancelar",  "Cancelar"

        return lista_eventos[0][0], lista_eventos[0][1]

    def verifica_tiro(self, jogador, x_atingido, y_atingido):
        #jogador
        if jogador:
            pontuacao_nova = self.__oceano1.verificar_tiro(x_atingido, y_atingido)
            self.__jogador0.pontuacao += int(pontuacao_nova)
            return int(pontuacao_nova)
        #pc
        else:
            pontuacao_nova = self.__oceano0.verificar_tiro(x_atingido, y_atingido)
            self.__jogador1.pontuacao += int(pontuacao_nova)
            return int(pontuacao_nova)

    def add_jogada(self, num_jogada, jogador, x_atingido, y_atingido, pontuacao):
        nova_jogada = Jogada(num_jogada, jogador, x_atingido, y_atingido, pontuacao)
        self.__jogada_DAO.add(nova_jogada)
        self.__lista_jogadas.append(nova_jogada)

    def le_pontuacao(self, jogador):
        if (jogador and self.__jogador0.pontuacao == self.__pontuacao_maxima):
            self.__tela_jogada.mostrar_mensagem("Você venceu!")
            return True
        elif (not jogador and self.__jogador1.pontuacao == self.__pontuacao_maxima):
            self.__tela_jogada.mostrar_mensagem("PC venceu!")
            return True
        else:
            return False

    def lista_jogadas(self):
        return self.__lista_jogadas
    