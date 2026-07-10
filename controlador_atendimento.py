from tela_atendimento import TelaAtendimento
from atendimento_dao import AtendimentoDAO
from atendimento import Atendimento
from datetime import date
from date_utils import parse_data
from tipo_atendimento import TipoAtendimento
from procedimento import Procedimento

class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__tela = TelaAtendimento()
        self.__controlador_sistema = controlador_sistema
        self.__dao = AtendimentoDAO()

    @property
    def atendimentos(self):
        return self.__dao.get_all()

    def salvar_dados(self):
        for atendimento in self.atendimentos:
            self.__dao.add(atendimento)

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1': self.incluir()
            elif opcao == '2': self.listar()
            elif opcao == '3': self.excluir()
            elif opcao == '4': self.alterar()
            elif opcao == '5': self.adicionar_procedimento()
            elif opcao == '6': self.listar_procedimentos()
            elif opcao in ('0', None): break

    def __parse_index(self, value):
        if isinstance(value, list):
            value = value[0] if value else ""
        if value is None:
            return None
        text = str(value).strip()
        if not text:
            return None
        if text.isdigit():
            return int(text)
        try:
            return int(text.split(' - ')[0])
        except Exception:
            return None

    def __obter_opcoes_cadastro(self):
        pacientes = self.__controlador_sistema.controlador_paciente.pacientes
        profissionais = self.__controlador_sistema.controlador_profissional.profissionais
        clinicas = list(self.__controlador_sistema.controlador_clinica.clinicas)
        if all(c.nome != self.__controlador_sistema.clinica_padrao.nome for c in clinicas):
            clinicas.insert(0, self.__controlador_sistema.clinica_padrao)
        return pacientes, profissionais, clinicas

    def __converter_dados_atendimento(self, dados, pacientes, profissionais, clinicas):
        if not dados['paciente'] or not dados['profissional']:
            self.__tela.mostrar_mensagem("Selecione paciente e profissional.")
            return None

        idx_paciente = self.__parse_index(dados['paciente'])
        idx_profissional = self.__parse_index(dados['profissional'])
        idx_clinica = self.__parse_index(dados['clinica'])

        if (
            idx_paciente is None or idx_paciente < 0 or idx_paciente >= len(pacientes) or
            idx_profissional is None or idx_profissional < 0 or idx_profissional >= len(profissionais) or
            idx_clinica is None or idx_clinica < 0 or idx_clinica >= len(clinicas)
        ):
            self.__tela.mostrar_mensagem("Selecao invalida. Escolha paciente, profissional e clinica da lista.")
            return None

        try:
            from datetime import datetime
            data = parse_data(dados['data'])

            hora_inicio_texto = str(dados.get('hora_inicio', '')[0] if isinstance(dados.get('hora_inicio'), list) and dados.get('hora_inicio') else dados.get('hora_inicio', '')).strip()
            hora_fim_texto = str(dados.get('hora_fim', '')[0] if isinstance(dados.get('hora_fim'), list) and dados.get('hora_fim') else dados.get('hora_fim', '')).strip()
            valor_texto = str(dados.get('valor', '')[0] if isinstance(dados.get('valor'), list) and dados.get('valor') else dados.get('valor', '')).strip()

            hora_inicio = None
            hora_fim = None
            for fmt in ['%H:%M', '%H:%M:%S', '%H.%M', '%Hh%M']:
                try:
                    hora_inicio = datetime.strptime(hora_inicio_texto, fmt).time()
                    break
                except ValueError:
                    continue
            for fmt in ['%H:%M', '%H:%M:%S', '%H.%M', '%Hh%M']:
                try:
                    hora_fim = datetime.strptime(hora_fim_texto, fmt).time()
                    break
                except ValueError:
                    continue

            valor = float(valor_texto.replace(',', '.')) if valor_texto else 0.0
        except Exception:
            self.__tela.mostrar_mensagem("Erro nos dados informados. Verifique data, horario e valor.")
            return None

        if data < date.today():
            self.__tela.mostrar_mensagem("Data invalida: a data deve ser hoje ou futura.")
            return None
        if hora_inicio is None or hora_fim is None:
            self.__tela.mostrar_mensagem("Preencha os horarios de inicio e fim do atendimento.")
            return None
        if hora_fim <= hora_inicio:
            self.__tela.mostrar_mensagem("O horario final deve ser posterior ao horario inicial.")
            return None

        tipo_texto = str(dados.get('tipo', '')).strip()
        tipo = TipoAtendimento(tipo_texto) if tipo_texto else self.__controlador_sistema.tipo_padrao

        return {
            "paciente": pacientes[idx_paciente],
            "profissional": profissionais[idx_profissional],
            "clinica": clinicas[idx_clinica],
            "data": data,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "tipo": tipo,
            "valor": valor
        }

    def incluir(self):
        pacientes = self.__controlador_sistema.controlador_paciente.pacientes
        profissionais = self.__controlador_sistema.controlador_profissional.profissionais
        clinicas = list(self.__controlador_sistema.controlador_clinica.clinicas)
        if all(c.nome != self.__controlador_sistema.clinica_padrao.nome for c in clinicas):
            clinicas.insert(0, self.__controlador_sistema.clinica_padrao)
        
        if not pacientes or not profissionais or not clinicas:
            self.__tela.mostrar_mensagem("É necessário ter pacientes, profissionais e clínicas cadastrados.")
            return

        dados = self.__tela.pegar_dados_atendimento(pacientes, profissionais, clinicas, self.__controlador_sistema.tipo_padrao)
        if not dados:
            return

        if not dados['paciente'] or not dados['profissional']:
            self.__tela.mostrar_mensagem("Selecione paciente e profissional.")
            return

        def parse_index(value):
            if isinstance(value, list):
                value = value[0] if value else ""
            if value is None:
                return None
            text = str(value).strip()
            if not text:
                return None
            if text.isdigit():
                return int(text)
            try:
                return int(text.split(' - ')[0])
            except Exception:
                return None

        idx_paciente = parse_index(dados['paciente'])
        idx_profissional = parse_index(dados['profissional'])
        if idx_paciente is None or idx_profissional is None:
            self.__tela.mostrar_mensagem("Seleção inválida. Escolha paciente, profissional e clínica da lista.")
            return

        idx_clinica = parse_index(dados['clinica'])
        if idx_clinica is None or idx_clinica < 0 or idx_clinica >= len(clinicas):
            self.__tela.mostrar_mensagem("Seleção inválida. Escolha paciente, profissional e clínica da lista.")
            return

        paciente = pacientes[idx_paciente]
        profissional = profissionais[idx_profissional]
        clinica = clinicas[idx_clinica]
        tipo = self.__controlador_sistema.tipo_padrao

        try:
            data = parse_data(dados['data'])
        except Exception:
            self.__tela.mostrar_mensagem("Formato de data invalido. Use DD/MM/AAAA ou DDMMAAAA.")
            return

        if data < date.today():
            self.__tela.mostrar_mensagem("Data inválida: a data deve ser hoje ou futura.")
            return

        try:
            from datetime import datetime
            hora_inicio = None
            hora_fim = None
            valor = 0.0

            hora_inicio_texto = ''
            hora_fim_texto = ''
            valor_texto = ''

            if isinstance(dados.get('hora_inicio'), list):
                hora_inicio_texto = str(dados['hora_inicio'][0] if dados['hora_inicio'] else '').strip()
            else:
                hora_inicio_texto = str(dados.get('hora_inicio', '')).strip()

            if isinstance(dados.get('hora_fim'), list):
                hora_fim_texto = str(dados['hora_fim'][0] if dados['hora_fim'] else '').strip()
            else:
                hora_fim_texto = str(dados.get('hora_fim', '')).strip()

            if isinstance(dados.get('valor'), list):
                valor_texto = str(dados['valor'][0] if dados['valor'] else '').strip()
            else:
                valor_texto = str(dados.get('valor', '')).strip()

            if hora_inicio_texto:
                for fmt in ['%H:%M', '%H:%M:%S', '%H.%M', '%Hh%M']:
                    try:
                        hora_inicio = datetime.strptime(hora_inicio_texto, fmt).time()
                        break
                    except ValueError:
                        continue
            if hora_fim_texto:
                for fmt in ['%H:%M', '%H:%M:%S', '%H.%M', '%Hh%M']:
                    try:
                        hora_fim = datetime.strptime(hora_fim_texto, fmt).time()
                        break
                    except ValueError:
                        continue
            if valor_texto:
                valor = float(valor_texto.replace(',', '.'))

            if hora_inicio is None or hora_fim is None:
                self.__tela.mostrar_mensagem("Preencha os horários de início e fim do atendimento.")
                return

            if hora_fim <= hora_inicio:
                self.__tela.mostrar_mensagem("O horário final deve ser posterior ao horário inicial.")
                return

            atendimento = Atendimento(clinica, paciente, profissional, data, hora_inicio, hora_fim, tipo, valor)
            self.__dao.add(atendimento)
            self.__tela.mostrar_mensagem("Atendimento registrado com sucesso!")
        except ValueError:
            self.__tela.mostrar_mensagem("Erro nos dados informados. Verifique horário e valor.")
        except TypeError as e:
            self.__tela.mostrar_mensagem(f"Erro ao registrar atendimento: {e}")
        except Exception as e:
            from exceptions import MenorDeIdadeException, HorarioInvalidoException
            if isinstance(e, MenorDeIdadeException):
                self.__tela.mostrar_mensagem("Não é possível marcar atendimento: paciente menor de idade.")
            elif isinstance(e, HorarioInvalidoException):
                self.__tela.mostrar_mensagem(str(e))
            else:
                self.__tela.mostrar_mensagem("Erro inesperado ao registrar atendimento.")

    def listar(self):
        atendimentos = self.__dao.get_all()
        msg = ""
        for a in atendimentos:
            msg += f"Data: {a.data.strftime('%d/%m/%Y')} | Paciente: {a.paciente.nome} | Saldo: R${a.calcular_valor_restante():.2f}\n"
        self.__tela.mostrar_mensagem(msg if msg else "Nenhum atendimento registrado.")

    def alterar(self):
        itens = self.__dao.get_all_items()
        if not itens:
            self.__tela.mostrar_mensagem("Nenhum atendimento para alterar.")
            return

        atendimentos = [a for _, a in itens]
        idx = self.__tela.selecionar_atendimento(atendimentos, 'alterar')
        if idx is None:
            self.__tela.mostrar_mensagem("Nenhuma selecao feita para alteracao.")
            return
        if idx < 0 or idx >= len(atendimentos):
            self.__tela.mostrar_mensagem("Selecao invalida.")
            return

        atendimento = atendimentos[idx]
        pacientes, profissionais, clinicas = self.__obter_opcoes_cadastro()
        if not pacientes or not profissionais or not clinicas:
            self.__tela.mostrar_mensagem("E necessario ter pacientes, profissionais e clinicas cadastrados.")
            return

        dados = self.__tela.pegar_dados_atendimento(
            pacientes,
            profissionais,
            clinicas,
            self.__controlador_sistema.tipo_padrao,
            atendimento
        )
        if not dados:
            return

        novos_dados = self.__converter_dados_atendimento(dados, pacientes, profissionais, clinicas)
        if not novos_dados:
            return

        try:
            from exceptions import MenorDeIdadeException, HorarioInvalidoException

            atendimento_teste = Atendimento(
                novos_dados["clinica"],
                novos_dados["paciente"],
                novos_dados["profissional"],
                novos_dados["data"],
                novos_dados["hora_inicio"],
                novos_dados["hora_fim"],
                novos_dados["tipo"],
                novos_dados["valor"]
            )

            atendimento.clinica = atendimento_teste.clinica
            atendimento.paciente = atendimento_teste.paciente
            atendimento.profissional = atendimento_teste.profissional
            atendimento.data = atendimento_teste.data
            atendimento.hora_inicio = atendimento_teste.hora_inicio
            atendimento.hora_fim = atendimento_teste.hora_fim
            atendimento.tipo_atendimento = atendimento_teste.tipo_atendimento
            atendimento.valor = atendimento_teste.valor

            chave = itens[idx][0]
            self.__dao.update(chave, atendimento)
            self.__tela.mostrar_mensagem("Atendimento alterado com sucesso!")
        except Exception as e:
            if isinstance(e, MenorDeIdadeException):
                self.__tela.mostrar_mensagem("Nao e possivel marcar atendimento: paciente menor de idade.")
            elif isinstance(e, HorarioInvalidoException):
                self.__tela.mostrar_mensagem(str(e))
            else:
                self.__tela.mostrar_mensagem("Erro inesperado ao alterar atendimento.")

    def adicionar_procedimento(self):
        itens = self.__dao.get_all_items()
        if not itens:
            self.__tela.mostrar_mensagem("Nenhum atendimento para adicionar procedimento.")
            return

        atendimentos = [a for _, a in itens]
        idx = self.__tela.selecionar_atendimento(atendimentos, 'adicionar procedimento')
        if idx is None:
            self.__tela.mostrar_mensagem("Nenhuma selecao feita.")
            return
        if idx < 0 or idx >= len(atendimentos):
            self.__tela.mostrar_mensagem("Selecao invalida.")
            return

        dados = self.__tela.pegar_dados_procedimento()
        if not dados:
            return

        descricao = str(dados.get('descricao', '')).strip()
        custo_texto = str(dados.get('custo', '')).strip()
        if not descricao:
            self.__tela.mostrar_mensagem("Informe a descricao do procedimento.")
            return

        try:
            custo = float(custo_texto.replace(',', '.')) if custo_texto else 0.0
        except ValueError:
            self.__tela.mostrar_mensagem("Custo invalido.")
            return

        atendimento = atendimentos[idx]
        procedimento = Procedimento(descricao, custo, atendimento.profissional)
        atendimento.adicionar_procedimento(procedimento)
        chave = itens[idx][0]
        self.__dao.update(chave, atendimento)
        self.__tela.mostrar_mensagem("Procedimento adicionado ao atendimento!")

    def listar_procedimentos(self):
        atendimentos = self.__dao.get_all()
        msg = ""
        procedimentos = []

        for atendimento in atendimentos:
            if not atendimento.procedimentos:
                continue

            msg += (
                f"Atendimento: {atendimento.data.strftime('%d/%m/%Y')} | "
                f"Paciente: {atendimento.paciente.nome}\n"
            )
            for procedimento in atendimento.procedimentos:
                procedimentos.append(procedimento)
                msg += (
                    f"- {procedimento.descricao} | "
                    f"Custo: R$ {procedimento.custo:.2f} | "
                    f"Profissional: {procedimento.profissional_responsavel.nome}\n"
                )
            msg += "\n"

        if procedimentos:
            mais_barato = min(procedimentos, key=lambda procedimento: procedimento.custo)
            mais_caro = max(procedimentos, key=lambda procedimento: procedimento.custo)
            msg += "Resumo de procedimentos\n" + "-" * 30 + "\n"
            msg += f"Procedimento mais barato: {mais_barato.descricao} | R$ {mais_barato.custo:.2f}\n"
            msg += f"Procedimento mais caro: {mais_caro.descricao} | R$ {mais_caro.custo:.2f}\n"

        self.__tela.mostrar_mensagem(msg if msg else "Nenhum procedimento cadastrado.")

    def excluir(self):
        itens = self.__dao.get_all_items()
        if not itens:
            self.__tela.mostrar_mensagem("Nenhum atendimento para excluir.")
            return
        atendimentos = [a for _, a in itens]
        idx = self.__tela.selecionar_atendimento(atendimentos)
        if idx is None:
            self.__tela.mostrar_mensagem("Nenhuma seleção feita para exclusão.")
            return
        if idx < 0 or idx >= len(atendimentos):
            self.__tela.mostrar_mensagem("Seleção inválida.")
            return
        chave = itens[idx][0]
        self.__dao.remove(chave)
        self.__tela.mostrar_mensagem("Atendimento excluído com sucesso.")
