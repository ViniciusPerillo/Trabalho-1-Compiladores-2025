# Generated from T3/Jander.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JanderParser import JanderParser
else:
    from JanderParser import JanderParser

# This class defines a complete listener for a parse tree produced by JanderParser.
class JanderListener(ParseTreeListener):

    # Enter a parse tree produced by JanderParser#init.
    def enterInit(self, ctx:JanderParser.InitContext):
        pass

    # Exit a parse tree produced by JanderParser#init.
    def exitInit(self, ctx:JanderParser.InitContext):
        pass


    # Enter a parse tree produced by JanderParser#declaracoes.
    def enterDeclaracoes(self, ctx:JanderParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by JanderParser#declaracoes.
    def exitDeclaracoes(self, ctx:JanderParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by JanderParser#declaracao_escopo.
    def enterDeclaracao_escopo(self, ctx:JanderParser.Declaracao_escopoContext):
        pass

    # Exit a parse tree produced by JanderParser#declaracao_escopo.
    def exitDeclaracao_escopo(self, ctx:JanderParser.Declaracao_escopoContext):
        pass


    # Enter a parse tree produced by JanderParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:JanderParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by JanderParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:JanderParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by JanderParser#variavel.
    def enterVariavel(self, ctx:JanderParser.VariavelContext):
        pass

    # Exit a parse tree produced by JanderParser#variavel.
    def exitVariavel(self, ctx:JanderParser.VariavelContext):
        pass


    # Enter a parse tree produced by JanderParser#identificador.
    def enterIdentificador(self, ctx:JanderParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by JanderParser#identificador.
    def exitIdentificador(self, ctx:JanderParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by JanderParser#dimensao.
    def enterDimensao(self, ctx:JanderParser.DimensaoContext):
        pass

    # Exit a parse tree produced by JanderParser#dimensao.
    def exitDimensao(self, ctx:JanderParser.DimensaoContext):
        pass


    # Enter a parse tree produced by JanderParser#tipo.
    def enterTipo(self, ctx:JanderParser.TipoContext):
        pass

    # Exit a parse tree produced by JanderParser#tipo.
    def exitTipo(self, ctx:JanderParser.TipoContext):
        pass


    # Enter a parse tree produced by JanderParser#tipo_basico.
    def enterTipo_basico(self, ctx:JanderParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by JanderParser#tipo_basico.
    def exitTipo_basico(self, ctx:JanderParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by JanderParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:JanderParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by JanderParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:JanderParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by JanderParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:JanderParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by JanderParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:JanderParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by JanderParser#valor_constante.
    def enterValor_constante(self, ctx:JanderParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by JanderParser#valor_constante.
    def exitValor_constante(self, ctx:JanderParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by JanderParser#registro.
    def enterRegistro(self, ctx:JanderParser.RegistroContext):
        pass

    # Exit a parse tree produced by JanderParser#registro.
    def exitRegistro(self, ctx:JanderParser.RegistroContext):
        pass


    # Enter a parse tree produced by JanderParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:JanderParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by JanderParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:JanderParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by JanderParser#parametro.
    def enterParametro(self, ctx:JanderParser.ParametroContext):
        pass

    # Exit a parse tree produced by JanderParser#parametro.
    def exitParametro(self, ctx:JanderParser.ParametroContext):
        pass


    # Enter a parse tree produced by JanderParser#parametros.
    def enterParametros(self, ctx:JanderParser.ParametrosContext):
        pass

    # Exit a parse tree produced by JanderParser#parametros.
    def exitParametros(self, ctx:JanderParser.ParametrosContext):
        pass


    # Enter a parse tree produced by JanderParser#corpo.
    def enterCorpo(self, ctx:JanderParser.CorpoContext):
        pass

    # Exit a parse tree produced by JanderParser#corpo.
    def exitCorpo(self, ctx:JanderParser.CorpoContext):
        pass


    # Enter a parse tree produced by JanderParser#cmd.
    def enterCmd(self, ctx:JanderParser.CmdContext):
        pass

    # Exit a parse tree produced by JanderParser#cmd.
    def exitCmd(self, ctx:JanderParser.CmdContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdLeia.
    def enterCmdLeia(self, ctx:JanderParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdLeia.
    def exitCmdLeia(self, ctx:JanderParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:JanderParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:JanderParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdSe.
    def enterCmdSe(self, ctx:JanderParser.CmdSeContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdSe.
    def exitCmdSe(self, ctx:JanderParser.CmdSeContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdCaso.
    def enterCmdCaso(self, ctx:JanderParser.CmdCasoContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdCaso.
    def exitCmdCaso(self, ctx:JanderParser.CmdCasoContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdPara.
    def enterCmdPara(self, ctx:JanderParser.CmdParaContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdPara.
    def exitCmdPara(self, ctx:JanderParser.CmdParaContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:JanderParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:JanderParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdFaca.
    def enterCmdFaca(self, ctx:JanderParser.CmdFacaContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdFaca.
    def exitCmdFaca(self, ctx:JanderParser.CmdFacaContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdAtribuicao.
    def enterCmdAtribuicao(self, ctx:JanderParser.CmdAtribuicaoContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdAtribuicao.
    def exitCmdAtribuicao(self, ctx:JanderParser.CmdAtribuicaoContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdChamada.
    def enterCmdChamada(self, ctx:JanderParser.CmdChamadaContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdChamada.
    def exitCmdChamada(self, ctx:JanderParser.CmdChamadaContext):
        pass


    # Enter a parse tree produced by JanderParser#cmdRetorne.
    def enterCmdRetorne(self, ctx:JanderParser.CmdRetorneContext):
        pass

    # Exit a parse tree produced by JanderParser#cmdRetorne.
    def exitCmdRetorne(self, ctx:JanderParser.CmdRetorneContext):
        pass


    # Enter a parse tree produced by JanderParser#selecao.
    def enterSelecao(self, ctx:JanderParser.SelecaoContext):
        pass

    # Exit a parse tree produced by JanderParser#selecao.
    def exitSelecao(self, ctx:JanderParser.SelecaoContext):
        pass


    # Enter a parse tree produced by JanderParser#item_selecao.
    def enterItem_selecao(self, ctx:JanderParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by JanderParser#item_selecao.
    def exitItem_selecao(self, ctx:JanderParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by JanderParser#constantes.
    def enterConstantes(self, ctx:JanderParser.ConstantesContext):
        pass

    # Exit a parse tree produced by JanderParser#constantes.
    def exitConstantes(self, ctx:JanderParser.ConstantesContext):
        pass


    # Enter a parse tree produced by JanderParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:JanderParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by JanderParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:JanderParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by JanderParser#op_unario.
    def enterOp_unario(self, ctx:JanderParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by JanderParser#op_unario.
    def exitOp_unario(self, ctx:JanderParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by JanderParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:JanderParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by JanderParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:JanderParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by JanderParser#termo.
    def enterTermo(self, ctx:JanderParser.TermoContext):
        pass

    # Exit a parse tree produced by JanderParser#termo.
    def exitTermo(self, ctx:JanderParser.TermoContext):
        pass


    # Enter a parse tree produced by JanderParser#fator.
    def enterFator(self, ctx:JanderParser.FatorContext):
        pass

    # Exit a parse tree produced by JanderParser#fator.
    def exitFator(self, ctx:JanderParser.FatorContext):
        pass


    # Enter a parse tree produced by JanderParser#op1.
    def enterOp1(self, ctx:JanderParser.Op1Context):
        pass

    # Exit a parse tree produced by JanderParser#op1.
    def exitOp1(self, ctx:JanderParser.Op1Context):
        pass


    # Enter a parse tree produced by JanderParser#op2.
    def enterOp2(self, ctx:JanderParser.Op2Context):
        pass

    # Exit a parse tree produced by JanderParser#op2.
    def exitOp2(self, ctx:JanderParser.Op2Context):
        pass


    # Enter a parse tree produced by JanderParser#op3.
    def enterOp3(self, ctx:JanderParser.Op3Context):
        pass

    # Exit a parse tree produced by JanderParser#op3.
    def exitOp3(self, ctx:JanderParser.Op3Context):
        pass


    # Enter a parse tree produced by JanderParser#parcela.
    def enterParcela(self, ctx:JanderParser.ParcelaContext):
        pass

    # Exit a parse tree produced by JanderParser#parcela.
    def exitParcela(self, ctx:JanderParser.ParcelaContext):
        pass


    # Enter a parse tree produced by JanderParser#parcela_unario.
    def enterParcela_unario(self, ctx:JanderParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by JanderParser#parcela_unario.
    def exitParcela_unario(self, ctx:JanderParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by JanderParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:JanderParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by JanderParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:JanderParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by JanderParser#exp_relacional.
    def enterExp_relacional(self, ctx:JanderParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by JanderParser#exp_relacional.
    def exitExp_relacional(self, ctx:JanderParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by JanderParser#op_relacional.
    def enterOp_relacional(self, ctx:JanderParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by JanderParser#op_relacional.
    def exitOp_relacional(self, ctx:JanderParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by JanderParser#expressao.
    def enterExpressao(self, ctx:JanderParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by JanderParser#expressao.
    def exitExpressao(self, ctx:JanderParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by JanderParser#termo_logico.
    def enterTermo_logico(self, ctx:JanderParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by JanderParser#termo_logico.
    def exitTermo_logico(self, ctx:JanderParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by JanderParser#fator_logico.
    def enterFator_logico(self, ctx:JanderParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by JanderParser#fator_logico.
    def exitFator_logico(self, ctx:JanderParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by JanderParser#parcela_logica.
    def enterParcela_logica(self, ctx:JanderParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by JanderParser#parcela_logica.
    def exitParcela_logica(self, ctx:JanderParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by JanderParser#op_logico_1.
    def enterOp_logico_1(self, ctx:JanderParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by JanderParser#op_logico_1.
    def exitOp_logico_1(self, ctx:JanderParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by JanderParser#op_logico_2.
    def enterOp_logico_2(self, ctx:JanderParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by JanderParser#op_logico_2.
    def exitOp_logico_2(self, ctx:JanderParser.Op_logico_2Context):
        pass



del JanderParser