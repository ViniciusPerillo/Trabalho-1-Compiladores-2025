lexer grammar Jander;
WS : [ \t\n\r]+ -> skip ;
COMMENT : '{' (~[\r\n])*? '}' -> skip;
P_RES : 'algoritmo' | 'fim_algoritmo' | 'declare' | 'leia' | 'escreva' | 'inteiro' | 'literal' | 'real' | 'logico' | 'se' | 'entao' | 'fim_se' | 'caso' |'senao' | 'fim_caso' | 'para' | 'faca' | 'fim_para' | 'enquanto' | 'fim_enquanto' | 'ate' | 'seja' | 'registro' | 'fim_registro' | 'tipo' | 'procedimento' | 'fim_procedimento' | 'var' | 'funcao' | 'fim_funcao' | 'retorne' | 'constante' | 'falso' | 'verdadeiro';

OP_LOG : 'e' | 'ou' | 'nao';

IDENT : ('a'..'z' | 'A'..'Z' | '_') ('a'..'z' | 'A'..'Z' | '0'..'9' | '_')*;
NUM_INT : ('0'..'9')+;
NUM_REAL : ('0'..'9')+ ('.' ('0'..'9')+)?;
CADEIA : '"' (~[\r\n])*? '"';

OP_REL : '>' | '>=' | '<' | '<=' | '<>' | '<-' | '=';
OP_ARIT : '+' | '-' | '*' | '/' | '%';

DELIM : ':';
ABREPAR : '(';
FECHAPAR: ')';
VIRGULA: ',';
INTERVALO: '..'; 
PONTEIRO: '^';
ENDERECO: '&';
STRUCT: '.';
VETOR: '[' | ']';



