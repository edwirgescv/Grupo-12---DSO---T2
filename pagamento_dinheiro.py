from pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def __init__(self,
                 data,
                 atendimento,
                 paciente,
                 valor_pago):

        super().__init__(
            data,
            atendimento,
            paciente,
            valor_pago
        )

    def detalhes_pagamento(self):
        return "Pagamento em dinheiro"