# Nome do arquivo
nome_arquivo = "estomago.txt"

# Inicializa variáveis
linhas = []
nonato_count = 0
iria_count = 0

# Lê o arquivo e processa as informações
with open(nome_arquivo, "r", encoding="ISO-8859-1") as arquivo:
    for linha in arquivo:
        linhas.append(linha.strip())  # Remove espaços em branco no início e no fim
        
        # Contagem de menções
        nonato_count += linha.lower().count("nonato")
        iria_count += linha.lower().count("íria")

# Impressão das informações solicitadas
print("Texto das primeiras 25 linhas:")
for i in range(min(25, len(linhas))):  # Garante que não exceda o número de linhas
    print(linhas[i])

# Número total de linhas
print(f"\nNúmero de linhas do arquivo: {len(linhas)}")

# Linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres: {linha_maior}")

# Número de menções aos personagens
print(f"\nNúmero de menções ao personagem 'Nonato': {nonato_count}")
print(f"Número de menções ao personagem 'Íria': {iria_count}")
