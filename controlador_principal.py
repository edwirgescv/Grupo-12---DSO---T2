from tela_principal import TelaPrincipal
from controlador_paciente import ControladorPaciente
from controlador_atendimento import ControladorAtendimento
from controlador_pagamento import ControladorPagamento
from controlador_profissional import ControladorProfissional
from controlador_relatorio import ControladorRelatorio
from controlador_agendamento import ControladorAgendamento
from controlador_exame import ControladorExame
from controlador_clinica import ControladorClinica

from clinica import Clinica
from profissional import Profissional
from tipo_atendimento import TipoAtendimento
from datetime import time

class ControladorPrincipal:
    __instance = None

    def __new__(cls):
        if ControladorPrincipal.__instance is None:
            ControladorPrincipal.__instance = object.__new__(cls)
        return ControladorPrincipal.__instance

    def __init__(self):
        if not hasattr(self, '__initialized'):
            self.__tela = TelaPrincipal()
            self.__controlador_paciente = ControladorPaciente(self)
            self.__controlador_atendimento = ControladorAtendimento(self)
            self.__controlador_pagamento = ControladorPagamento(self)
            self.__controlador_profissional = ControladorProfissional(self)
            self.__controlador_relatorio = ControladorRelatorio(self)
            self.__controlador_agendamento = ControladorAgendamento(self)
            self.__controlador_exame = ControladorExame(self)
            self.__controlador_clinica = ControladorClinica(self)

            self.clinica_padrao = Clinica("Vida Saudável", "Florianópolis", "Matriz", time(8, 0), time(18, 0))
            self.profissional_padrao = Profissional("Dr. Carlos", "48999999999", "12345678900", "Geral", "CRM123")
            self.tipo_padrao = TipoAtendimento("Consulta Padrão")

            self.__initialized = True

    @property
    def controlador_paciente(self): return self.__controlador_paciente
    @property
    def controlador_atendimento(self): return self.__controlador_atendimento
    @property
    def controlador_profissional(self): return self.__controlador_profissional
    @property
    def controlador_relatorio(self): return self.__controlador_relatorio
    @property
    def controlador_agendamento(self): return self.__controlador_agendamento
    @property
    def controlador_exame(self): return self.__controlador_exame
    @property
    def controlador_clinica(self): return self.__controlador_clinica
    @property
    def controlador_pagamento(self): return self.__controlador_pagamento

    def iniciar_sistema(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1': self.__controlador_paciente.abre_tela()
            elif opcao == '2': self.__controlador_atendimento.abre_tela()
            elif opcao == '3': self.__controlador_pagamento.abre_tela()
            elif opcao == '4': self.__controlador_profissional.abre_tela()
            elif opcao == '5': self.__controlador_relatorio.menu_relatorios()
            elif opcao == '6': self.__controlador_agendamento.abre_tela()
            elif opcao == '7': self.__controlador_exame.abre_tela()
            elif opcao == '8': self.__controlador_clinica.abre_tela()
            elif opcao in ('0', None):
                break