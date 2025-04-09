import re

palavras_reservadas = {
    "algoritmo": "PRALG", 
    "fim_algoritmo": "PRFAÇG",
    "declarar": "PRDECL",
    "literal": "PRLIT",
    "inteiro": "PRINT",
    "leia": "PRLEIA",
    "escreva": "PRESCR"
}

simbolos = {
    "(": "ABREPAR",
    ")": "FECHAPAR",
    ",": "VIR",
    ":": "DP"
}

#operadores_aritimeticos

#operadores_relacionais


def remove_comentarios(texto):
    return re.sub(r"\{.*?\}", "", texto, flags=re.DOTALL)

def analisar_lexicamente(texto):
    tokens = []
    texto_sem_comentarios = remove_comentarios(texto)

    linhas = texto_sem_comentarios.splitlines()
    variaveis = set()
    declarando = False

    for linha in linhas:
        linha = linha.strip()

        # Pular linhas vazias
        if not linha:
            continue

        # Verifica se a linha inicia uma declaração
        if linha.startswith("declarar"):
            tokens.append("<declarar, PRALG>")
            declarando = True
            continue

        # Enquanto estiver declarando
        if declarando and ":" in linha:
            partes = linha.split(":")
            if len(partes) == 2:
                var = partes[0].strip()
                tipo = partes[1].strip()
                variaveis.add(var)

                tokens.append(f"<{var}, ID>")
                tokens.append("<:, DP>")
                tokens.append(f"<{tipo}, PRVAR>")
            continue

        # Sai do modo declaração se encontrar uma nova palavra-chave fora da declaração
        declarando = False

        # Agora processa normalmente a linha
        padrao = r'\".*?\"|\w+|[(),:]'
        palavras = re.findall(padrao, linha)

        for token in palavras:
            if token in palavras_reservadas.keys():
                tokens.append(f"<{token}, PR>")
            elif token in simbolos:
                tokens.append(f"<{token}, {simbolos[token]}>")
            elif token.isdigit():
                tokens.append(f"<{token}, NUM>")
            elif re.fullmatch(r'\".*\"', token):
                tokens.append(f"<{token}, LIT>")
            elif token in variaveis:
                tokens.append(f"<{token}, VAR>")  # ou VAR se quiser marcar diferente
            else:
                tokens.append(f"<{token}, VAR>")

    return tokens

# Leitura do arquivo
with open("programa.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Análise
tokens = analisar_lexicamente(conteudo)

# Escrita da saída
with open("saida.txt", "w", encoding="utf-8") as f:
    for token in tokens:
        f.write(token + "\n")
