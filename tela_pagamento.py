import FreeSimpleGUI as sg

class TelaPagamento:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('💰 MÓDULO FINANCEIRO', font=("Helvetica", 15))],
            [sg.Button('Registrar Pagamento', key='1', size=(25, 1))],
            [sg.Button('Listar Pagamentos', key='2', size=(25, 1))],
            [sg.Button('Excluir Pagamento', key='4', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(25, 1))]
        ]
        self.__window = sg.Window('Módulo Financeiro', element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def selecionar_atendimento(self, atendimentos):
        sg.ChangeLookAndFeel('Reddit')
        lista = [f"{i} - {a.data.strftime('%d/%m/%Y')} | {a.paciente.nome}" for i, a in enumerate(atendimentos)]
        layout = [
            [sg.Text('Selecione o atendimento para pagamento:')],
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

    def pegar_dados_pagamento(self, paciente_nome=None):
        sg.ChangeLookAndFeel('Reddit')
        titulo = 'Dados do Pagamento'
        if paciente_nome:
            titulo = f'Pagamento para {paciente_nome}'
        layout = [
            [sg.Text(titulo, font=("Helvetica", 12))],
            [sg.Text('Valor (R$):'), sg.InputText(key='valor')],
            [sg.Radio('PIX', "RADIO1", key='1', default=True), 
             sg.Radio('Cartão', "RADIO1", key='2'), 
             sg.Radio('Dinheiro', "RADIO1", key='3')],
            [sg.Text('CPF (Para PIX):'), sg.InputText(key='cpf')],
            [sg.Text('Cartão (Para Cartão):'), sg.InputText(key='cartao')],
            [sg.Text('Bandeira (Para Cartão):'), sg.InputText(key='bandeira')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window(titulo).Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()

        if button == 'Confirmar':
            try:
                valor = float(values['valor'])
                tipo = '1' if values['1'] else '2' if values['2'] else '3'
                dados = {"valor": valor, "tipo": tipo}
                if tipo == '1':
                    dados["cpf_pagador"] = values['cpf']
                elif tipo == '2':
                    dados["numero_cartao"] = values['cartao']
                    dados["bandeira"] = values['bandeira']
                return dados
            except ValueError:
                self.mostrar_mensagem("Erro: Valor inválido.")
                return None
        return None

    def mostrar_mensagem(self, msg):
        sg.Popup(msg, title="Aviso Financeiro")