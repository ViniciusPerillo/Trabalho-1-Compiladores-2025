import sys
from antlr4 import *
from Jander import Jander

def main(argv):
    input_stream = FileStream(argv[1],encoding="utf-8")
    lexer = Jander(input_stream)
    token = lexer.nextToken()

    while token.type != Token.EOF:
        nome_token = Jander.symbolicNames[token.type]
        if nome_token in ['VARIAVEL', 'NUMINT', 'NUMREAL', 'PRES', 'LITERAL']:
            print(f"<{nome_token}, {token.text}>")
        else:
            print(f"<{nome_token}>")

        token = lexer.nextToken()

if __name__ == '__main__':
    main(sys.argv)