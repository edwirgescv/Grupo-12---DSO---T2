import FreeSimpleGUI as sg


class TelaAtendimento:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MODULO ATENDIMENTOS', font=("Helvetica", 15))],
            [sg.Button('Registrar Atendimento', key='1', size=(25, 1))],
            [sg.Button('Listar Atendimentos', key='2', size=(25, 1))],
            [sg.Button('Excluir Atendimento', key='3', size=(25, 1))],
            [sg.Button('Alterar Atendimento', key='4', size=(25, 1))],
            [sg.Button('Adicionar Procedimento', key='5', size=(25, 1))],
            [sg.Button('Listar Procedimentos', key='6', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(25, 1))]
        ]
        self.__window = sg.Window('Atendimentos', element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def selecionar_atendimento(self, atendimentos, acao='excluir'):
        sg.ChangeLookAndFeel('Reddit')
        lista = [f"{i} - {a.data.strftime('%d/%m/%Y')} | {a.paciente.nome}" for i, a in enumerate(atendimentos)]
        layout = [
            [sg.Text(f'Selecione o atendimento para {acao}:')],
            [sg.Combo(values=lista, size=(50, 1), key='selecionado')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Atendimento').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Confirmar' and values.get('selecionado'):
            try:
                return int(str(values['selecionado']).split(' - ')[0])
            except Exception:
                return None
        return None

    def pegar_dados_atendimento(self, pacientes, profissionais, clinicas, tipo_padrao, atendimento=None):
        sg.ChangeLookAndFeel('Reddit')
        paciente_valores = [f"{i} - {p.nome} ({p.cpf})" for i, p in enumerate(pacientes)]
        profissional_valores = [f"{i} - {p.nome} ({p.cpf})" for i, p in enumerate(profissionais)]
        clinica_valores = [f"{i} - {c.nome} ({c.endereco})" for i, c in enumerate(clinicas)]
        horarios = [f'{h:02d}:00' for h in range(8, 19)]

        paciente_padrao = ''
        profissional_padrao = ''
        clinica_padrao = ''
        data_padrao = ''
        hora_inicio_padrao = '08:00'
        hora_fim_padrao = '09:00'
        tipo_padrao_texto = str(tipo_padrao)
        valor_padrao = ''
        titulo = 'Novo Atendimento'

        if atendimento:
            titulo = 'Alterar Atendimento'
            for i, paciente in enumerate(pacientes):
                if paciente.cpf == atendimento.paciente.cpf:
                    paciente_padrao = paciente_valores[i]
                    break
            for i, profissional in enumerate(profissionais):
                if profissional.cpf == atendimento.profissional.cpf:
                    profissional_padrao = profissional_valores[i]
                    break
            for i, clinica in enumerate(clinicas):
                if clinica.nome == atendimento.clinica.nome:
                    clinica_padrao = clinica_valores[i]
                    break
            data_padrao = atendimento.data.strftime('%d/%m/%Y')
            hora_inicio_padrao = atendimento.hora_inicio.strftime('%H:%M')
            hora_fim_padrao = atendimento.hora_fim.strftime('%H:%M')
            tipo_padrao_texto = str(atendimento.tipo_atendimento)
            valor_padrao = str(atendimento.valor).replace('.', ',')

        layout = [
            [sg.Text('Paciente:'), sg.Combo(values=paciente_valores, size=(40, 1), key='paciente', default_value=paciente_padrao)],
            [sg.Text('Profissional:'), sg.Combo(values=profissional_valores, size=(40, 1), key='profissional', default_value=profissional_padrao)],
            [sg.Text('Clinica:'), sg.Combo(values=clinica_valores, size=(40, 1), key='clinica', default_value=clinica_padrao)],
            [sg.Text('Data (DD/MM/AAAA ou DDMMAAAA):'), sg.InputText(default_text=data_padrao, key='data', size=(20, 1))],
            [sg.Text('Horario de Inicio:'), sg.Combo(values=horarios, size=(20, 1), key='hora_inicio', default_value=hora_inicio_padrao)],
            [sg.Text('Horario de Fim:'), sg.Combo(values=horarios, size=(20, 1), key='hora_fim', default_value=hora_fim_padrao)],
            [sg.Text('Tipo de Atendimento:'), sg.InputText(default_text=tipo_padrao_texto, key='tipo', size=(40, 1))],
            [sg.Text('Valor (R$):'), sg.InputText(default_text=valor_padrao, key='valor', size=(20, 1))],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window(titulo, element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Salvar':
            return values
        return None

    def pegar_dados_procedimento(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Descricao:'), sg.InputText(key='descricao', size=(40, 1))],
            [sg.Text('Custo (R$):'), sg.InputText(key='custo', size=(20, 1))],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Adicionar Procedimento').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Salvar':
            return values
        return None

    def mostrar_mensagem(self, msg):
        sg.Popup(msg, title="Aviso")
