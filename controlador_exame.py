from tela_exame import TelaExame
from exame_dao import ExameDAO
from exame import Exame

class ControladorExame:
    def __init__(self, controlador_sistema):
        self.__tela = TelaExame()
        self.__controlador_sistema = controlador_sistema
        self.__dao = ExameDAO()

    @property
    def exames(self):
        return self.__dao.get_all()

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1': self.incluir()
            elif opcao == '2': self.listar()
            elif opcao == '3': self.excluir()
            elif opcao in ('0', None): break

    def incluir(self):
        dados = self.__tela.pegar_dados_exame()
        if dados:
            if self.__dao.get(dados["nome"]) is None:
                exame = Exame(dados["nome"], dados["preparo"])
                self.__dao.add(exame)
                self.__tela.mostrar_mensagem("Exame cadastrado com sucesso!")
            else:
                self.__tela.mostrar_mensagem("Exame já existe no sistema.")

    def listar(self):
        lista = self.__dao.get_all()
        msg = ""
        for e in lista:
            msg += f"Exame: {e.nome} | Preparo: {e.preparo}\n"
        self.__tela.mostrar_mensagem(msg if msg else "Nenhum exame cadastrado.")

    def excluir(self):
        nome = self.__tela.selecionar_exame()
        if nome:
            if self.__dao.get(nome):
                self.__dao.remove(nome)
                self.__tela.mostrar_mensagem("Exame excluído!")
            else:
                self.__tela.mostrar_mensagem("Exame não encontrado.")