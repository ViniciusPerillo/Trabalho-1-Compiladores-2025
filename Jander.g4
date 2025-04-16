lexer grammar Jander;
WS : [ \t\n\r]+ -> skip ;
COMMENT : '{'.*?'}' -> skip;
P_RES : 'algoritmo' | 'fim_algoritmo' | 'declare' | 'leia' | 'escreva' | 'inteiro' | 'literal' | 'real' | 'logico' | 'se' | 'entao' | 'fim_se' | 'caso' |'senao' | 'fim_caso' | 'para' | 'faca' | 'fim_para' | 'enquanto' | 'fim_enquanto' | 'ate';
OP_LOG : 'e' | 'ou' | 'nao';

IDENT : ('a'..'z' | 'A'..'Z') ('a'..'z' | 'A'..'Z' | '0'..'9')*;
NUM_INT : ('+'|'-')?('0'..'9')+;
NUM_REAL : ('+'|'-')?('0'..'9')+ ('.' ('0'..'9')+)?;
CADEIA : '"'.*?'"';

OP_REL : '>' | '>=' | '<' | '<=' | '<>' | '<-' | '=';
OP_ARIT : '+' | '-' | '*' | '/';

DELIM : ':';
ABREPAR : '(';
FECHAPAR: ')';
VIRGULA: ',';
INTERVALO: '..'; 
PONTEIRO: '^';
ENDERECO: '&';




