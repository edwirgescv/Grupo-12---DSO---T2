from tela_agendamento import TelaAgendamento
from agendamento_dao import AgendamentoDAO
from agendamento import Agendamento
from date_utils import normalizar_data

class ControladorAgendamento:
    def __init__(self, controlador_sistema):
        self.__tela = TelaAgendamento()
        self.__controlador_sistema = controlador_sistema
        self.__dao = AgendamentoDAO()

    @property
    def agendamentos(self):
        return self.__dao.get_all()

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1': self.incluir()
            elif opcao == '2': self.listar()
            elif opcao == '3': self.excluir()
            elif opcao in ('0', None): break

    def incluir(self):
        dados = self.__tela.pegar_dados_agendamento()
        if dados:
            dados["data"] = normalizar_data(dados["data"])
            agendamento = Agendamento(dados["data"], dados["hora"])
            self.__dao.add(agendamento)
            self.__tela.mostrar_mensagem("Agendamento registrado!")

    def listar(self):
        lista = self.__dao.get_all()
        msg = ""
        for a in lista:
            msg += f"Reserva - Data: {a.data} | Hora: {a.hora}\n"
        self.__tela.mostrar_mensagem(msg if msg else "Nenhum agendamento encontrado.")

    def excluir(self):
        lista = self.__dao.get_all()
        if not lista:
            self.__tela.mostrar_mensagem("Nenhum agendamento para excluir.")
            return
        idx = self.__tela.selecionar_agendamento(lista)
        if idx is not None:
            chave = id(lista[idx])
            self.__dao.remove(chave)
            self.__tela.mostrar_mensagem("Agendamento excluído!")
