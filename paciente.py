from datetime import date
from pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(self, nome, celular, cpf, data_nascimento):
        super().__init__(nome, celular, cpf)
        self.__data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self.__data_nascimento = value

    def calcular_idade(self):
        hoje = date.today()
        idade = hoje.year - self.__data_nascimento.year

        if (hoje.month, hoje.day) < (
            self.__data_nascimento.month,
            self.__data_nascimento.day
        ):
            idade -= 1

        return idade

    def maior_de_idade(self):
        return self.calcular_idade() >= 18

    def exibir_dados(self):
        return f"Paciente: {self.nome} | CPF: {self.cpf}"