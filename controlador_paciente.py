from tela_paciente import TelaPaciente
from paciente_dao import PacienteDAO
from paciente import Paciente
from date_utils import parse_data

class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__tela = TelaPaciente()
        self.__controlador_sistema = controlador_sistema
        self.__dao = PacienteDAO()

    @property
    def pacientes(self):
        return self.__dao.get_all()

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1': self.incluir()
            elif opcao == '2': self.listar()
            elif opcao == '3': self.alterar()
            elif opcao in ('0', None): break

    def incluir(self):
        dados = self.__tela.pegar_dados_paciente()
        if dados:
            if self.__dao.get(dados["cpf"]) is None:
                # parsear data de nascimento no formato DD/MM/AAAA
                try:
                    data_nasc_str = dados.get("data_nascimento", "")
                    data_nasc = parse_data(data_nasc_str) if data_nasc_str else None
                except Exception:
                    self.__tela.mostrar_mensagem("Formato de data invalido. Use DD/MM/AAAA ou DDMMAAAA.")
                    return

                paciente = Paciente(dados["nome"], dados.get("celular", ""), dados["cpf"], data_nasc)
                self.__dao.add(paciente)
                self.__tela.mostrar_mensagem("Salvo!")
            else:
                self.__tela.mostrar_mensagem("CPF já existe!")

    def listar(self):
        pacientes = self.__dao.get_all()
        msg = ""
        for p in pacientes:
            msg += f"Nome: {p.nome} | CPF: {p.cpf}\n"
        self.__tela.mostrar_mensagem(msg if msg else "Nenhum paciente.")

    def alterar(self):
        cpf = self.__tela.selecionar_paciente()
        if cpf:
            paciente = self.__dao.get(cpf)
            if paciente:
                dados = self.__tela.pegar_dados_paciente(paciente)
                if dados:
                    novo_cpf = dados.get("cpf", cpf)
                    if novo_cpf != cpf and self.__dao.get(novo_cpf) is not None:
                        self.__tela.mostrar_mensagem("CPF já cadastrado para outro paciente.")
                        return

                    paciente.nome = dados.get("nome", paciente.nome)
                    paciente.celular = dados.get("celular", paciente.celular)
                    # parsear data de nascimento
                    data_nasc_str = dados.get("data_nascimento", "")
                    if data_nasc_str:
                        try:
                            paciente.data_nascimento = parse_data(data_nasc_str)
                        except Exception:
                            self.__tela.mostrar_mensagem("Formato de data invalido. Use DD/MM/AAAA ou DDMMAAAA.")
                            return

                    if novo_cpf != cpf:
                        self.__dao.remove(cpf)
                        paciente = Paciente(paciente.nome, paciente.celular, novo_cpf, paciente.data_nascimento)
                    self.__dao.add(paciente)
                    self.__tela.mostrar_mensagem("Dados alterados!")
            else:
                self.__tela.mostrar_mensagem("Paciente não encontrado.")
