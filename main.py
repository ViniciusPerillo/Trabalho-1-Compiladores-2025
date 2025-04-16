import sys
import os
import re
from io import StringIO
from antlr4 import *
from Jander import Jander
from antlr4.error.ErrorListener import ErrorListener

class JanderError(ErrorListener):
    def __init__(self, output: StringIO):
        super().__init__()
        self.out = output
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if '\\n' in msg or '\\r' in msg:
            if '{' in msg:
                print(f'Linha {line}: comentario nao fechado', file= self.out)
            elif '"' in msg:
                print(f'Linha {line}: cadeia literal nao fechada', file= self.out)
        else:
            print(f'Linha {line}: {re.search(r"'(.*?)'", msg).group(1)} - simbolo nao identificado', file= self.out)

def main(argv):
    input_stream = FileStream(argv[1],encoding="utf-8")
    output = argv[2]
    lexer = Jander(input_stream)
    token = lexer.nextToken()

    with open(output, mode='w') as out:
        lexer.removeErrorListeners()
        lexer.addErrorListener(JanderError(out))
        while token.type != Token.EOF:
            nome_token = Jander.symbolicNames[token.type]
            if nome_token in ['IDENT', 'NUM_INT', 'NUM_REAL', 'CADEIA']:
                print(f"<'{token.text}',{nome_token}>", file= out)
            else:
                print(f"<'{token.text}','{token.text}'>", file= out)

            token = lexer.nextToken()


if __name__ == '__main__':
    main(sys.argv)

# def tester(argv):
#     output = argv[2]
#     saida_correta = argv[1].split('entrada')
#     with open(output, mode='r') as f:
#         out_lines = f.readlines()

#     with open('saida'.join(saida_correta), mode= 'r') as f:
#         corr = f.readlines()

#     for idx in range(len(corr)):
#         if corr[idx] != out_lines[idx]:
#             print(f'{idx}: linha deveria ser {corr[idx]} ao inves de {out_lines[idx]}')
        

# def run():
#     root = 'C:\\UFSCAR\\COMPILADORES\\Trabalho-1-Compiladores-2025\\testes\\entrada\\'
#     for case in os.listdir(root):
#         args = [None, root + case, 'output.txt']
#         print(case)
#         print('\n\n')
#         main(args)
#         tester(args)
#         print('\n\n\n\n\n')

# if __name__ == '__main__':
#     run()