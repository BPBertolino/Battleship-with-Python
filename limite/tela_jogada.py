from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg
from exception.campos_vazios_exception import CamposVaziosException


class TelaJogada(AbstractTela):

    def __init__(self, dimensao_N, dimensao_L):
        self.__dimensao_N = dimensao_N
        self.__dimensao_L = dimensao_L
    
    @property
    def dimensao_N(self):
        return self.__dimensao_N
    
    @property
    def dimensao_L(self):
        return self.__dimensao_L

    def cria_board(self, dimensao_N, dimensao_L, matriz_oceano, posicionamento = False, pc_joga = False):
        board = []
        for i in range(dimensao_N):
            linha = []
            for j in range(dimensao_L):
                if matriz_oceano[i][j] == 'E' and posicionamento == True:
                    linha.append(sg.Canvas(size=(28, 30), background_color='yellow', key= 'canvas'))
                elif matriz_oceano[i][j] == 'x':
                    linha.append(sg.Canvas(size=(28, 30), background_color='black', key= 'canvas'))
                elif matriz_oceano[i][j] == 'B':
                    linha.append(sg.Canvas(size=(28, 30), background_color='red', key= 'canvas'))
                elif matriz_oceano[i][j] == 0 and pc_joga == True:
                    linha.append(sg.Canvas(size=(28, 30), background_color='blue', key= 'canvas'))
                else: 
                    linha.append(sg.Button(' ', size=(4, 2), key=(i,j), pad=(0,0),auto_size_button = True, button_color=('blue')))          
            board.append(linha)
        return board
    
    def posicionamento_inicial(self, matriz_oceano, nome_barco, tamanho_barco, posicionamento):
        board = self.cria_board(self.__dimensao_N, self.__dimensao_L,matriz_oceano,True) 
        layout =  [[sg.Text('------ Posicione seus barcos no oceano ------', expand_x=True, justification='center', font=("Helvica", 15))],
                [sg.Text('No final, você tera posicionado:  ',  font=("Helvica", 10))],
                [sg.Text('3x Botes (1 bloco), 2x Submarinos (2 blocos), 2x Fragatas (3 blocos), 1x Porta aviao (4 blocos)',  font=("Helvica", 10))],
                [sg.Text('Escolha a posicao desejada para ' + nome_barco + ', embarcao de ' + str(tamanho_barco) + ' bloco(s)', font=("Helvica", 10))],
                board,
                [sg.Submit('Confirmar', tooltip='Confirme a posição escolhida'), sg.Cancel('Cancelar jogo', tooltip = "Volte para menu principal")]]
        
        window = sg.Window('Posicionar embarcações', layout)
        event_list = []
        while True:
            
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancelar jogo'):
                window.close()
                return "Cancelar"

            if event in (sg.Submit, 'Confirmar'):
                try:
                    if len(event_list) == tamanho_barco:
                        teste = self.testar_posicoes(event_list, tamanho_barco)
                        if teste == False :
                            self.mostrar_mensagem("Selecione quadrados lado a lado!")
                            raise CamposVaziosException
                        window.close()
                        return event_list
                #ERRO
                    else:
                        self.mostrar_mensagem("Selecione " + str(tamanho_barco) + " quadrado(s)!")
                        raise CamposVaziosException
                except CamposVaziosException:
                    window.close()
                    return 0
            if event != "Confirmar" and event != "Cancelar":
                if event not in event_list:
                    event_list.append(event)
                    window[event].update(board[event[0]][event[1]] , button_color=('yellow','yellow'))
                else:
                    event_list.remove(event)
                    window[event].update(board[event[0]][event[1]] , button_color=('blue','blue'))
    
    def testar_posicoes(self, lista_posicoes, tamanho):
        lista_posicoes.sort()
        x_inicial = lista_posicoes[0][0]
        y_inicial = lista_posicoes[0][1]
        posicoes_ocupadas = []
        if len(lista_posicoes) > 1 and lista_posicoes[0][0] == lista_posicoes[1][0]:
            direcao = 0
        else:
            direcao =  1
        for i in range (tamanho):
            #caso horizontal
            if direcao == 0:
                posicoes_ocupadas.append((x_inicial,y_inicial+i))
            #caso vertical
            else:
                posicoes_ocupadas.append((x_inicial+i,y_inicial))
        if posicoes_ocupadas == lista_posicoes:
            return True
        else:
            return False

    def tela_fazer_jogada(self, matriz_usuario_jogando, matriz_pc_jogando, nome_jogador, pontos_parciais_jogador, pontos_parciais_pc, num_jogada):
        #coluna onde jogador joga
        coluna_0 = sg.Column( self.cria_board(self.__dimensao_N,self.__dimensao_L,matriz_usuario_jogando) )
        #coluna onde oceano joga
        coluna_1 = sg.Column( self.cria_board(self.__dimensao_N,self.__dimensao_L,matriz_pc_jogando, True, True))
        layout =[[sg.Text('--------- Realize sua jogada ---------', expand_x=True, justification='center',font=("Helvica", 20))],
                [sg.Text('Jogada de nº ' + str(num_jogada) + '. Clique onde deseja atirar e confirme:  ', font=("Helvica", 10))],
                [coluna_0, sg.VerticalSeparator(), coluna_1],
                [sg.Text('Pontuação parcial de ' + nome_jogador + ": " + str(pontos_parciais_jogador) , font=("Helvica", 15)), sg.Text('Pontuação parcial de PC: ' + str(pontos_parciais_pc) ,   expand_x=True, justification='right', font=("Helvica", 15))],
                [sg.Submit('Confirmar', tooltip='Confirme a posição escolhida'), sg.Cancel('Cancelar jogo')]]
        window = sg.Window('Batalha Naval', layout)
        event_list = []
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar jogo'):
                window.close()
                return "Cancelar"

            if event in (sg.Submit, 'Confirmar'):
                try:
                    if len(event_list) == 1:
                        window.close()
                        return event_list
                #ERRO
                    else:
                        self.mostrar_mensagem("Selecione 1 quadrado")
                        raise CamposVaziosException
                except CamposVaziosException:
                    window.close()
                    return 0
            if event != "Confirmar" and event != "Cancelar":
                if event not in event_list:
                    event_list.append(event)
                    window[event].update(button_color=('yellow','yellow'))
                else:
                    event_list.remove(event)
                    window[event].update( button_color=('blue','blue'))
        window.close()

