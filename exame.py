from datetime import datetime
from exceptions import HorarioInvalidoException


class Exame:
    """Classe compatível com duas formas de uso:
    - Tipo de exame cadastrado no sistema: Exame(nome, preparo)
    - Agendamento de exame: Exame(paciente, profissional, clinica, tipo_exame, data_agendamento, hora_agendamento)
    """

    def __init__(self, *args):
        if len(args) == 2:
            # formato simples: nome e preparo
            nome, preparo = args
            self.__nome = nome
            self.__preparo = preparo

            # campos de agendamento não usados
            self.__paciente = None
            self.__profissional = None
            self.__clinica = None
            self.__tipo_exame = None
            self.__data_agendamento = None
            self.__hora_agendamento = None
            self.__status = None
            self.__data_criacao = datetime.now()
            self.__data_realizacao = None
            self.__resultado = ""
            self.__observacoes = ""

        elif len(args) == 6:
            paciente, profissional, clinica, tipo_exame, data_agendamento, hora_agendamento = args

            if hora_agendamento < clinica.horario_abertura:
                raise HorarioInvalidoException("Exame antes da abertura da clínica.")

            if hora_agendamento > clinica.horario_fechamento:
                raise HorarioInvalidoException("Exame após fechamento da clínica.")

            self.__paciente = paciente
            self.__profissional = profissional
            self.__clinica = clinica
            self.__tipo_exame = tipo_exame
            self.__data_agendamento = data_agendamento
            self.__hora_agendamento = hora_agendamento
            self.__status = "Agendado"
            self.__data_criacao = datetime.now()
            self.__data_realizacao = None
            self.__resultado = ""
            self.__observacoes = ""

            # compatibilidade com cadastro de tipo de exame
            self.__nome = tipo_exame
            self.__preparo = ""

        else:
            raise TypeError("Exame: argumentos inválidos para inicialização")

    # compatibilidade com cadastro simples
    @property
    def nome(self):
        return getattr(self, '_Exame__nome', None)

    @property
    def preparo(self):
        return getattr(self, '_Exame__preparo', '')

    # propriedades para agendamento
    @property
    def paciente(self):
        return getattr(self, '_Exame__paciente', None)

    @property
    def profissional(self):
        return getattr(self, '_Exame__profissional', None)

    @property
    def clinica(self):
        return getattr(self, '_Exame__clinica', None)

    @property
    def tipo_exame(self):
        return getattr(self, '_Exame__tipo_exame', None)

    @property
    def data_agendamento(self):
        return getattr(self, '_Exame__data_agendamento', None)

    @property
    def hora_agendamento(self):
        return getattr(self, '_Exame__hora_agendamento', None)

    @property
    def status(self):
        return getattr(self, '_Exame__status', None)

    @property
    def resultado(self):
        return getattr(self, '_Exame__resultado', '')

    @resultado.setter
    def resultado(self, resultado):
        self.__resultado = resultado

    @property
    def observacoes(self):
        return getattr(self, '_Exame__observacoes', '')

    @observacoes.setter
    def observacoes(self, observacoes):
        self.__observacoes = observacoes

    def confirmar(self):
        if hasattr(self, '_Exame__status'):
            self.__status = "Confirmado"

    def cancelar(self):
        if hasattr(self, '_Exame__status'):
            self.__status = "Cancelado"

    def realizar_exame(self, resultado):
        if hasattr(self, '_Exame__status'):
            self.__status = "Realizado"
            self.__data_realizacao = datetime.now()
            self.__resultado = resultado

    def remarcar(self, nova_data, nova_hora):
        if not hasattr(self, '_Exame__clinica') or self.__clinica is None:
            raise HorarioInvalidoException("Exame sem clínica associada não pode ser remarcado.")

        if nova_hora < self.__clinica.horario_abertura:
            raise HorarioInvalidoException("Novo horário antes da abertura da clínica.")

        if nova_hora > self.__clinica.horario_fechamento:
            raise HorarioInvalidoException("Novo horário após fechamento da clínica.")

        self.__data_agendamento = nova_data
        self.__hora_agendamento = nova_hora
        self.__status = "Remarcado"

    def exibir_dados(self):
        if self.tipo_exame and self.paciente:
            return (
                f"Exame: {self.__tipo_exame} | "
                f"Paciente: {self.__paciente.nome} | "
                f"Data: {self.__data_agendamento.strftime('%d/%m/%Y')} às "
                f"{self.__hora_agendamento.strftime('%H:%M')} | "
                f"Status: {self.__status}"
            )
        else:
            return (
                f"Exame: {self.nome} | Preparo: {self.preparo}"
            )
