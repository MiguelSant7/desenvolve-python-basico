import os
import re

# Nome dos arquivos
arquivo_frase = "frase.txt"
arquivo_palavras = "palavras.txt"

# Lê "frase.txt"
with open(arquivo_frase, "r") as arquivo:
    conteudo = arquivo.read()

# Remove caracteres não alfabéticos e espaços em branco
# Usa expressão regular para manter apenas letras e espaços
conteudo_limpo = re.sub(r'[^a-zA-Z\s]', '', conteudo)

# Separa as palavras e remove espaços em branco adicionais
palavras = conteudo_limpo.split()

# Salva as palavras no arquivo "palavras.txt"
with open(arquivo_palavras, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")  # Escreve cada palavra em uma nova linha

# Lê e imprime o conteúdo do arquivo "palavras.txt"
with open(arquivo_palavras, "r") as arquivo:
    conteudo_palavras = arquivo.read()
    print(conteudo_palavras)
