# Função para ordenar os caracteres de uma palavra
def ordenar_palavra(palavra):
    return ''.join(sorted(palavra))

# Apresentação
print("______Encontrar Anagramas_______\n")

# Entrada da frase
frase = input("Digite uma frase: ").lower()  # Convertendo a frase para minúsculas

# Entrada da palavra objetivo
palavra_objetivo = input("Digite a palavra objetivo: ").lower()

# Ordenando a palavra objetivo para comparação
palavra_ordenada = ordenar_palavra(palavra_objetivo)

# Lista para armazenar anagramas encontrados
anagramas = []

# Separando a frase em palavras e verificando cada uma
for palavra in frase.split():
    # Remover caracteres não alfabéticos da palavra
    palavra_limpa = ''.join(letra for letra in palavra if letra.isalpha())
    
    # Comparar a palavra limpa ordenada com a palavra objetivo ordenada
    if ordenar_palavra(palavra_limpa) == palavra_ordenada:
        anagramas.append(palavra)

# Imprimindo os anagramas encontrados
print(f"Anagramas: {anagramas}")