# Generated from Jander.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JanderParser import JanderParser
else:
    from JanderParser import JanderParser

# This class defines a complete generic visitor for a parse tree produced by JanderParser.

class JanderVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JanderParser#init.
    def visitInit(self, ctx:JanderParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#declaracoes.
    def visitDeclaracoes(self, ctx:JanderParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#declaracao_escopo.
    def visitDeclaracao_escopo(self, ctx:JanderParser.Declaracao_escopoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#declaracao_local.
    def visitDeclaracao_local(self, ctx:JanderParser.Declaracao_localContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#variavel.
    def visitVariavel(self, ctx:JanderParser.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#identificador.
    def visitIdentificador(self, ctx:JanderParser.IdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#dimensao.
    def visitDimensao(self, ctx:JanderParser.DimensaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#tipo.
    def visitTipo(self, ctx:JanderParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#tipo_basico.
    def visitTipo_basico(self, ctx:JanderParser.Tipo_basicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#tipo_basico_ident.
    def visitTipo_basico_ident(self, ctx:JanderParser.Tipo_basico_identContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#tipo_estendido.
    def visitTipo_estendido(self, ctx:JanderParser.Tipo_estendidoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#valor_constante.
    def visitValor_constante(self, ctx:JanderParser.Valor_constanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#registro.
    def visitRegistro(self, ctx:JanderParser.RegistroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#declaracao_global.
    def visitDeclaracao_global(self, ctx:JanderParser.Declaracao_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#parametro.
    def visitParametro(self, ctx:JanderParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#parametros.
    def visitParametros(self, ctx:JanderParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#corpo.
    def visitCorpo(self, ctx:JanderParser.CorpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmd.
    def visitCmd(self, ctx:JanderParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdLeia.
    def visitCmdLeia(self, ctx:JanderParser.CmdLeiaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdEscreva.
    def visitCmdEscreva(self, ctx:JanderParser.CmdEscrevaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdSe.
    def visitCmdSe(self, ctx:JanderParser.CmdSeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdCaso.
    def visitCmdCaso(self, ctx:JanderParser.CmdCasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdPara.
    def visitCmdPara(self, ctx:JanderParser.CmdParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdEnquanto.
    def visitCmdEnquanto(self, ctx:JanderParser.CmdEnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdFaca.
    def visitCmdFaca(self, ctx:JanderParser.CmdFacaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdAtribuicao.
    def visitCmdAtribuicao(self, ctx:JanderParser.CmdAtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdChamada.
    def visitCmdChamada(self, ctx:JanderParser.CmdChamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#cmdRetorne.
    def visitCmdRetorne(self, ctx:JanderParser.CmdRetorneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#selecao.
    def visitSelecao(self, ctx:JanderParser.SelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#item_selecao.
    def visitItem_selecao(self, ctx:JanderParser.Item_selecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#constantes.
    def visitConstantes(self, ctx:JanderParser.ConstantesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#numero_intervalo.
    def visitNumero_intervalo(self, ctx:JanderParser.Numero_intervaloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#op_unario.
    def visitOp_unario(self, ctx:JanderParser.Op_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#exp_aritmetica.
    def visitExp_aritmetica(self, ctx:JanderParser.Exp_aritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#termo.
    def visitTermo(self, ctx:JanderParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#fator.
    def visitFator(self, ctx:JanderParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#op1.
    def visitOp1(self, ctx:JanderParser.Op1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#op2.
    def visitOp2(self, ctx:JanderParser.Op2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#op3.
    def visitOp3(self, ctx:JanderParser.Op3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#parcela.
    def visitParcela(self, ctx:JanderParser.ParcelaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#parcela_unario.
    def visitParcela_unario(self, ctx:JanderParser.Parcela_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#parcela_nao_unario.
    def visitParcela_nao_unario(self, ctx:JanderParser.Parcela_nao_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#exp_relacional.
    def visitExp_relacional(self, ctx:JanderParser.Exp_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#op_relacional.
    def visitOp_relacional(self, ctx:JanderParser.Op_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#expressao.
    def visitExpressao(self, ctx:JanderParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#termo_logico.
    def visitTermo_logico(self, ctx:JanderParser.Termo_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#fator_logico.
    def visitFator_logico(self, ctx:JanderParser.Fator_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#parcela_logica.
    def visitParcela_logica(self, ctx:JanderParser.Parcela_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#op_logico_1.
    def visitOp_logico_1(self, ctx:JanderParser.Op_logico_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JanderParser#op_logico_2.
    def visitOp_logico_2(self, ctx:JanderParser.Op_logico_2Context):
        return self.visitChildren(ctx)



del JanderParser