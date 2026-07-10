from dao import DAO
from agendamento import Agendamento

class AgendamentoDAO(DAO):
    def __init__(self):
        super().__init__('agendamentos.pkl')

    def add(self, agendamento: Agendamento):
        if isinstance(agendamento, Agendamento):
            chave = id(agendamento)
            super().add(chave, agendamento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)