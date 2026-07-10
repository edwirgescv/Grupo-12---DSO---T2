from tela_profissional import TelaProfissional
from profissional_dao import ProfissionalDAO
from profissional import Profissional

class ControladorProfissional:
    def __init__(self, controlador_sistema):
        self.__tela = TelaProfissional()
        self.__controlador_sistema = controlador_sistema
        self.__dao = ProfissionalDAO()

    @property
    def profissionais(self):
        return self.__dao.get_all()

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1': self.incluir()
            elif opcao == '2': self.listar()
            elif opcao == '3': self.alterar()
            elif opcao == '4': self.excluir()
            elif opcao in ('0', None): break

    def incluir(self):
        dados = self.__tela.pegar_dados_profissional()
        if dados:
            if self.__dao.get(dados["cpf"]) is None:
                profissional = Profissional(dados["nome"], dados["telefone"], dados["cpf"], dados["especialidade"], dados["registro"])
                self.__dao.add(profissional)
                self.__tela.mostrar_mensagem("Profissional cadastrado!")
            else:
                self.__tela.mostrar_mensagem("CPF já cadastrado!")

    def listar(self):
        profissionais = self.__dao.get_all()
        msg = ""
        for p in profissionais:
            msg += f"Nome: {p.nome} | CPF: {p.cpf} | Esp: {p.especialidade} | CRM: {p.registro}\n"
        self.__tela.mostrar_mensagem(msg if msg else "Nenhum profissional cadastrado.")

    def alterar(self):
        cpf = self.__tela.selecionar_profissional()
        if cpf:
            profissional = self.__dao.get(cpf)
            if profissional:
                dados = self.__tela.pegar_dados_profissional()
                if dados:
                    profissional.nome = dados["nome"]
                    profissional.telefone = dados["telefone"]
                    profissional.especialidade = dados["especialidade"]
                    profissional.registro = dados["registro"]
                    self.__dao.add(profissional)
                    self.__tela.mostrar_mensagem("Dados alterados!")
            else:
                self.__tela.mostrar_mensagem("Profissional não encontrado.")

    def excluir(self):
        cpf = self.__tela.selecionar_profissional()
        if cpf:
            if self.__dao.get(cpf):
                self.__dao.remove(cpf)
                self.__tela.mostrar_mensagem("Profissional excluído!")
            else:
                self.__tela.mostrar_mensagem("Profissional não encontrado.")