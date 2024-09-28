import os

# Entrada
frase = input("Digite uma frase: ")

# Arquivo
nome_arquivo = 'frase.txt'

# Salvando frase
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(frase)


# Caminho
caminho_completo = os.path.abspath(nome_arquivo)


# Impressão 
print(f"Frase salva em: {caminho_completo}")