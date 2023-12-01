from DAOs.dao import DAO
from entidade.jogo import Jogo
 

class JogoDAO(DAO):
    def __init__(self):
        super().__init__("jogos.pkl")

    def add(self, jogo: Jogo):
        if((jogo is not None) and isinstance(jogo, Jogo) and isinstance(jogo.num_jogo, int)):
            super().add(jogo.num_jogo, jogo)

    def update(self, jogo: Jogo):
        if((jogo is not None) and isinstance(jogo, Jogo) and isinstance(jogo.num_jogo, int)):
            super().update(jogo.num_jogo, jogo)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)