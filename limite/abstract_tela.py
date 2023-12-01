from abc import ABC, abstractmethod, abstractproperty
import PySimpleGUI as sg
from pickle import TRUE


class AbstractTela(ABC):

    def __init__(self):
        self.__window = None

    @property
    def window(self):
        return self.__window
    
    @window.setter
    def window(self, window):
        self.__window = window
        
    def checa_data_nasc(self, data_nasc):
        eh_valida = False
        try:
            data_nasc = data_nasc.split(":")
            if not ((len(data_nasc) == 3) and (self.checa_ano(data_nasc[2])) and (self.checa_mes(data_nasc[1])) and (self.checa_dia(data_nasc[2], data_nasc[1], data_nasc[0]))):
                raise ValueError
            else:
                eh_valida = True
                return eh_valida
        except ValueError:
            print("Valor incorreto. Insira uma data de nascimento válida usando o calendário.")

    def checa_ano(self, ano):
        ano_valido = False
        if self.checa_numero_inteiro_limitado(ano, 2023):
            ano_valido = True
            return ano_valido
        
    def checa_mes(self, mes):
        mes_valido = False
        if self.checa_numero_inteiro_limitado(mes, 12):
            mes_valido = True
            return mes_valido
        
    def checa_dia(self, ano, mes, dia):
        dia_valido = False
        if (self.checa_numero_inteiro(ano) and (self.checa_numero_inteiro(mes)) and (self.checa_numero_inteiro(dia))):
            ano = int(ano)
            mes = int(mes)
            if mes == 2:
                if ((ano % 4 == 0) and (ano != 2000)):
                    limite = 29
                else:
                    limite = 28
            elif ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)):
                limite = 30
            else:
                limite = 31
        if self.checa_numero_inteiro_limitado(dia, limite):
            dia_valido = True
            return dia_valido

    def checa_numero_inteiro(self, inteiro):
        eh_inteiro = False
        try:
            inteiro = int(inteiro)
            if not isinstance(inteiro, int):
                raise ValueError
            else:
                eh_inteiro = True
                return eh_inteiro
        except ValueError:
            print("Valor incorreto. Digite um número inteiro válido.")
            
    def checa_numero_inteiro_limitado(self, inteiro, limite: int = 0):
        eh_valido = False
        try:
            inteiro = int(inteiro)
            if ((inteiro > limite) or (inteiro <= 0)):
                raise ValueError
            else:
                eh_valido = True
                return eh_valido
        except ValueError:
            print("Valor incorreto. Digite um número inteiro positivo até " , limite)
            
    def le_numero_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto. Digite um número inteiro válido.")
                if inteiros_validos:
                    print("Valores válidos: ", inteiros_validos)

    def le_numero_inteiro_limitado(self, mensagem: str = "", inteiro_maximo: int = 0):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if ((inteiro > inteiro_maximo) or (inteiro <= 0)):
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto. Digite um número inteiro positivo até " , inteiro_maximo)

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
