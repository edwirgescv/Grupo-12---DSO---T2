from datetime import datetime
from exceptions import HorarioInvalidoException


class Agendamento:
    """Suporta duas formas de inicialização:
    - Agendamento simples (data, hora)
    - Agendamento completo (paciente, profissional, clinica, data, hora, tipo_atendimento)
    """

    def __init__(self, *args):
        if len(args) == 2:
            # forma simples: data, hora
            data_agendamento, hora_agendamento = args
            self.__data_agendamento = data_agendamento
            self.__hora_agendamento = hora_agendamento
            self.__paciente = None
            self.__profissional = None
            self.__clinica = None
            self.__tipo_atendimento = None
            self.__status = None
            self.__data_criacao = datetime.now()
            self.__observacoes = ""

        elif len(args) == 6:
            paciente, profissional, clinica, data_agendamento, hora_agendamento, tipo_atendimento = args

            if hora_agendamento < clinica.horario_abertura:
                raise HorarioInvalidoException("Agendamento antes da abertura da clínica.")

            if hora_agendamento > clinica.horario_fechamento:
                raise HorarioInvalidoException("Agendamento após fechamento da clínica.")

            self.__paciente = paciente
            self.__profissional = profissional
            self.__clinica = clinica
            self.__data_agendamento = data_agendamento
            self.__hora_agendamento = hora_agendamento
            self.__tipo_atendimento = tipo_atendimento
            self.__status = "Agendado"
            self.__data_criacao = datetime.now()
            self.__observacoes = ""

        else:
            raise TypeError("Agendamento: argumentos inválidos para inicialização")

    @property
    def paciente(self):
        return getattr(self, '_Agendamento__paciente', None)

    @property
    def profissional(self):
        return getattr(self, '_Agendamento__profissional', None)

    @property
    def clinica(self):
        return getattr(self, '_Agendamento__clinica', None)

    @property
    def data_agendamento(self):
        return getattr(self, '_Agendamento__data_agendamento', None)

    @property
    def hora_agendamento(self):
        return getattr(self, '_Agendamento__hora_agendamento', None)

    # compatibilidade com controladores que usam .data / .hora
    @property
    def data(self):
        return self.data_agendamento

    @property
    def hora(self):
        return self.hora_agendamento

    @property
    def tipo_atendimento(self):
        return getattr(self, '_Agendamento__tipo_atendimento', None)

    @property
    def status(self):
        return getattr(self, '_Agendamento__status', None)

    @property
    def observacoes(self):
        return getattr(self, '_Agendamento__observacoes', '')

    @observacoes.setter
    def observacoes(self, observacoes):
        self.__observacoes = observacoes

    def confirmar(self):
        if hasattr(self, '_Agendamento__status'):
            self.__status = "Confirmado"

    def cancelar(self):
        if hasattr(self, '_Agendamento__status'):
            self.__status = "Cancelado"

    def marcar_como_realizado(self):
        if hasattr(self, '_Agendamento__status'):
            self.__status = "Realizado"

    def remarcar(self, nova_data, nova_hora):
        if not hasattr(self, '_Agendamento__clinica') or self.__clinica is None:
            raise HorarioInvalidoException("Agendamento sem clínica associada não pode ser remarcado.")

        if nova_hora < self.__clinica.horario_abertura:
            raise HorarioInvalidoException("Novo horário antes da abertura da clínica.")

        if nova_hora > self.__clinica.horario_fechamento:
            raise HorarioInvalidoException("Novo horário após fechamento da clínica.")

        self.__data_agendamento = nova_data
        self.__hora_agendamento = nova_hora
        self.__status = "Remarcado"

    def exibir_dados(self):
        if self.paciente and self.profissional:
            return (
                f"Agendamento: {self.__paciente.nome} com "
                f"{self.__profissional.nome} | "
                f"Data: {self.__data_agendamento.strftime('%d/%m/%Y')} às "
                f"{self.__hora_agendamento.strftime('%H:%M')} | "
                f"Status: {self.__status}"
            )
        else:
            return (
                f"Agendamento - Data: {self.data_agendamento.strftime('%d/%m/%Y')} | Hora: {self.hora_agendamento.strftime('%H:%M')}"
            )
