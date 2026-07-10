import FreeSimpleGUI as sg

class TelaProfissional:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MÓDULO PROFISSIONAIS', font=("Helvetica", 15))],
            [sg.Button('Incluir', key='1', size=(20,1))],
            [sg.Button('Listar', key='2', size=(20,1))],
            [sg.Button('Alterar', key='3', size=(20,1))],
            [sg.Button('Excluir', key='4', size=(20,1))],
            [sg.Button('Voltar', key='0', size=(20,1))]
        ]
        self.__window = sg.Window('Profissionais', element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def pegar_dados_profissional(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('Telefone:'), sg.InputText(key='telefone')],
            [sg.Text('CPF:'), sg.InputText(key='cpf')],
            [sg.Text('Especialidade:'), sg.InputText(key='especialidade')],
            [sg.Text('Registro (CRM):'), sg.InputText(key='registro')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Profissional').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Salvar':
            return values
        return None

    def selecionar_profissional(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Digite o CPF do Profissional:')],
            [sg.InputText(key='cpf')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Profissional').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Confirmar':
            return values['cpf']
        return None

    def mostrar_mensagem(self, msg):
        sg.Popup(msg, title="Aviso")