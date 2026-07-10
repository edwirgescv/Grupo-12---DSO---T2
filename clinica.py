from datetime import time


class Clinica:
    def __init__(self, nome, endereco, descricao, horario_abertura, horario_fechamento):
        self.__nome = nome
        self.__endereco = endereco
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self.__descricao = nova_descricao

    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, novo_horario):
        self.__horario_abertura = novo_horario

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, novo_horario):
        self.__horario_fechamento = novo_horario

    def exibir_dados(self):
        return f"Clínica: {self.__nome} | Endereço: {self.__endereco}"