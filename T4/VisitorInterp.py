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
        self.retorno = False

    def visitInit(self, ctx):
        self.simbolos = Simbolos()
        return self.visitChildren(ctx)
    
    '''
    Mensagens de erro
    '''
    def error(self, line, msg, erro):
        match erro:
            # TipoNaoDeclarado
            case 1: print(f"Linha {line}: tipo {msg} nao declarado", file=self.out, flush= True)
            # IdentificadorNaoDeclarado
            case 2: print(f"Linha {line}: identificador {msg} nao declarado", file=self.out, flush= True)
            # IdentificadorJaUtilizadoNoEscopo
            case 3: print(f"Linha {line}: identificador {msg} ja declarado anteriormente", file=self.out, flush= True)
            # AtribuicaoNaoCompativel
            case 4: print(f"Linha {line}: atribuicao nao compativel para {msg}", file=self.out, flush= True)
            # IncompatibilidadeDeParametros
            case 5: print(f"Linha {line}: incompatibilidade de parametros na chamada de {msg}", file=self.out, flush= True)
            # ComandoRetorneNaoPermitido
            case 6: print(f"Linha {line}: comando retorne nao permitido nesse escopo", file=self.out, flush= True)
            # Retorne incompativel
            case 7: print(f"Linha {line}: comando retorne nao permitido nesse escopo", file=self.out, flush= True)
            # Tipos de paarametro incompativeis
            case 8: print(f"Linha {line}: incompatibilidade de parametros na chamada de {msg}", file=self.out, flush= True)

    '''
    Visitors
    '''
    def visitDeclaracao_local(self, ctx):        
        
        if ctx.IDENT():
            ident = ctx.IDENT().getText()
            if ctx.tipo():
                tipo = ctx.tipo().getText().lstrip('^')
                tipo = self.visitTipo(ctx.tipo())
            elif ctx.tipo_basico():
                tipo = ctx.tipo_basico().getText()
                try:
                    self.simbolos.verifType(tipo)
                except TipoNaoDeclarado:
                    self.error(ctx.start.line, tipo, 1)
                    tipo = 'indefinido'

            else:
                tipo = None

            try:
                self.simbolos.verifSimbolNesseEscopo(ident)
            except IdentificadorJaUtilizadoNoEscopo:
                self.error(ctx.start.line, ident, 3)

            
            

            if ctx.tipo(): 
                if (ctx.tipo().getText().startswith("^")): tipo = "^" + tipo
                self.simbolos.add_tipo(ident, tipo)
            else:
                self.simbolos.add_var(ident, tipo, None, is_constante=(ctx.tipo_basico() is not None))
        else:
            pass

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
            param_name_tipo = param.tipo_estendido().getText()
            param_tipo = self.simbolos[param_name_tipo]['tipo']

            for param_ident in param_idents:
                params_dict |= {param_ident.getText(): param_tipo}
                
        self.simbolos.add_func(ident, tipo, params_dict)
        self.simbolos.add_escopo()

        for param_name, param_tipo in params_dict.items():
            if isinstance(param_tipo, dict):
                for campo, tipo_campo in param_tipo.items():
                    nome_completo = f"{param_ident.getText()}.{campo}"
                    try:
                        self.simbolos.add_var(nome_completo, tipo_campo, None, False)
                    except IdentificadorJaUtilizadoNoEscopo:
                        self.error(self, ident.start.line, nome_completo, 3)
            else:
                self.simbolos.add_var(param_name, param_tipo, None, False)



        children_ctx = self.visitChildren(ctx)
        
        if self.retorno:
            if tipo is None:
                self.error(self.retorno, msg='', erro= 7)
            self.retorno = False
              
        self.simbolos.del_escopo()

        return children_ctx
    
    def visitVariavel(self, ctx):
        idents = ctx.identificador()
        tipo = self.visitTipo(ctx.tipo())

        
        for ident in idents:
            print(ident.getText() + " var ")
            if ident.dimensao().exp_aritmetica():
                ident = ident.IDENT()[0]

            # se for registro de registro
            try:
                self.simbolos.verifSimbolNesseEscopo(ident.getText())
            except IdentificadorJaUtilizadoNoEscopo:
                self.error(ident.start.line, ident.getText(), 3)
            else:
            
                if isinstance(tipo, dict):
                    for campo, tipo_campo in tipo.items():
                        nome_completo = f"{ident.getText()}.{campo}"
                        try:
                            self.simbolos.verifType(tipo_campo)
                        except TipoNaoDeclarado:
                            self.error(ctx.start.line, tipo, 1)
                            tipo_campo = 'invalido'
                        
                        try:
                            self.simbolos.add_var(nome_completo, tipo_campo, None, False)
                        except IdentificadorJaUtilizadoNoEscopo:
                            self.error(self, ident.start.line, nome_completo, 3)
                else:
                    try:
                        self.simbolos.verifType(tipo)
                    except TipoNaoDeclarado:
                        self.error(ctx.start.line, tipo, 1)
                        tipo = 'invalido'
                    
                
                

                if (ctx.tipo().getText().startswith("^")): tipo = "^" + tipo

                self.simbolos.add_var(ident.getText(), tipo, None, False)

        return self.visitChildren(ctx)
    

        
    
    #
    def visitCmdAtribuicao(self, ctx):
        ident = ctx.identificador()
        
        if ident.dimensao().exp_aritmetica():
            ident = ident.IDENT()[0].getText().lstrip('^')
        else:
            ident = ident.getText().lstrip('^')
        

        try:
            simbolo = self.simbolos[ident]
        except IdentificadorNaoDeclarado:
            self.error(ctx.start.line, ident, 2)
        else:
        
            if not isinstance(simbolo['tipo'], dict):
                if (simbolo['tipo'].startswith("^")):
                    if(ctx.PONTEIRO()):
                        try:
                            expressaoTipo = self._avaliar_expressao(ctx.expressao())
                            self._tipos_compativeis(simbolo['tipo'].lstrip('^'), expressaoTipo)
                        except AtribuicaoNaoCompativel:
                            self.error(ctx.start.line, '^' + ctx.identificador().getText(), 4)

                    else:
                        if not ctx.expressao().getText().startswith('&'):
                            self.error(ctx.start.line, ident.getText(), 4)
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
            if ident.dimensao().exp_aritmetica():
                ident = ident.IDENT()[0]
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
                expr = exprs[idx]
                self._tipos_compativeis(self._avaliar_expressao(expr), param, int2real= False)
            except (AtribuicaoNaoCompativel, IndexError):
                self.error(ctx.start.line, ident, 8)
        
        return self.visitChildren(ctx)
    
    def visitCmdRetorne(self, ctx):
        self.retorno = ctx.start.line 
    
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

        return tipos[0] if len(tipos) == 1 else 'logico' 

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
                return self._avaliar_expressao(p.expressao())
            if p.identificador():
                ident = p.identificador()
                if ident.dimensao().exp_aritmetica():
                    ident = ident.IDENT()[0]
                name = ident.getText() 
                return self._tipo_identificador(name, ctx)

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
            name = ctx.getText()
            return self.simbolos[name]['tipo']

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

        children_ctx = self.visitChildren(ctx)
        if self.retorno:
            self.error(self.retorno, msg= '', erro= 7)
            self.retorno = False

        self.simbolos.del_escopo()
        return children_ctx
    
'''
O que faltaria para ficar completo:

- Não consegue lidar com atribuições com variaveis 
- Faltam alguns Cmd: caso, chamada, faca, retorne, se, ect. Mas tem o sufuciente para o T3

'''