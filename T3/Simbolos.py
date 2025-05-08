class IdentificadorNaoDeclarado(Exception):
    pass

class IdentificadorJaUtilizadoNoEscopo(Exception):
    pass

class TipoNaoDeclarado(Exception):
    pass

class Simbolos:
    '''
    Classe que armazena e faz verificações dos siumbolos nos diferentes escopos
    '''
    def __init__(self):
        self.__escopos = []
        self.__add_escopo()
        self.__tipos = ['literal', 'inteiro', 'real', 'logico']
    
    def add_escopo(self):
        self.__escopos.append(dict())

    def del_escopo(self):
        self.__escopos.pop()

    def __getitem__(self, key):
        for scp in reversed(self.__escopos):
            try:
                return scp[key]
            except KeyError:
                pass
        
        raise IdentificadorNaoDeclarado
    
    def add_var(self, identificador: str, tipo: str, valor, is_constante: bool):
        self.__escopos[-1] |= {identificador: {'tipo': tipo, 
                                                'is_constante': is_constante,
                                                'valor': valor}}
        
    def add_tipo(self, nome_tipo: str, tipo: str):
        self.__tipos.append(tipo)
        self.__escopos[-1] |= {nome_tipo: {'tipo': tipo}}

    def verifSimbolo(self, simbolo: str):
        try:
            self.__escopos[-1][simbolo]
        except KeyError:
            pass
        else:
            raise IdentificadorJaUtilizadoNoEscopo
        
    def verifTipo(self, tipo: str):
        if tipo not in self.__tipos:
            raise TipoNaoDeclarado


    __add_escopo = add_escopo
