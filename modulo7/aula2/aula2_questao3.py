# Apresentação 
print("_____Verificador de palíndromo______\n")

# Entrada


# Processamento

while True:
    palavra = input("Digite uma palavra: ")
    if palavra.lower() == "Fim".lower():
        print("Programa finalizado.")
        break

    # Invertendo a palavra
    inverso = palavra[::-1]

    # Verificação
    if palavra == inverso:
        print(f'"{palavra}" é um palíndromo.')
    else:
        print(f'"{palavra}" não é um palíndromo.')
