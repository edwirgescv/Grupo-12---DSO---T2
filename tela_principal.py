import FreeSimpleGUI as sg

class TelaPrincipal:
    def __init__(self):
        self.__window = None

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('🏥 SISTEMA DE GESTÃO DE CLÍNICA', font=("Helvetica", 20), justification='center')],
            [sg.Button('Módulo de Pacientes', key='1', size=(30, 1))],
            [sg.Button('Módulo de Atendimentos', key='2', size=(30, 1))],
            [sg.Button('Módulo Financeiro (Pagamentos)', key='3', size=(30, 1))],
            [sg.Button('Módulo de Profissionais', key='4', size=(30, 1))],
            [sg.Button('Relatórios', key='5', size=(30, 1))],
            [sg.Button('Módulo de Agendamentos', key='6', size=(30, 1))],
            [sg.Button('Módulo de Exames', key='7', size=(30, 1))],
            [sg.Button('Gestão de Clínicas', key='8', size=(30, 1))],
            [sg.Button('Sair do Sistema', key='0', size=(30, 1))]
        ]
        self.__window = sg.Window('Menu Principal', element_justification='c').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def mostrar_mensagem(self, msg):
        sg.Popup(msg, title="Aviso")