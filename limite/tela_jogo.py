from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaJogo(AbstractTela):

    def __init__(self):
        self.init_opcoes()
        
    def print_lista(self, lista):
        text = ""
        for jog in lista:
            if jog.pontuacao_jogador == 41:
                vit = " venceu o jogo com "
            else:
                vit = " perdeu o jogo com "
            text += str(jog.num_jogo) + " --- " + "Jogador: " + str(jog.usuario0.cpf) + " - " + jog.usuario0.nome + vit + str(jog.pontuacao_jogador) + " pontos." + "\n"
        return text
    
    def print_lista2(self, lista):
        text = ""
        for jog in lista:
            text += jog + "\n"
        return text

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if button in (None, 'Sair'):
            opcao = 5
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBlue4')
        layout = [
            [sg.Text('------ BATALHA NAVAL ------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Iniciar novo jogo', "RD1", key='1')],
            [sg.Radio('Cadastro de usuários', "RD1", key='2')],
            [sg.Radio('Histórico de jogos', "RD1", key='3')],
            [sg.Radio('Classificação', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Sair')]
        ]
        self.window = sg.Window('Batalha Naval').Layout(layout)
        
    def tela_dimensoes(self):  
        self.init_dimensoes()
        button, values = self.open()
        dimensao_N = int(values["v"])
        dimensao_L = int(values["h"])
        if button in (None, "Cancelar jogo"):
            self.close()            
            return "cancelar"
        self.close()
        return {"dimensao_N": dimensao_N, "dimensao_L": dimensao_L}
        
    def init_dimensoes(self):   
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ ESCOLHER DIMENSÕES ------", font=("Helvica", 25))],
            [sg.Text("Escolha as dimensões dos oceanos", font=("Helvica", 15))],
            [sg.Text("Horizontal: ", font=("Helvica", 15)), sg.Slider(range=(8, 16), orientation='h', size=(28, 20), default_value=8, key = 'h')],
            [sg.Text("Vertical: ", font=("Helvica", 15)), sg.Slider(range=(16, 8), orientation='v', size=(12, 20), default_value=8, key = 'v')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar jogo")]
        ]
        self.window = sg.Window("Escolher dimensões - Batalha Naval").Layout(layout)  
        
    def tela_list(self, lista):
        self.init_list(lista)
        button, values = self.open()
        self.close()
        return lista
        
    def init_list(self, lista):
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ HISTÓRICO DE JOGOS ------", font=("Helvica", 25))],
            [sg.Text(self.print_lista(lista), font=("Helvica", 15))], 
            [sg.Cancel("Voltar")]
        ]
        self.window = sg.Window("Listar jogos - Batalha Naval").Layout(layout)
        
    def tela_relatorio(self, lista):
        self.init_relatorio(lista)
        button, values = self.open()
        self.close()
        return lista
        
    def init_relatorio(self, lista):
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ SÉRIE DE JOGADAS ------", font=("Helvica", 25))],
            [sg.Text("Relatorio final: [jogador][x][y] ", font=("Helvica", 15))],
            [sg.Text(self.print_lista2(lista), font=("Helvica", 10))], 
            [sg.Cancel("Voltar")]
        ]
        self.window = sg.Window("Listar jogadas - Batalha Naval").Layout(layout)
