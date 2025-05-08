import sys
from io import StringIO
from antlr4 import *
from JanderParser import JanderParser
from JanderVisitor import JanderVisitor
from Simbolos import *

class VisitorInterp(JanderVisitor):
    '''
    Classe filha que herda o Visitor base
    '''
    def __init__(self, output: StringIO):
        super().__init__()
        self.out = output
    
    def visitInit(self, ctx):
        self.simbolos = Simbolos()

        return self.visitChildren(ctx)
    

    def visitDeclaracao_local(self, ctx):        
        if ctx.valor_constante() != None:
            try:    
                self.simbolos.verifySymbol(ctx.IDENT().getText())
            except IdentificadorJaUtilizadoNoEscopo:
                #inserir mensagem de erro
                pass
            
            self.simbolos.add_var(ctx.IDENT().getText(), ctx.tipo_basico().getText(), ctx.valor_constanter().getText(), True)

        elif ctx.tipo() != None:
            try: 
                self.simbolos.verifSimbolNesseEscopo(ctx.IDENT().getText())
            except IdentificadorJaUtilizadoNoEscopo:
                 #inserir mensagem de erro
                pass

        return self.visitChildren(ctx)
    
    def visitVariavel(self, ctx):
        idents =  [ctx.identificador0] + (ctx.outrosIdentificadores if ctx.outrosIdentificadores != None else [])

        for ident in idents:
            try:
                self.simbolos.verifSimbolNesseEscopo(ident.getText())
            except IdentificadorJaUtilizadoNoEscopo:
                #inserir mensagem de erro
                pass
            
            try:
                self.simbolos[ctx.tipo().getText()]
            except IdentificadorNaoDeclarado:
                #acessa a linha do token alvo
                linha = ctx.tipo().tipo_estendido().tipo_basico_ident().IDENT().symbol.line
                print(f'Linha {linha}: tipo {ctx.tipo().getText()} nao declarado', file= self.out)
                #salva a variavel com o tipo invalido
                self.simbolos.add_var(ident.getText(), 'invalido', None, False)

            self.simbolos.add_var(ident.getText(), ctx.tipo().getText(), None, False)

    
        return self.visitChildren(ctx)

    def visitCmdLeia(self, ctx):
        idents =  [ctx.identificador0] + (ctx.outrosIdentificadores if ctx.outrosIdentificadores != None else [])
        
        for ident in idents:
            try:
                self.simbolos[ident.getText()]
            except IdentificadorNaoDeclarado:
                #acessa a linha do token alvo
                linha = ident.ident0.line
                print(f'Linha {linha}: identificador {ident.getText()} nao declarado', file= self.out)

    def visitCorpo(self, ctx):
        # Adiciona o escopo da main ao codigo
        self.simbolos.add_escopo()
        children_ctx = self.visitChildren(ctx)
        self.simbolos.del_escopo()
        return children_ctx
    
    
        
