class TipoAtendimento:
    def __init__(self, descricao):
        self.__descricao = descricao

    @property
    def descricao(self):
        return self.__descricao

    def __str__(self):
        return self.__descricao