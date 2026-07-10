from exceptions import (
    MenorDeIdadeException,
    HorarioInvalidoException
)
from datetime import datetime, timedelta


class Atendimento:
    """Aceita duas formas de inicialização:
    - Completa: (clinica, paciente, profissional, data, hora_inicio, hora_fim, tipo_atendimento, valor)
    - Simplificada: (data, paciente, profissional, tipo_atendimento, clinica)
    """

    def __init__(self, *args):
        if len(args) == 8:
            clinica, paciente, profissional, data, hora_inicio, hora_fim, tipo_atendimento, valor = args
        elif len(args) == 5:
            data, paciente, profissional, tipo_atendimento, clinica = args
            hora_inicio = clinica.horario_abertura
            try:
                hora_fim = (datetime.combine(data, hora_inicio) + timedelta(hours=1)).time()
            except Exception:
                hora_fim = hora_inicio
            valor = 0.0
        else:
            raise TypeError("Atendimento: argumentos inválidos para inicialização")

        if not paciente.maior_de_idade():
            raise MenorDeIdadeException(
                "Paciente menor de idade."
            )

        if hora_inicio < clinica.horario_abertura or hora_fim > clinica.horario_fechamento:
            raise HorarioInvalidoException(
                f"Clínica não está em funcionamento nessa hora. A clínica funciona das {clinica.horario_abertura.strftime('%H:%M')} às {clinica.horario_fechamento.strftime('%H:%M')}."
            )

        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__valor = valor

        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio):
        self.__hora_inicio = hora_inicio

    @property
    def hora_fim(self):
        return self.__hora_fim

    @hora_fim.setter
    def hora_fim(self, hora_fim):
        self.__hora_fim = hora_fim

    @property
    def pagamentos(self):
        return self.__pagamentos

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional):
        self.__profissional = profissional

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica):
        self.__clinica = clinica

    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento):
        self.__tipo_atendimento = tipo_atendimento

    @property
    def procedimentos(self):
        return self.__procedimentos

    def adicionar_procedimento(self, procedimento):
        self.__procedimentos.append(procedimento)

    def adicionar_pagamento(self, pagamento):
        self.__pagamentos.append(pagamento)

    def calcular_total_pago(self):
        total = 0

        for pagamento in self.__pagamentos:
            total += pagamento.valor_pago

        return total

    def calcular_valor_restante(self):
        return self.__valor - self.calcular_total_pago()

    def exibir_dados(self):
        return (
            f"Atendimento de {self.__paciente.nome} "
            f"com {self.__profissional.nome}"
        )
