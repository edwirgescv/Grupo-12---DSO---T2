from abc import ABC, abstractmethod
from datetime import datetime
from exceptions import PagamentoAtrasadoException


class Pagamento(ABC):
    def __init__(self, data, atendimento,
                 paciente, valor_pago):

        if isinstance(data, datetime):
            data = data.date()

        data_atendimento = atendimento.data
        if isinstance(data_atendimento, datetime):
            data_atendimento = data_atendimento.date()

        if data > data_atendimento:
            raise PagamentoAtrasadoException(
                "Pagamento realizado após a data do atendimento."
            )

        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago

    @property
    def valor_pago(self):
        return self.__valor_pago

    @property
    def data(self):
        return self.__data

    @property
    def paciente(self):
        return self.__paciente

    @abstractmethod
    def detalhes_pagamento(self):
        pass