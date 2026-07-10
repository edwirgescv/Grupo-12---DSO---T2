from pagamento import Pagamento


class PagamentoCartao(Pagamento):
    def __init__(self,
                 data,
                 atendimento,
                 paciente,
                 valor_pago,
                 numero_cartao,
                 bandeira):

        super().__init__(
            data,
            atendimento,
            paciente,
            valor_pago
        )

        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    def detalhes_pagamento(self):
        return (
            f"Pagamento Cartão | "
            f"Bandeira: {self.__bandeira}"
        )