from pagamento import Pagamento


class PagamentoPix(Pagamento):
    def __init__(self, data, atendimento,
                 paciente, valor_pago,
                 cpf_pagador):

        super().__init__(
            data,
            atendimento,
            paciente,
            valor_pago
        )

        self.__cpf_pagador = cpf_pagador

    def detalhes_pagamento(self):
        return (
            f"Pagamento PIX | "
            f"CPF Pagador: {self.__cpf_pagador}"
        )