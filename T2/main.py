import os
import sys
import re
from io import TextIOBase
from antlr4 import *
from JanderLexer import JanderLexer
from JanderParser import JanderParser
from antlr4.error.ErrorListener import ErrorListener
from io import StringIO


# Exceção personalizada para interromper parsing imediatamente após o primeiro erro
class InterromperParsing(Exception):
    pass

class JanderLexerError(ErrorListener):
    '''
    Classe que herda ErrorListener para alaterar as mensagens de erro do lexer
    Inputs:
        output: StringIO -> arquivo IO que o print ira escrever
    '''
    def __init__(self, output: StringIO):
        super().__init__()
        self.out = output
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(msg)
        # Trata erros de quebra de linha onde não deveria
        if '\\n' in msg or '\\r' in msg:
            # Quebra no Comentário
            if '{' in msg:
                print(f'Linha {line}: comentario nao fechado', file= self.out)
            #Quebra na Cadeia
            elif '"' in msg:
                print(f'Linha {line}: cadeia literal nao fechada', file= self.out)
        # Trata outros erros de símbolo não reconhecido
        else:
            print(f'Linha {line}: {re.search(r"'(.*?)'", msg).group(1)} - simbolo nao identificado', flush= True, file= self.out)
            #print(msg)
        
        print("Fim da compilacao", file=self.out)
        sys.exit()
        
    
class JanderParserError(ErrorListener):
    '''
    Classe que herda ErrorListener para alaterar as mensagens de erro do parser
    Inputs:
        output: StringIO -> arquivo IO que o print ira escrever
    '''
    def __init__(self, output: StringIO):
        super().__init__()
        self.out = output
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(msg)
        # Trata o erro específico de EOF
        if 'EOF' in msg:
            print(f'Linha {line}: erro sintatico proximo a EOF', flush= True, file= self.out)
        elif 'missing' in msg:
            print(f'Linha {line}: erro sintatico proximo a {re.search(r"at '(.*?)'", msg).group(1)}', flush= True, file= self.out)
        elif 'extraneous' in msg or 'mismatched' in msg:
            #print(f'Linha {line}: erro sintatico proximo a {re.search(r"input '(.*?)'", msg).group(1)}', flush= True, file= self.out)
            print(f'Linha {line}: erro sintatico proximo a {offendingSymbol.text}', flush= True, file= self.out)

        elif 'alternative' in msg:
            print(f'Linha {line}: erro sintatico proximo a {re.search(r"input '(.*?)'", msg).group(1)[-1]}', flush= True, file= self.out)
            
        print("Fim da compilacao", file=self.out)
        
        sys.exit()



def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
    output_path = argv[2]

    with open(output_path, 'w', encoding='utf-8') as out:
        # Listener Lexer
        lexer = JanderLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(JanderLexerError(out))

        token_stream = CommonTokenStream(lexer)
        # Listener Parser
        parser = JanderParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(JanderParserError(out))

        try:
            parser.header()
        except InterromperParsing:
            # Interrompe análise após o primeiro erro
            pass
        except:
            # Ignora outras exceções do ANTLR
            pass

        

# Código para teste em massa de todos os casos
def tester(argv):
    output = argv[2]
    saida_correta = argv[1].split('entrada')
    with open(output, mode='r') as f:
        out_lines = f.readlines()

    with open('saida'.join(saida_correta), mode= 'r') as f:
        corr = f.readlines()

    for idx in range(len(corr)):
        if corr[idx] != out_lines[idx]:
            print(f'{idx}: linha deveria ser {corr[idx]} ao inves de {out_lines[idx]}')
            raise KeyboardInterrupt
            
# Código para teste em massa de todos os casos
def run():
    #root = '<path>'
    for case in sorted(os.listdir(root)):
        args = [None, root + case, 'output.txt']
        print(case)
        print('\n\n')
        main(args)
        tester(args)
        print('\n\n\n\n\n')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        run()
    else:
        main(sys.argv)
