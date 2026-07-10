from dao import DAO
from exame import Exame

class ExameDAO(DAO):
    def __init__(self):
        super().__init__('exames.pkl')

    def add(self, exame: Exame):
        if isinstance(exame, Exame) and isinstance(exame.nome, str):
            super().add(exame.nome, exame)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)