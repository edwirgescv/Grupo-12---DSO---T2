from dao import DAO
from paciente import Paciente

class PacienteDAO(DAO):
    def __init__(self):
        super().__init__('pacientes.pkl')

    def add(self, paciente: Paciente):
        if isinstance(paciente, Paciente) and isinstance(paciente.cpf, str):
            super().add(paciente.cpf, paciente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)