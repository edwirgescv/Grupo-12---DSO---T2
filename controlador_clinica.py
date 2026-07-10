from tela_clinica import TelaClinica
from clinica_dao import ClinicaDAO
from clinica import Clinica
from datetime import time

class ControladorClinica:
    def __init__(self, controlador_sistema):
        self.__tela = TelaClinica()
        self.__controlador_sistema = controlador_sistema
        self.__dao = ClinicaDAO()

    @property
    def clinicas(self):
        return self.__dao.get_all()

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1': self.incluir()
            elif opcao == '2': self.listar()
            elif opcao == '3': self.alterar()
            elif opcao == '4': self.excluir()
            elif opcao in ('0', None): break

    def incluir(self):
        dados = self.__tela.pegar_dados_clinica()
        if dados:
            if self.__dao.get(dados["nome"]) is None:
                abertura = dados.get('abertura', '08:00')
                fechamento = dados.get('fechamento', '18:00')
                hora_abertura = int(abertura.split(':')[0])
                minuto_abertura = int(abertura.split(':')[1])
                hora_fechamento = int(fechamento.split(':')[0])
                minuto_fechamento = int(fechamento.split(':')[1])

                clinica = Clinica(
                    dados["nome"],
                    dados["endereco"],
                    dados.get("descricao", ""),
                    time(hora_abertura, minuto_abertura),
                    time(hora_fechamento, minuto_fechamento)
                )
                self.__dao.add(clinica)
                self.__tela.mostrar_mensagem("Clínica cadastrada!")
            else:
                self.__tela.mostrar_mensagem("Clínica já existe!")

    def listar(self):
        clinicas = self.__dao.get_all()
        msg = ""
        for c in clinicas:
            msg += f"Clínica: {c.nome} | Endereço: {c.endereco} | Horário: {c.horario_abertura.strftime('%H:%M')} - {c.horario_fechamento.strftime('%H:%M')}\n"
        self.__tela.mostrar_mensagem(msg if msg else "Nenhuma clínica cadastrada.")

    def alterar(self):
        clinicas = self.__dao.get_all()
        if not clinicas:
            self.__tela.mostrar_mensagem("Nenhuma clínica cadastrada.")
            return

        nome_clinica = self.__tela.selecionar_clinica(clinicas)
        if not nome_clinica:
            return

        clinica = self.__dao.get(nome_clinica)
        if not clinica:
            self.__tela.mostrar_mensagem("Clínica não encontrada.")
            return

        dados = self.__tela.pegar_dados_clinica()
        if dados:
            abertura = dados.get('abertura', '08:00')
            fechamento = dados.get('fechamento', '18:00')
            hora_abertura = int(abertura.split(':')[0])
            minuto_abertura = int(abertura.split(':')[1])
            hora_fechamento = int(fechamento.split(':')[0])
            minuto_fechamento = int(fechamento.split(':')[1])

            novo_nome = dados.get('nome', clinica.nome)
            clinica.nome = novo_nome
            clinica.endereco = dados.get('endereco', clinica.endereco)
            clinica.descricao = dados.get('descricao', clinica.descricao)
            clinica.horario_abertura = time(hora_abertura, minuto_abertura)
            clinica.horario_fechamento = time(hora_fechamento, minuto_fechamento)

            if novo_nome != nome_clinica:
                self.__dao.remove(nome_clinica)
            self.__dao.add(clinica)
            self.__tela.mostrar_mensagem("Clínica alterada com sucesso!")

    def excluir(self):
        clinicas = self.__dao.get_all()
        if not clinicas:
            self.__tela.mostrar_mensagem("Nenhuma clínica cadastrada.")
            return

        nome_clinica = self.__tela.selecionar_clinica(clinicas)
        if not nome_clinica:
            return

        if self.__dao.get(nome_clinica):
            self.__dao.remove(nome_clinica)
            self.__tela.mostrar_mensagem("Clínica excluída com sucesso!")
        else:
            self.__tela.mostrar_mensagem("Clínica não encontrada.")