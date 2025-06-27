class TipoNaoDeclarado(Exception):
    pass

class IdentificadorNaoDeclarado(Exception):
    pass

class IdentificadorJaUtilizadoNoEscopo(Exception):
    pass

class AtribuicaoNaoCompativel(Exception):
    pass

class IncompatibilidadeDeParametros(Exception):
    pass

class ComandoRetorneNaoPermitido(Exception):
    pass

class RetornoInside(Exception):
    def __init__(self, ctx, *args):
        super().__init__(*args)
        self.ctx = ctx

class Simbolos:
    '''
    Classe que armazena e faz verificações dos siumbolos nos diferentes escopos
    '''
    def __init__(self):
        self.__escopos = []
        self.__escopos_global_reservado = dict()
        self.__tipos = []
        self.__add_escopo()
        self.__add_tipo('literal', 'literal')
        self.__add_tipo('inteiro', 'inteiro')
        self.__add_tipo('real', 'real')
        self.__add_tipo('logico', 'logico')
        self.__add_tipo('registro', 'registro')
    
    def add_escopo(self):
        self.__escopos.append(dict())

    def del_escopo(self):
        self.__escopos.pop()

    def __getitem__(self, key):
        key = key.lstrip('^')
        try:
            return self.__escopos_global_reservado[key]
        except KeyError:
            for scp in reversed(self.__escopos):
                try:
                    return scp[key]
                except KeyError:
                    pass
        
        raise IdentificadorNaoDeclarado
    
    def add_var(self, 
                identificador: str, 
                tipo: str, 
                valor, is_constante: bool) -> None:
        
        var = {identificador: {'tipo': tipo, 
                                'is_constante': is_constante,
                                'valor': valor}}
        if is_constante:
            self.__escopos_global_reservado |= var
        else:
            self.__escopos[-1] |= var
    
    def add_func(self,
                 identificador: str,
                 tipo: str,
                 params: dict[str, str]) -> None:
        
        self.__escopos_global_reservado |= {identificador: {'tipo': tipo, 
                                               'params': params}}
        
        

    def add_tipo(self, nome_tipo: str, tipo: str):
        self.__tipos.append(tipo)
        self.__escopos[-1] |= {nome_tipo: {'tipo': tipo}}

    def verifSimbolNesseEscopo(self, simbolo: str):
        try:
            self.__escopos_global_reservado[simbolo]
        except KeyError:
            try:
                self.__escopos[-1][simbolo]
            except KeyError:
                pass
            else:
                raise IdentificadorJaUtilizadoNoEscopo
        else:
            raise IdentificadorJaUtilizadoNoEscopo

    '''
    def verifSimbolNesseEscopo(self, simbolo: str):
        try:
            self.__escopos[-1][simbolo]
        except KeyError:
            pass
        else:
            raise IdentificadorJaUtilizadoNoEscopo
    '''
    def verifType(self, simbolo: str):
        if(simbolo in self.__tipos):
            pass
        else:
            raise TipoNaoDeclarado


    __add_escopo = add_escopo
    __add_tipo = add_tipo