from datetime import date
from tela_pagamento import TelaPagamento
from pagamento_pix import PagamentoPix
from pagamento_cartao import PagamentoCartao
from pagamento_dinheiro import PagamentoDinheiro
from exceptions import PagamentoAtrasadoException

class ControladorPagamento:
    def __init__(self, controlador_sistema):
        self.__tela = TelaPagamento()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1':
                self.incluir_pagamento()
            elif opcao == '2':
                self.listar_pagamentos()
            elif opcao == '4':
                self.excluir_pagamento()
            elif opcao in ('0', None):
                break

    def incluir_pagamento(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not atendimentos:
            self.__tela.mostrar_mensagem("É necessário ter um atendimento registrado primeiro.")
            return

        idx = self.__tela.selecionar_atendimento(atendimentos)
        if idx is None or idx < 0 or idx >= len(atendimentos):
            self.__tela.mostrar_mensagem("Seleção de atendimento inválida.")
            return

        atendimento_vinculado = atendimentos[idx]
        hoje = date.today()
        if hoje > atendimento_vinculado.data:
            self.__tela.mostrar_mensagem("O pagamento deve ser realizado ate o dia marcado para o atendimento.")
            return

        paciente_vinculado = atendimento_vinculado.paciente
        dados = self.__tela.pegar_dados_pagamento(paciente_vinculado.nome)
        if dados:
            try:
                hoje = date.today()
                if hoje > atendimento_vinculado.data:
                    self.__tela.mostrar_mensagem("O pagamento deve ser realizado até a data do atendimento.")
                    return

                if dados["tipo"] == '1':
                    novo = PagamentoPix(hoje, atendimento_vinculado, paciente_vinculado, dados["valor"], dados["cpf_pagador"])
                elif dados["tipo"] == '2':
                    novo = PagamentoCartao(hoje, atendimento_vinculado, paciente_vinculado, dados["valor"], dados["numero_cartao"], dados["bandeira"])
                else:
                    novo = PagamentoDinheiro(hoje, atendimento_vinculado, paciente_vinculado, dados["valor"])

                atendimento_vinculado.adicionar_pagamento(novo)
                self.__controlador_sistema.controlador_atendimento.salvar_dados()
                self.__tela.mostrar_mensagem("Pagamento registrado e salvo no sistema!")
            except PagamentoAtrasadoException as e:
                self.__tela.mostrar_mensagem(str(e))

    def listar_pagamentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        msg = ""
        for a in atendimentos:
            if hasattr(a, 'pagamentos') and a.pagamentos:
                msg += f"Atendimento de {a.paciente.nome}:\n"
                for p in a.pagamentos:
                    msg += f"- R$ {p.valor_pago:.2f} ({type(p).__name__})\n"
        
        self.__tela.mostrar_mensagem(msg if msg else "Nenhum pagamento registrado.")

    def excluir_pagamento(self):
        self.__tela.mostrar_mensagem("Para excluir um pagamento, exclua o Atendimento vinculado.")













        
