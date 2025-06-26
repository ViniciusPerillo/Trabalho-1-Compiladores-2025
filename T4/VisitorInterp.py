import sys
from io import StringIO
from antlr4 import *
from JanderVisitor import JanderVisitor
from Simbolos import *

'''
Classe filha que herda o Visitor base
'''
class VisitorInterp(JanderVisitor):
    def __init__(self, output: StringIO):
        super().__init__()
        self.out = output

    def visitInit(self, ctx):
        self.simbolos = Simbolos()
        return self.visitChildren(ctx)
    
    '''
    Mensagens de erro
    '''
    def error(self, line, msg, erro):
        match erro:
            # TipoNaoDeclarado
            case 1: print(f"Linha {line}: tipo {msg} nao declarado", file=self.out)
            # IdentificadorNaoDeclarado
            case 2: print(f"Linha {line}: identificador {msg} nao declarado", file=self.out)
            # IdentificadorJaUtilizadoNoEscopo
            case 3: print(f"Linha {line}: identificador {msg} ja declarado anteriormente", file=self.out)
            # AtribuicaoNaoCompativel
            case 4: print(f"Linha {line}: atribuicao nao compativel para {msg}", file=self.out)
            # IncompatibilidadeDeParametros
            case 5: print(f"Linha {line}: incompatibilidade de parametros na chamada de {msg}", file=self.out)
            # ComandoRetorneNaoPermitido
            case 6: print(f"Linha {line}: comando retorne nao permitido nesse escopo", file=self.out)
            # Retorne incompativel
            case 7: print(f"Linha {line}: comando retorne nao permitido nesse escopo", file=self.out)
            # Tipos de paarametro incompativeis
            case 8: print(f"Linha {line}: incompatibilidade de parametros na chamada de {msg}", file=self.out)

    '''
    Visitors
    '''
    def visitDeclaracao_local(self, ctx):        
        if ctx.IDENT():
            ident = ctx.IDENT().getText()
            tipo = ctx.tipo().getText().lstrip('^') if ctx.tipo() else None
            print(ident + " decl")

            try:
                self.simbolos.verifType(tipo)
            except TipoNaoDeclarado:
                self.error(ctx.start.line, tipo, 1)
                tipo = 'indefinido'

            try:
                self.simbolos.verifSimbolNesseEscopo(ident)
            except IdentificadorJaUtilizadoNoEscopo:
                self.error(ctx.start.line, ident, 2)

            if (ctx.tipo().getText().startswith("^")): tipo = "^" + tipo

            self.simbolos.add_var(ident, tipo, None, is_constante=False)
            print(ident)

        return self.visitChildren(ctx)
    
    def visitDeclaracao_global(self, ctx):
        ident = ctx.IDENT().getText()
        
        if ctx.tipo_estendido():
            tipo = ctx.tipo_estendido().getText()
        else: 
            tipo = None

        params = ctx.parametros().parametro()

        params_dict = {}

        for param in params:
            param_idents = param.identificador()
            param_tipo = param.tipo_estendido().getText()

            for param_ident in param_idents:
                params_dict |= {param_ident.getText(): param_tipo}
                
        self.simbolos.add_func(ident, tipo, params_dict)
        self.simbolos.add_escopo()

        for param in params:
            param_idents = param.identificador()
            param_tipo = param.tipo_estendido().getText()

            for param_ident in param_idents:
                self.simbolos.add_var(param_ident.getText(), param_tipo, None, False)

        try:
            children_ctx = self.visitChildren(ctx)
        except RetornoInside:
            if tipo is None:
                self.error(ctx, erro= 7)
        self.simbolos.del_escopo()

        return children_ctx
    
    def visitVariavel(self, ctx):
        idents = ctx.identificador()
        tipo = self.visitTipo(ctx.tipo())

        
        for ident in idents:
            print(ident.getText() + " var ")

            # se for registro de registro
            if isinstance(tipo, dict):
                for campo, tipo_campo in tipo.items():
                    nome_completo = f"{ident.getText()}.{campo}"
                    try:
                        self.simbolos.add_var(nome_completo, tipo_campo, None, False)
                    except IdentificadorJaUtilizadoNoEscopo:
                        self.error(self, ident.start.line, nome_completo, 3)

                self.simbolos.add_tipo(ident, tipo)
            # se não
            else:
                try:
                    self.simbolos.verifSimbolNesseEscopo(ident.getText())
                except IdentificadorJaUtilizadoNoEscopo:
                    self.error(ident.start.line, ident.getText(), 3)
                    pass
                
                try:
                    self.simbolos.verifType(tipo)
                except TipoNaoDeclarado:
                    line = ctx.tipo().tipo_estendido().tipo_basico_ident().IDENT().symbol.line if ctx.tipo().tipo_estendido().tipo_basico_ident().IDENT().symbol.line else ctx.tipo().tipo_estendido().IDENT().symbol.line
                    self.error(ctx.tipo().tipo_estendido().tipo_basico_ident().IDENT().symbol.line, tipo, 1)
                    tipo = 'invalido'

            if (ctx.tipo().getText().startswith("^")): tipo = "^" + tipo

            self.simbolos.add_var(ident.getText(), tipo, None, False)

        return self.visitChildren(ctx)
    
    
    #
    def visitCmdAtribuicao(self, ctx):
        ident = ctx.identificador().getText().lstrip('^')

        try:
            simbolo = self.simbolos[ident]
        except IdentificadorNaoDeclarado:
            self.error(ctx.start.line, ident, 2)
            return self.visitChildren(ctx)

        if (simbolo['tipo'].startswith("^")):
            if(ctx.PONTEIRO()):
                try:
                    expressaoTipo = self._avaliar_expressao(ctx.expressao())
                    self._tipos_compativeis(simbolo['tipo'].lstrip('^'), expressaoTipo)
                except AtribuicaoNaoCompativel:
                    self.error(ctx.start.line, '^' + ctx.identificador().getText(), 4)

            else:
                if not ctx.expressao().getText().startswith('&'):
                    self.error(ctx.start.line, ident, 4)
                else:
                    try:
                        expressao = self.simbolos[ctx.expressao().getText().lstrip('&')]
                        self._tipos_compativeis(simbolo['tipo'].lstrip('^'), expressao['tipo'])

                    except AtribuicaoNaoCompativel:
                        self.error(ctx.start.line, ctx.identificador().getText(), 4)


        else:
            try:
                expressaoTipo = self._avaliar_expressao(ctx.expressao())
                self._tipos_compativeis(simbolo['tipo'], expressaoTipo)
            except AtribuicaoNaoCompativel:
                self.error(ctx.start.line, ident, 4)


        return self.visitChildren(ctx)
    

    def visitCmdLeia(self, ctx):
        idents = ctx.identificador()
        
        for ident in idents:
            try:
                self.simbolos[ident.getText()]
            except IdentificadorNaoDeclarado:
                self.error(ident.start.line, ident.getText(), 2)
        return self.visitChildren(ctx)

    def visitCmdEnquanto(self, ctx):
        self._avaliar_expressao(ctx.expressao())
        return self.visitChildren(ctx)

    def visitCmdSe(self, ctx):
        self._avaliar_expressao(ctx.expressao())
        return self.visitChildren(ctx)

    ###
    def visitCmdEscreva(self, ctx):
        for exp in ctx.expressao():
            self._avaliar_expressao(exp)
        return self.visitChildren(ctx)

    def visitCmdChamada(self, ctx):
        ident = ctx.IDENT().getText()
        exprs = ctx.expressao()

        params = self.simbolos[ident]['params']

        for idx, param in enumerate(params.values()):
            try:
                self._tipos_compativeis(self._avaliar_expressao(exprs[idx]), param, int2real= False)
            except (AtribuicaoNaoCompativel, IndexError):
                self.error(ctx.start.line, ident, 8)
        
        return self.visitChildren(ctx)

    def _avaliar_expressao(self, ctx):  

        termos = []
        if isinstance(ctx, list):
            for c in ctx: termos.extend(c.termo_logico())
        else: termos = ctx.termo_logico()

        for termo in termos:
            tipo = self._avaliar_termo_logico(termo)
            if tipo != 'logico':
                return tipo
        return 'logico'

    def _avaliar_termo_logico(self, ctx):
        fatores = ctx.fator_logico()
        for fator in fatores:
            tipo = self._avaliar_fator_logico(fator)
            if tipo != 'logico':
                return tipo
        return 'logico'

    def _avaliar_fator_logico(self, ctx):
        sla = ctx.parcela_logica().getText()
        return self._avaliar_parcela_logica(ctx.parcela_logica())

    def _avaliar_parcela_logica(self, ctx):
        if ctx.exp_relacional():
            return self._avaliar_exp_relacional(ctx.exp_relacional())
        return 'logico'


    def _avaliar_exp_relacional(self, ctx):
        tipos = [self._avaliar_exp_aritmetica(t) for t in ctx.exp_aritmetica()]

        for idx, tipo in enumerate(tipos[1:]):
            self._tipos_compativeis(tipos[idx], tipo)

        return tipos[0]

    def _avaliar_exp_aritmetica(self, ctx):
        tipos = [self._avaliar_termo(t) for t in ctx.termo()]

        for idx, tipo in enumerate(tipos[1:]):
            if not self._tipos_compativeis(tipos[idx], tipo):
                raise AtribuicaoNaoCompativel
        
        return self._tipo_dominante(tipos)

    def _avaliar_termo(self, ctx):
        tipos = [self._avaliar_fator(f) for f in ctx.fator()]
        return self._tipo_dominante(tipos)

    def _avaliar_fator(self, ctx):
        tipos = [self._avaliar_parcela(p) for p in ctx.parcela()]
        return self._tipo_dominante(tipos)

    def _avaliar_parcela(self, ctx):
        if ctx.parcela_nao_unario():
            if ctx.parcela_nao_unario().CADEIA():
                return 'literal'

            if ctx.parcela_nao_unario().identificador():
                ident = ctx.parcela_nao_unario().identificador().getText()
                return self._tipo_identificador(ident, ctx)

        if ctx.parcela_unario():
            p = ctx.parcela_unario()
            if p.cmdChamada():  
                ident = p.cmdChamada().IDENT().getText()
                try:
                    self.simbolos[ident]
                except IdentificadorNaoDeclarado:
                    self.error(ident.start.line, ident.getText(), 2)
                return self.simbolos[ident]['tipo']
            if p.NUM_INT():
                return 'inteiro'
            if p.NUM_REAL():
                return 'real'
            if p.expressao():
                return self._avaliar_expressao(p.expressao(0))
            if p.identificador():
                ident = p.identificador().getText()
                try:
                    self.simbolos[ident]
                except IdentificadorNaoDeclarado:
                    self.error(ident.start.line, ident.getText(), 2)
                return self._tipo_identificador(ident, ctx)

        return 'indefinido'

    def _tipo_identificador(self, nome, ctx):
        try:
            simbolo = self.simbolos[nome]
            return simbolo['tipo']
        except IdentificadorNaoDeclarado:
            self.error(ctx.start.line, nome, 2)
            return 'indefinido'
        
    ## Precisa melhorar a logica
    def _tipo_dominante(self, tipos):
        tipos = [t for t in tipos if t != 'indefinido']
        if not tipos:
            return 'indefinido'
        if 'logico' in tipos:
            return 'logico'
        if 'real' in tipos:
            return 'real'
        if 'inteiro' in tipos:
            return 'inteiro'
        if 'literal' in tipos:
            return 'literal'
        return tipos[0]

    def visitTipo(self, ctx):
        if ctx.registro():
            campos = {}
            for var_ctx in ctx.registro().variavel():
                tipo_campo = self.visitTipo(var_ctx.tipo())
                for ident_ctx in var_ctx.identificador():
                    nome_campo = self._get_nome_identificador(ident_ctx)
                    campos[nome_campo] = tipo_campo
            return campos 
        else:
            return ctx.getText()

    def _tipos_compativeis(self, tipo1, tipo2, *, int2real= True):
        if 'indefinido' in (tipo1, tipo2):
            return False
        if tipo1 == tipo2:
            return True
        if {tipo1, tipo2}.issubset({'inteiro', 'real'}) and int2real:
            return True
        
        raise AtribuicaoNaoCompativel

    def _get_nome_identificador(self, ctx):
        partes = [ident.getText() for ident in ctx.IDENT()]
        return ".".join(partes)

    def visitCorpo(self, ctx):
        # Adiciona o escopo da main ao codigo
        self.simbolos.add_escopo()
        try:
            children_ctx = self.visitChildren(ctx)
        except RetornoInside:
            pass
        self.simbolos.del_escopo()
        return children_ctx
    
'''
O que faltaria para ficar completo:

- Não consegue lidar com atribuições com variaveis 
- Faltam alguns Cmd: caso, chamada, faca, retorne, se, ect. Mas tem o sufuciente para o T3

'''