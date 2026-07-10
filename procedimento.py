class Procedimento:
    def __init__(self, descricao, custo,
                 profissional_responsavel):

        self.__descricao = descricao
        self.__custo = custo
        self.__profissional_responsavel = profissional_responsavel

    @property
    def descricao(self):
        return self.__descricao

    @property
    def custo(self):
        return self.__custo

    @property
    def profissional_responsavel(self):
        return self.__profissional_responsavel

    def exibir_dados(self):
        return (
            f"Procedimento: {self.descricao} | "
            f"Custo: R$ {self.custo:.2f}"
        )