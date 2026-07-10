from dao import DAO
from atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, atendimento: Atendimento):
        if isinstance(atendimento, Atendimento):
            chave = id(atendimento)
            super().add(chave, atendimento)

    def update(self, key: int, atendimento: Atendimento):
        if isinstance(key, int) and isinstance(atendimento, Atendimento):
            super().add(key, atendimento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
