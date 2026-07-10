from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, celular: str, cpf: str):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

    def __setstate__(self, state):
        if isinstance(state, dict):
            if 'nome' in state and '_Pessoa__nome' not in state:
                state['_Pessoa__nome'] = state['nome']
            if 'celular' in state and '_Pessoa__celular' not in state:
                state['_Pessoa__celular'] = state['celular']
            if 'cpf' in state and '_Pessoa__cpf' not in state:
                state['_Pessoa__cpf'] = state['cpf']
        self.__dict__.update(state)

    def _get_private(self, field_name, public_name):
        if field_name in self.__dict__:
            return self.__dict__[field_name]
        if public_name in self.__dict__:
            return self.__dict__[public_name]
        raise AttributeError(public_name)

    @property
    def nome(self):
        return self._get_private('_Pessoa__nome', 'nome')

    @nome.setter
    def nome(self, value: str):
        self.__nome = value
        if 'nome' in self.__dict__:
            self.__dict__['nome'] = value

    @property
    def celular(self):
        return self._get_private('_Pessoa__celular', 'celular')

    @celular.setter
    def celular(self, value: str):
        self.__celular = value
        if 'celular' in self.__dict__:
            self.__dict__['celular'] = value

    # backward-compatible alias `telefone`
    @property
    def telefone(self):
        return self.celular

    @telefone.setter
    def telefone(self, value: str):
        self.__celular = value

    @property
    def cpf(self):
        return self.__cpf

    @abstractmethod
    def exibir_dados(self):
        pass