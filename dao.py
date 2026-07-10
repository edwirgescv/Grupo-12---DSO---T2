import os
import pickle
import importlib
from abc import ABC

class DAO(ABC):
    def __init__(self, datasource=''):
        self._datasource = datasource
        self._cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
        except (pickle.UnpicklingError, AttributeError, ModuleNotFoundError, ImportError, EOFError):
            backup_path = f"{self._datasource}.corrupt"
            try:
                os.replace(self._datasource, backup_path)
            except OSError:
                pass
            self._cache = {}
            self.__dump()

    def __dump(self):
        pickle.dump(self._cache, open(self._datasource, 'wb'))

    def __load(self):
        class _SafeUnpickler(pickle.Unpickler):
            def find_class(self, module, name):
                if module == '__main__':
                    aliases = {
                        'Clinica': 'clinica',
                        'Paciente': 'paciente',
                        'Profissional': 'profissional',
                        'Atendimento': 'atendimento',
                        'Agendamento': 'agendamento',
                        'Exame': 'exame',
                        'TipoAtendimento': 'tipo_atendimento',
                        'Pagamento': 'pagamento',
                        'PagamentoCartao': 'pagamento_cartao',
                        'PagamentoDinheiro': 'pagamento_dinheiro',
                        'PagamentoPix': 'pagamento_pix',
                        'Procedimento': 'procedimento',
                        'Pessoa': 'pessoa'
                    }
                    module = aliases.get(name, module)
                return super().find_class(module, name)

        with open(self._datasource, 'rb') as handle:
            self._cache = _SafeUnpickler(handle).load()

    def add(self, key, obj):
        self._cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self._cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self._cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return list(self._cache.values())

    def get_all_items(self):
        return list(self._cache.items())