from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario
from DAOs.usuario_dao import UsuarioDAO
from exception.usuario_existente_exception import UsuarioExistenteException
from exception.usuario_inexistente_exception import UsuarioInexistenteException
from exception.usuario_invalido_exception import UsuarioInvalidoException
from exception.campos_vazios_exception import CamposVaziosException


class ControladorUsuario:

    def __init__(self, tela_usuario: TelaUsuario = None, lista_usuarios = []):
        self.__tela_usuario = TelaUsuario()
        self.__usuario_DAO = UsuarioDAO()
        
    @property
    def usuario_DAO(self):
        return self.__usuario_DAO
        
    def selecionar_usuario(self):
        lista_usuarios = []        
        for usu in self.__usuario_DAO.get_all():
            lista_usuarios.append(usu)
        usuario = self.selecionar_usuario_por_dados(self.__tela_usuario.tela_sel(lista_usuarios))
        return usuario

    def selecionar_usuario_por_dados(self, cpf):
        for usu in self.__usuario_DAO.get_all():
            if (usu.cpf == cpf):
                return usu
        return None

    def menu_usuario(self):
        lista_opcoes_usuario = {1: self.add_usuario, 2: self.alt_usuario, 3: self.rem_usuario, 4: self.listar_usuarios, 5: self.retornar}
        while True:
            opcao_escolhida = self.__tela_usuario.tela_opcoes()
            funcao_escolhida = lista_opcoes_usuario[opcao_escolhida]
            funcao = funcao_escolhida()
            if isinstance(funcao, Usuario):
                return funcao
            elif funcao == "voltar":
                return "voltar"
            
    def retornar(self):
        return "voltar"
    
    def listar_usuarios(self):
        lista_usuarios = []
        for usu in self.__usuario_DAO.get_all():
            lista_usuarios.append(usu)
        self.__tela_usuario.tela_list(lista_usuarios)
        return 0
    
    def listar_usuarios_classificados(self):
        dados_usuarios = []
        lista_usuarios = []
        for usu in self.__usuario_DAO.get_all():
            dados_usuarios.append({"cpf":usu.cpf, "nome":usu.nome, "data_nasc":usu.data_nascimento, "pontuacao":usu.pontuacao, "pontuacao_acum":usu.pontuacao_acumulada})
            lista_usuarios.append(usu)
        lista_usuarios.sort(key = lambda x: x.pontuacao_acumulada, reverse = True)
        self.__tela_usuario.tela_list_rank(lista_usuarios)
        return 0
    
    def add_usuario(self):
        dados_usuario = self.__tela_usuario.tela_add()
        try:
            if dados_usuario is not None: 
                usuario = Usuario(dados_usuario["cpf"], dados_usuario["nome"], dados_usuario["data_nasc"], dados_usuario["pontuacao"], dados_usuario["pontuacao_acum"])
            else:
                raise CamposVaziosException
            try:
                if self.selecionar_usuario_por_dados(dados_usuario["cpf"]) is not None:
                    raise UsuarioExistenteException
                self.__usuario_DAO.add(usuario)
                return 0
            except UsuarioExistenteException or KeyError:
                self.__tela_usuario.mostrar_mensagem("Se quiser jogar com este usuário, inicie um novo jogo e o selecione.")
                return 0
        except CamposVaziosException:
            self.__tela_usuario.mostrar_mensagem("Insira os dados e clique em Confirmar.")
            return 0

    def add_usuario_pc(self):
        usuario = Usuario(0, "PC", "01:01:1900", 0, 0)
        for usu in self.__usuario_DAO.get_all():
            if usu.nome == "PC":
                return
        self.__usuario_DAO.add(usuario) 
        return 0
            
    def rem_usuario(self):
        while True:
            try:
                usuario = self.selecionar_usuario_por_dados(self.__tela_usuario.tela_rem())
                if usuario is None:
                    raise UsuarioInexistenteException
                elif usuario.nome == "PC" or usuario.cpf == 0:
                    raise UsuarioInvalidoException
                self.__usuario_DAO.remove(usuario.cpf)          
                return 0
            except UsuarioInexistenteException:
                self.__tela_usuario.mostrar_mensagem("Selecione um usuário existente.")
                return 0
            except UsuarioInvalidoException:
                self.__tela_usuario.mostrar_mensagem("Selecione um usuário válido.")
                return 0
    
    def alt_usuario(self):
        while True:
            try:
                usuario = self.selecionar_usuario_por_dados(self.__tela_usuario.tela_alt_antigos())
                if usuario is None:
                    raise UsuarioInexistenteException
                elif usuario.nome == "PC" or usuario.cpf == 0:
                    raise UsuarioInvalidoException
                dados_usuario = self.__tela_usuario.tela_alt_novos()
                usuario.nome = dados_usuario["nome"]
                usuario.data_nascimento = dados_usuario["data_nasc"]
                self.__usuario_DAO.update(usuario) 
                return 0
            except UsuarioInexistenteException:
                self.__tela_usuario.mostrar_mensagem("Selecione um usuário existente.")
                return 0
            except UsuarioInvalidoException:
                self.__tela_usuario.mostrar_mensagem("Selecione um usuário válido.")
                return 0 
