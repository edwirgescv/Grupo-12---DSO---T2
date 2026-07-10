import FreeSimpleGUI as sg

class TelaExame:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MÓDULO DE EXAMES', font=("Helvetica", 15))],
            [sg.Button('Cadastrar Exame', key='1', size=(25, 1))],
            [sg.Button('Listar Exames', key='2', size=(25, 1))],
            [sg.Button('Excluir Exame', key='3', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(25, 1))]
        ]
        self.__window = sg.Window('Exames', element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def pegar_dados_exame(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Nome do Exame:'), sg.InputText(key='nome')],
            [sg.Text('Preparo/Recomendação:'), sg.InputText(key='preparo')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Novo Exame').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Salvar':
            return values
        return None

    def selecionar_exame(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Digite o nome do Exame:')],
            [sg.InputText(key='nome')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Confirmar':
            return values['nome']
        return None

    def mostrar_mensagem(self, msg):
        sg.Popup(msg, title="Aviso")