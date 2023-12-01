from entidade.jogo import Jogo
from limite.tela_jogo import TelaJogo
from DAOs.jogo_dao import JogoDAO
from controle.controle_usuario import ControladorUsuario
from controle.controle_jogada import ControladorJogada
from entidade.usuario import Usuario
from entidade.embarcacao import Embarcacao
from exception.usuario_existente_exception import UsuarioExistenteException
from exception.usuario_inexistente_exception import UsuarioInexistenteException
from exception.usuario_invalido_exception import UsuarioInvalidoException
import random


class ControladorJogo:
    
    def __init__(self, jogo: Jogo = None, tela_jogo: TelaJogo = None, controle_usuario: ControladorUsuario = None, controle_jogada: ControladorJogada = None):
        self.__jogo = None
        self.__tela_jogo = TelaJogo()
        self.__jogo_DAO = JogoDAO()
        self.__controle_usuario = ControladorUsuario()
        self.__controle_jogada = None
        
    def encontrar_ultimo_jogo(self):
        if len(self.__jogo_DAO.get_all_keys()) > 0:
            num_jogo = max(self.__jogo_DAO.get_all_keys())
        else:
            num_jogo = 1
        self.iniciar_jogo(num_jogo)
    
    def iniciar_jogo(self, num_jogo = 1):
        usuario0 = self.menu_jogo()
        if isinstance(usuario0, Usuario):
            self.__controle_usuario.add_usuario_pc()
            usuario1 = self.__controle_usuario.selecionar_usuario_por_dados(0)
            dimensao_N, dimensao_L = self.solicitar_dimensoes(num_jogo)
            self.criar_jogo(num_jogo, usuario0, usuario1, dimensao_N, dimensao_L)
        
    def menu_jogo(self):
        lista_opcoes_jogo = {1: self.definir_jogadores, 2: self.__controle_usuario.menu_usuario, 3: self.listar_jogos, 4: self.__controle_usuario.listar_usuarios_classificados, 5: self.sair}
        while True:
            funcao = 0
            opcao_escolhida = self.__tela_jogo.tela_opcoes()
            funcao_escolhida = lista_opcoes_jogo[opcao_escolhida]
            funcao = funcao_escolhida()
            if isinstance(funcao, Usuario):
                return funcao
            elif funcao == "sair":
                return "sair"
            
    def sair(self):
        return "sair"
                
    def definir_jogadores(self):
        while True:
            try:
                usuario = self.__controle_usuario.selecionar_usuario()
                if usuario is None:
                    raise UsuarioInexistenteException
                elif usuario.nome == "PC" or usuario.cpf == 0:
                    raise UsuarioInvalidoException
                return usuario
            except UsuarioInexistenteException:
                self.__tela_jogo.mostrar_mensagem("Selecione um usuario existente.")
                return 0
            except UsuarioInvalidoException:
                self.__tela_jogo.mostrar_mensagem("Selecione um usuario valido.")
                return 0
            
    def listar_jogos(self):
        dados_jogos = []
        lista_jogos = []
        for jog in self.__jogo_DAO.get_all():
            dados_jogos.append({"num_jogo":jog.num_jogo, "usuario0":jog.usuario0, "usuario1":jog.usuario1, "oceano0":jog.oceano0, "oceano1":jog.oceano1, "pontuacao_jogador":jog.pontuacao_jogador})
            lista_jogos.append(jog)
        self.__tela_jogo.tela_list(lista_jogos)
        return 0

    def solicitar_dimensoes(self, num_jogo):
        dimensoes = self.__tela_jogo.tela_dimensoes()
        if dimensoes == "cancelar":
            self.iniciar_jogo(num_jogo)
        else:
            dimensao_N = dimensoes["dimensao_N"]
            dimensao_L = dimensoes["dimensao_L"]
            return dimensao_N, dimensao_L

    def criar_jogo(self, num_jogo, usuario0, usuario1, dimensao_N, dimensao_L, pontuacao_jogador = 0):
        self.__jogo = Jogo(num_jogo, usuario0, usuario1, dimensao_N, dimensao_L, pontuacao_jogador)
        self.__jogo.usuario0.pontuacao = 0
        self.__jogo.usuario1.pontuacao = 0
        self.setup_pc(dimensao_N, dimensao_L)
        oceano0 = self.__jogo.oceano0
        oceano1 = self.__jogo.oceano1
        usuario0 = self.__jogo.usuario0
        usuario1 = self.__jogo.usuario1
        self.iniciar_jogadas(usuario0, usuario1, oceano0, oceano1, num_jogo)

    def setup_pc(self, dimensao_N, dimensao_L):
        lista_barcos = self.__jogo.oceano1.criar_frota()
        self.__jogo.oceano1.criar_matriz_oceano()
        i = 0
        while i < 8:
            x_inicial, y_inicial, direcao = self.distribuicao_aleatoria(dimensao_N, dimensao_L)
            barco = lista_barcos[i]
            barco.ocupar_posicoes(x_inicial, y_inicial, direcao, barco.tamanho)
            verifica_posicao = self.verifica_posicao_valida(barco, self.__jogo.oceano1)
            if verifica_posicao:
                self.__jogo.oceano1.povoar_oceano(barco.posicoes_ocupadas)
                self.__jogo.oceano1.posiconar_matriz_embarcacoes(barco.posicoes_ocupadas)
                i+=1

    def distribuicao_aleatoria(self, dimensao_N, dimensao_L):
        x_inicial = random.randint(0,dimensao_N-1)
        y_inicial = random.randint(0,dimensao_L-1)
        direcao = random.randint(0,1)
        return x_inicial, y_inicial, direcao
    
    def verifica_posicao_valida(self, barco, oceano):
        for item in barco.posicoes_ocupadas:
            if item in oceano.pontos_ocupados_oceano:
                barco.posicoes_ocupadas = []
                return False
            if item[0] > (oceano.dimensao_N-1) or item[1] > (oceano.dimensao_L-1):
                barco.posicoes_ocupadas = []
                return False 
        return True

    def iniciar_jogadas(self, jogador, pc, oceano0, oceano1, num_jogo):
        self.__controle_jogada = ControladorJogada(jogador, pc, oceano0, oceano1)
        continua_jogo = self.__controle_jogada.solicitar_barcos()
        if continua_jogo == False:
            self.iniciar_jogo(num_jogo)
        jogo_terminou = False
        jogo_terminou = self.__controle_jogada.fazer_jogada()
        if jogo_terminou == None:
            self.encerrar_jogo()    
    
    def encerrar_jogo(self):
        self.__jogo.usuario0.pontuacao_acumulada += self.__jogo.usuario0.pontuacao
        self.__jogo.usuario1.pontuacao_acumulada += self.__jogo.usuario1.pontuacao
        self.__jogo.pontuacao_jogador = self.__jogo.usuario0.pontuacao
        self.informar_resultado_jogo() 
        self.informar_relatorio()
        self.__jogo_DAO.add(self.__jogo)
        self.__controle_usuario.usuario_DAO.update(self.__jogo.usuario0)
        self.__controle_jogada.jogada_DAO.remove_all()
        num_jogo = self.__jogo.num_jogo + 1
        self.iniciar_jogo(num_jogo)
    
    def informar_resultado_jogo(self):
        pontuacao_maxima = 41
        if self.__jogo.usuario0.pontuacao == pontuacao_maxima:
            vencedor = self.__jogo.usuario0
            perdedor = self.__jogo.usuario1
        else:
            vencedor = self.__jogo.usuario1
            perdedor = self.__jogo.usuario0
        self.__tela_jogo.mostrar_mensagem(vencedor.nome + " venceu o jogo com " + str(vencedor.pontuacao) + " pontos, contra " + str(perdedor.pontuacao) + " do adversário " + perdedor.nome + ".")
    
    def informar_relatorio(self):
        lista_jogadas = []
        for jogada in self.__controle_jogada.lista_jogadas():
            item = (jogada.jogador.nome +  ", " + str(jogada.x) + ", " + str(jogada.y))
            lista_jogadas.append(item)
        self.__tela_jogo.tela_relatorio(lista_jogadas)

