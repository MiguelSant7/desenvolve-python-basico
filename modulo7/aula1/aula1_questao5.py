## Leitor de vogais


# Apresentação
print("______Contador de vogais_______\n")

# Entrada
string           = input("Digite uma frase: ")
vogais_definidas = ['a', 'e', 'i', 'o', 'u'] # Lista de vogais
string           = string.lower() # Transformaçao de upper cases para lowcase

cont          = 0 # Contador de vogais
indice_vogais = []

# Leitura da frase e filtro de vogais
for indice, caractere in enumerate(string):
    if caractere in vogais_definidas:
        cont += 1
        indice_vogais.append(indice)

# Impressão
print(f"Vogais: {cont}")
print(f"índices: {indice_vogais}")