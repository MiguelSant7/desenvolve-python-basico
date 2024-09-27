# Entrada
frase = input("Escreva uma frase: ").lower()

# Processamento
vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    frase = frase.replace(vogal, "*")

# Impressão
print(f"Frase: {frase}")