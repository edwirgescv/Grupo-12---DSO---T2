import FreeSimpleGUI as sg

class TelaClinica:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MÓDULO CLÍNICA', font=("Helvetica", 15))],
            [sg.Button('Cadastrar Clínica', key='1', size=(20,1))],
            [sg.Button('Listar Clínicas', key='2', size=(20,1))],
            [sg.Button('Alterar Clínica', key='3', size=(20,1))],
            [sg.Button('Excluir Clínica', key='4', size=(20,1))],
            [sg.Button('Voltar', key='0', size=(20,1))]
        ]
        self.__window = sg.Window('Clínica', element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def pegar_dados_clinica(self):
        sg.ChangeLookAndFeel('Reddit')
        horarios = [f'{h:02d}:00' for h in range(24)]
        layout = [
            [sg.Text('Nome da Clínica:'), sg.InputText(key='nome')],
            [sg.Text('Cidade/Endereço:'), sg.InputText(key='endereco')],
            [sg.Text('Descrição:'), sg.InputText(key='descricao')],
            [sg.Text('Horário de abertura:'), sg.Combo(horarios, default_value='08:00', key='abertura', size=(10, 1))],
            [sg.Text('Horário de fechamento:'), sg.Combo(horarios, default_value='18:00', key='fechamento', size=(10, 1))],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Dados da Clínica').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Salvar':
            return values
        return None

    def selecionar_clinica(self, clinicas):
        sg.ChangeLookAndFeel('Reddit')
        nomes = [c.nome for c in clinicas]
        layout = [
            [sg.Text('Selecione a clínica:')],
            [sg.Combo(values=nomes, size=(40, 1), key='clinica')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Clínica').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Confirmar':
            valor = values.get('clinica')
            if isinstance(valor, list):
                valor = valor[0] if valor else None
            return str(valor).strip() if valor is not None else None
        return None

    def mostrar_mensagem(self, msg):
        sg.Popup(msg, title="Aviso")