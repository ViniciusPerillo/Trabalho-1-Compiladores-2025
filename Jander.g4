lexer grammar Jander;
WS : [ \t\n\r]+ -> skip ;
COMMENT : '{'.*?'}' -> skip;
PRES : 'algoritmo' | 'fim_algoritmo' | 'declare' | 'leia' | 'escreva' | 'inteiro' | 'literal';
VARIAVEL : ('a'..'z' | 'A'..'Z') ('a'..'z' | 'A'..'Z' | '0'..'9')*;
NUMINT : ('+'|'-')?('0'..'9')+;
NUMREAL : ('+'|'-')?('0'..'9')+ ('.' ('0'..'9')+)?;
LITERAL : '"'.*?'"';
OP_REL : '>' | '>=' | '<' | '<=' | '<>' | '<-';
OP_ARIT : '+' | '-' | '*' | '/';
DELIM : ':';
ABREPAR : '(';
FECHAPAR: ')';
VIRGULA: ',';

