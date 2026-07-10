from pessoa import Pessoa


class Profissional(Pessoa):
    def __init__(self, nome, celular, cpf,
                 especialidade, registro_profissional):

        super().__init__(nome, celular, cpf)

        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, value):
        self.__especialidade = value

    @property
    def registro_profissional(self):
        return self.__registro_profissional

    @property
    def registro(self):
        return self.__registro_profissional

    @registro.setter
    def registro(self, value):
        self.__registro_profissional = value

    def exibir_dados(self):
        return (
            f"Profissional: {self.nome} | "
            f"Especialidade: {self.especialidade}"
        )