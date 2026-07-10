import FreeSimpleGUI as sg


class TelaRelatorio:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MODULO DE RELATORIOS', font=("Helvetica", 15))],
            [sg.Button('Relatorio de Pacientes', key='1', size=(30, 1))],
            [sg.Button('Relatorio de Atendimentos', key='2', size=(30, 1))],
            [sg.Button('Clinica Mais Popular', key='3', size=(30, 1))],
            [sg.Button('Atendimentos Mais Caro/Barato', key='4', size=(30, 1))],
            [sg.Button('Procedimento Mais Realizado', key='5', size=(30, 1))],
            [sg.Button('Voltar', key='0', size=(30, 1))]
        ]
        self.__window = sg.Window('Relatorios', element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def mostrar_relatorio(self, titulo, conteudo):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(titulo, font=("Helvetica", 14))],
            [sg.Multiline(conteudo, size=(70, 18), disabled=True)],
            [sg.Button('Fechar')]
        ]
        self.__window = sg.Window('Relatorio').Layout(layout)
        self.__window.Read()
        self.__window.Close()
