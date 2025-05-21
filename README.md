# Trabalhos Compiladores

* Ana Ellen Deodato da Silva, 800206
* Gabriel Vianna Spolon, 811649
* Vinicius Gonçalves Perillo, 800219

# T1

## Bibliotecas

Este trabalho foi feito inteiramente em Python, usando a bibioteca **Antlr**:

Antlr é uma biblioteca usada para criar e interpretar linguagens, como se fosse um motor de parser (analisador de texto). Você escreve a gramática da linguagem e o Antlr gera código que entende e processa textos seguindo essa gramática.

Baixar em: [https://www.antlr.org/download.html](url) a versão 4.13.2. Após isso, é preciso colocar o arquivo na pasta do projeto e rodar:

> java -jar ./antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor Jander.g4

Isto vai fazer com que a biblioteca crie o analisador Jander.py segundo a Gramática Léxica de Jander.g4.

## Configurações

* Python - Versão mais atualizada disponível
* Java - Versão mais atualizada disponível

## Como executar

Aṕos executar o comando da biblioteca, basta executar:

> python3 main.py <input.txt> <output.txt>

# T2

Este trabalho também foi feito inteiramente em Python, usando a biblioteca Antlr.

Ela continua sendo usada para gerar automaticamente os analisadores léxico e agora também o sintático a partir da gramática da linguagem LA (Linguagem Algorítmica), fornecida pelo professor.

A execução e configurações deste trabalho são as mesmas que do T1.