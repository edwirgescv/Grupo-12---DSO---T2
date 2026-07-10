from dao import DAO
from clinica import Clinica

class ClinicaDAO(DAO):
    def __init__(self):
        super().__init__('clinicas.pkl')

    def add(self, clinica: Clinica):
        if isinstance(clinica, Clinica) and isinstance(clinica.nome, str):
            super().add(clinica.nome, clinica)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)