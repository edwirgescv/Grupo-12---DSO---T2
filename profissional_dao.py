from dao import DAO
from profissional import Profissional

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__('profissionais.pkl')

    def add(self, profissional: Profissional):
        if isinstance(profissional, Profissional) and isinstance(profissional.cpf, str):
            super().add(profissional.cpf, profissional)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)