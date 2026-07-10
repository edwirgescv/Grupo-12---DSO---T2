import FreeSimpleGUI as sg

class TelaPaciente:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MÓDULO PACIENTES', font=("Helvetica", 15))],
            [sg.Button('Incluir', key='1')],
            [sg.Button('Listar', key='2')],
            [sg.Button('Alterar', key='3')],
            [sg.Button('Voltar', key='0')]
        ]
        self.__window = sg.Window('Pacientes').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def pegar_dados_paciente(self, paciente=None):
        sg.ChangeLookAndFeel('Reddit')
        nome = paciente.nome if paciente else ''
        cpf = paciente.cpf if paciente else ''
        celular = paciente.celular if paciente else ''
        data_nascimento = paciente.data_nascimento.strftime('%d/%m/%Y') if paciente and paciente.data_nascimento else ''
        layout = [
            [sg.Text('Nome:'), sg.InputText(default_text=nome, key='nome')],
            [sg.Text('CPF:'), sg.InputText(default_text=cpf, key='cpf')],
            [sg.Text('Celular:'), sg.InputText(default_text=celular, key='celular')],
            [sg.Text('Data de nascimento (DD/MM/AAAA ou DDMMAAAA):'), sg.InputText(default_text=data_nascimento, key='data_nascimento')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Dados').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()

        if button == 'Salvar':
            return {"nome": values['nome'], "cpf": values['cpf'], "celular": values.get('celular', ''), "data_nascimento": values.get('data_nascimento', '')}
        return None

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)

    def selecionar_paciente(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Digite o CPF do Paciente:')],
            [sg.InputText(key='cpf')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Paciente').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Confirmar':
            return values['cpf']
        return None
