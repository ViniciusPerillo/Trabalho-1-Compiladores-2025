import sys
import os
from antlr4 import *
from Jander import Jander

def main(argv):
    input_stream = FileStream(argv[1],encoding="utf-8")
    output = argv[2]
    lexer = Jander(input_stream)
    token = lexer.nextToken()

    with open(output, mode='w') as out:
        while token.type != Token.EOF:
            nome_token = Jander.symbolicNames[token.type]
        
            if nome_token in ['IDENT', 'NUM_INT', 'NUM_REAL', 'CADEIA']:
                print(f"<'{token.text}',{nome_token}>", file= out)
            else:
                print(f"<'{token.text}','{token.text}'>", file= out)

            token = lexer.nextToken()

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
        

# if __name__ == '__main__':
#     main(sys.argv)
#     tester(sys.argv)


def run():
    root = 'D:\\gitRep\\Trabalho-1-Compiladores-2025\\casos_de_teste\\entrada\\'
    for case in os.listdir(root):
        args = [None, root + case, 'output.txt']
        print(case)
        print('\n\n')
        main(args)
        tester(args)
        print('\n\n\n\n\n')

if __name__ == '__main__':
    run()