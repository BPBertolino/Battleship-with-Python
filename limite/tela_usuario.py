from limite.abstract_tela import AbstractTela
from exception.cpf_invalido_exception import CPFInvalidoException
from exception.usuario_invalido_exception import UsuarioInvalidoException
from exception.data_nasc_invalida_exception import DataNascimentoInvalidaException
import PySimpleGUI as sg


class TelaUsuario(AbstractTela):
   
    def __init__(self):
        self.init_opcoes()
        
    def print_lista(self, lista):
        text = ""
        for usu in lista:
            text += "CPF: " + str(usu.cpf) + "\n" + " Nome: " + usu.nome + "\n" + " Data de nascimento: " + usu.data_nascimento + "\n" + " Pontuação: " + str(usu.pontuacao) + "\n" + " Pontuação acumulada: " + str(usu.pontuacao_acumulada) + "\n"
        return text
        
    def print_lista_rank(self, lista):
        text = ""
        for usu in lista:
            text += str(lista.index(usu) + 1) + " --- Jogador: " + str(usu.cpf) + " - " + usu.nome + " com " + str(usu.pontuacao_acumulada) + " pontos." + "\n"
        return text

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values["1"]:
            opcao = 1
        if values["2"]:
            opcao = 2
        if values["3"]:
            opcao = 3
        if values["4"]:
            opcao = 4
        if values["5"] or button in (None, "Voltar"):
            opcao = 5
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ BATALHA NAVAL ------", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Criar cadastro", "RD1", key="1")],
            [sg.Radio("Alterar cadastro", "RD1", key="2")],
            [sg.Radio("Apagar cadastro", "RD1", key="3")],
            [sg.Radio("Listar usuários", "RD1", key="4")],
            [sg.Radio("Voltar ao menu do jogo", "RD1", key="5")],
            [sg.Button("Confirmar"), sg.Cancel("Voltar")]
        ]
        self.window = sg.Window("Cadastro de usuários - Batalha Naval").Layout(layout)
 
    def tela_add(self):
        self.init_add()
        while True:
            button, values = self.open()
            if button == "Confirmar":
                try:
                    if ((self.checa_numero_inteiro(values["cpf"])) and (values["cpf"] != "")):            
                        cpf = values["cpf"]
                    else:
                        raise CPFInvalidoException
                    if ((values["nome"] != "PC") and (values["nome"] != "")):
                        nome = values["nome"]
                    else:
                        raise UsuarioInvalidoException
                    if self.checa_data_nasc(values["data_nasc"]):
                        data_nascimento = values["data_nasc"]
                    else:
                        raise DataNascimentoInvalidaException
                    self.close()
                    return {"cpf": int(cpf), "nome": nome, "data_nasc": data_nascimento, "pontuacao": 0, "pontuacao_acum": 0}
                except CPFInvalidoException:
                    self.mostrar_mensagem("CPF inválido. Insira um número inteiro.")
                except UsuarioInvalidoException:
                    self.mostrar_mensagem("Insira um nome válido.")
                except DataNascimentoInvalidaException:
                    self.mostrar_mensagem("Insira uma data de nascimento válida.")
            else:
                self.close()
                return None
        
    def init_add(self):
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ CRIAR CADASTRO ------", font=("Helvica", 25))],
            [sg.Text("Insira os dados do novo usuário", font=("Helvica", 15))],
            [sg.Text("CPF: ", font=("Helvica", 15)), sg.InputText("", key="cpf")],
            [sg.Text("Nome: ", font=("Helvica", 15)), sg.InputText("", key="nome")],
            [sg.Text("Data de nascimento: ", font=("Helvica", 15)), sg.InputText("", key="data_nasc"),
             sg.CalendarButton("Selecione a data", close_when_date_chosen = True, target="data_nasc", format="%d:%m:%Y")],
            [sg.Button("Confirmar"), sg.Cancel("Voltar")]
        ]
        self.window = sg.Window("Adicionar usuário - Batalha Naval").Layout(layout)

    def tela_alt_antigos(self):
        self.init_alt_antigos()
        while True:
            button, values = self.open()
            if button == "Confirmar":
                try:
                    if ((self.checa_numero_inteiro(values["cpf"])) and (values["cpf"] != "")):
                        cpf = values["cpf"]
                    else:
                        raise CPFInvalidoException
                    self.close()
                    return int(cpf)
                except CPFInvalidoException:
                    self.mostrar_mensagem("CPF inválido. Insira um número inteiro.")
            else:
                self.close()
                return None

    def init_alt_antigos(self):
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ ALTERAR CADASTRO ------", font=("Helvica", 25))],
            [sg.Text("Insira o cpf do usuário", font=("Helvica", 15))],
            [sg.Text("CPF: ", font=("Helvica", 15)), sg.InputText("", key="cpf")],
            [sg.Button("Confirmar"), sg.Cancel("Voltar")]
        ]
        self.window = sg.Window("Alterar usuário - Batalha Naval").Layout(layout)

    def tela_alt_novos(self):
        self.init_alt_novos()
        while True:
            button, values = self.open()
            if button == "Confirmar":
                try:
                    if ((values["nome"] != "PC") and (values["nome"] != "")):
                        nome = values["nome"]
                    else:
                        raise UsuarioInvalidoException
                    if self.checa_data_nasc(values["data_nasc"]):
                        data_nascimento = values["data_nasc"]
                    else:
                        raise DataNascimentoInvalidaException
                    self.close()
                    return {"nome": nome, "data_nasc": data_nascimento}
                except UsuarioInvalidoException:
                    self.mostrar_mensagem("Insira um nome válido.")
                except DataNascimentoInvalidaException:
                    self.mostrar_mensagem("Insira uma data de nascimento válida.")
            else:
                self.close()
                return None                 
        
    def init_alt_novos(self):
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ ALTERAR CADASTRO ------", font=("Helvica", 25))],
            [sg.Text("Insira os dados novos", font=("Helvica", 15))],
            [sg.Text("Nome: ", font=("Helvica", 15)), sg.InputText("", key="nome")],
            [sg.Text("Data de nascimento: ", font=("Helvica", 15)), sg.InputText("", key="data_nasc"),
             sg.CalendarButton("Selecione a data", close_when_date_chosen = True, target="data_nasc", format="%d:%m:%Y")],
            [sg.Button("Confirmar"), sg.Cancel("Voltar")]
        ]
        self.window = sg.Window("Alterar usuário - Batalha Naval").Layout(layout)
 
    def tela_rem(self):
        self.init_rem()
        while True:
            button, values = self.open()
            if button == "Confirmar":
                try:
                    if ((self.checa_numero_inteiro(values["cpf"])) and (values["cpf"] != "")):
                        cpf = values["cpf"]
                    else:
                        raise CPFInvalidoException
                    self.close()
                    return int(cpf)
                except CPFInvalidoException:
                    self.mostrar_mensagem("CPF inválido. Insira um número inteiro.")
            else:
                self.close()
                return None 
    
    def init_rem(self):
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ APAGAR CADASTRO ------", font=("Helvica", 25))],
            [sg.Text("Insira o cpf do usuário", font=("Helvica", 15))],
            [sg.Text("CPF: ", font=("Helvica", 15)), sg.InputText("", key="cpf")],
            [sg.Button("Confirmar"), sg.Cancel("Voltar")]
        ]
        self.window = sg.Window("Apagar usuário - Batalha Naval").Layout(layout)

    def tela_list(self, lista):
        self.init_list(lista)
        button, values = self.open()
        self.close()
        return lista
        
    def init_list(self, lista):
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ LISTA DE USUÁRIOS ------", font=("Helvica", 25))],
            [sg.Text(self.print_lista(lista), font=("Helvica", 15))], 
            [sg.Cancel("Voltar")]
        ]
        self.window = sg.Window("Listar usuários - Batalha Naval").Layout(layout)
        
    def tela_list_rank(self, lista):
        self.init_list_rank(lista)
        button, values = self.open()
        self.close()
        return lista
        
    def init_list_rank(self, lista):
        sg.ChangeLookAndFeel("LightBlue4")
        layout = [
            [sg.Text("------ CLASSIFICAÇÃO ------", font=("Helvica", 25))],
            [sg.Text(self.print_lista_rank(lista), font=("Helvica", 15))],
            [sg.Cancel("Voltar")]
        ]
        self.window = sg.Window('Classificar usuários - Batalha Naval').Layout(layout)
    
    def tela_sel(self, lista):
        lista_nomes = []
        for usu in lista:
            if usu.cpf > 0:
                lista_nomes.append(str(usu.cpf) + ": " + usu.nome)
        self.init_sel(lista_nomes)
        while True:
            button, values = self.open()
            if ((values['-COMBO-'] != "") and button == "Confirmar"):
                self.close()
                cpf_jogador = int(values['-COMBO-'].split(":")[0])
                return cpf_jogador
    
    def init_sel(self, lista_nomes):
        sg.ChangeLookAndFeel("LightBlue4")
        combobox = sg.Combo((lista_nomes), font=("Helvica", 15),  expand_x=True, enable_events=True,  readonly=False, key='-COMBO-')
        layout = [
            [sg.Text("------ SELECIONAR JOGADOR ------", font=("Helvica", 25))],
            [sg.Text("Escolha o jogador", font=("Helvica", 15))],
            [combobox],
            [sg.Button("Confirmar"), sg.Cancel("Voltar")]
        ]
        self.window = sg.Window("Selecionar jogador - Batalha Naval").Layout(layout)    
