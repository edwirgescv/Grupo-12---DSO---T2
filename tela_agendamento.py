import FreeSimpleGUI as sg

class TelaAgendamento:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MÓDULO DE AGENDAMENTOS', font=("Helvetica", 15))],
            [sg.Button('Registrar Agendamento', key='1', size=(25, 1))],
            [sg.Button('Listar Agendamentos', key='2', size=(25, 1))],
            [sg.Button('Excluir Agendamento', key='3', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(25, 1))]
        ]
        self.__window = sg.Window('Agendamentos', element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def pegar_dados_agendamento(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Data (DD/MM/AAAA ou DDMMAAAA):'), sg.InputText(key='data')],
            [sg.Text('Hora (HH:MM):'), sg.InputText(key='hora')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Novo Agendamento').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Salvar':
            return values
        return None

    def selecionar_agendamento(self, agendamentos):
        sg.ChangeLookAndFeel('Reddit')
        lista = [f"{i} - ID: {id(a)}" for i, a in enumerate(agendamentos)]
        layout = [
            [sg.Text('Selecione o Agendamento:')],
            [sg.Listbox(values=lista, size=(40, 10), key='selecionado')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Confirmar' and values['selecionado']:
            return int(values['selecionado'][0].split(' - ')[0])
        return None

    def mostrar_mensagem(self, msg):
        sg.Popup(msg, title="Aviso")
