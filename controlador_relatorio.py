from tela_relatorio import TelaRelatorio


class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__tela = TelaRelatorio()
        self.__controlador_sistema = controlador_sistema

    def menu_relatorios(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1':
                self.relatorio_pacientes()
            elif opcao == '2':
                self.relatorio_atendimentos()
            elif opcao == '3':
                self.relatorio_clinica_popular()
            elif opcao == '4':
                self.relatorio_atendimentos_extremos()
            elif opcao == '5':
                self.relatorio_procedimentos_populares()
            elif opcao in ('0', None):
                break

    def _valor_para_considerar(self, atendimento):
        return atendimento.valor

    def _obter_atendimentos_extremos(self, atendimentos):
        if not atendimentos:
            return None, None
        mais_caro = max(atendimentos, key=lambda atendimento: self._valor_para_considerar(atendimento))
        mais_barato = min(atendimentos, key=lambda atendimento: self._valor_para_considerar(atendimento))
        return mais_caro, mais_barato

    def _adicionar_resumo_atendimentos(self, msg, atendimentos):
        mais_caro, mais_barato = self._obter_atendimentos_extremos(atendimentos)
        msg += "Resumo de atendimentos\n" + "-" * 30 + "\n"
        if mais_caro is None:
            msg += "Atendimento mais caro: Nenhum atendimento cadastrado\n"
            msg += "Atendimento mais barato: Nenhum atendimento cadastrado\n"
        else:
            valor_caro = self._valor_para_considerar(mais_caro)
            valor_barato = self._valor_para_considerar(mais_barato)
            msg += (
                f"Atendimento mais caro: {mais_caro.paciente.nome} | "
                f"{mais_caro.data.strftime('%d/%m/%Y')} | R$ {valor_caro:.2f}\n"
            )
            msg += (
                f"Atendimento mais barato: {mais_barato.paciente.nome} | "
                f"{mais_barato.data.strftime('%d/%m/%Y')} | R$ {valor_barato:.2f}\n"
            )
        return msg + "\n"

    def relatorio_pacientes(self):
        pacientes = self.__controlador_sistema.controlador_paciente.pacientes

        msg = "LISTAGEM GERAL DE PACIENTES\n" + "-" * 30 + "\n"
        for p in pacientes:
            msg += f"Nome: {p.nome} - CPF: {p.cpf}\n"
        self.__tela.mostrar_relatorio("Relatorio de Pacientes", msg)

    def relatorio_atendimentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos

        msg = "LISTAGEM GERAL DE ATENDIMENTOS\n" + "-" * 30 + "\n"
        for a in atendimentos:
            msg += (
                f"Data: {a.data.strftime('%d/%m/%Y')} - "
                f"Paciente: {a.paciente.nome} - "
                f"Clinica: {a.clinica.nome} - "
                f"Valor: R$ {a.valor:.2f}\n"
            )
        msg += "\n"
        msg = self._adicionar_resumo_atendimentos(msg, atendimentos)
        self.__tela.mostrar_relatorio("Relatorio de Atendimentos", msg)

    def relatorio_atendimentos_extremos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        msg = "ATENDIMENTOS MAIS CARO E MAIS BARATO\n" + "-" * 30 + "\n"
        msg = self._adicionar_resumo_atendimentos(msg, atendimentos)
        self.__tela.mostrar_relatorio("Atendimentos Extremos", msg)

    def relatorio_clinica_popular(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not atendimentos:
            self.__tela.mostrar_relatorio("Clinica Mais Popular", "Nenhum atendimento registrado.")
            return

        contagem = {}
        for a in atendimentos:
            nome_clinica = a.clinica.nome
            contagem[nome_clinica] = contagem.get(nome_clinica, 0) + 1

        nome, total = max(contagem.items(), key=lambda item: item[1])
        msg = "CLINICA MAIS POPULAR\n" + "-" * 30 + "\n"
        msg += f"Clinica: {nome}\nAtendimentos marcados: {total}\n\n"
        msg += "Contagem por clinica:\n"
        for clinica, qtd in sorted(contagem.items(), key=lambda item: item[1], reverse=True):
            msg += f"- {clinica}: {qtd}\n"

        self.__tela.mostrar_relatorio("Clinica Mais Popular", msg)

    def relatorio_procedimentos_populares(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        contagem = {}
        procedimentos = []

        for atendimento in atendimentos:
            for procedimento in atendimento.procedimentos:
                procedimentos.append(procedimento)
                descricao = procedimento.descricao
                contagem[descricao] = contagem.get(descricao, 0) + 1

        if not procedimentos:
            self.__tela.mostrar_relatorio(
                "Procedimento Mais Realizado",
                "Nenhum procedimento registrado nos atendimentos."
            )
            return

        descricao, quantidade = max(contagem.items(), key=lambda item: item[1])
        mais_barato = min(procedimentos, key=lambda procedimento: procedimento.custo)
        mais_caro = max(procedimentos, key=lambda procedimento: procedimento.custo)

        msg = "RESUMO DE PROCEDIMENTOS\n" + "-" * 30 + "\n"
        msg += f"Procedimento mais realizado: {descricao} | {quantidade} vez(es)\n"
        msg += f"Procedimento mais barato: {mais_barato.descricao} | R$ {mais_barato.custo:.2f}\n"
        msg += f"Procedimento mais caro: {mais_caro.descricao} | R$ {mais_caro.custo:.2f}\n"

        self.__tela.mostrar_relatorio("Procedimento Mais Realizado", msg)
