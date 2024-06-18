## Questão2

# Entrada
frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

# Processamento
lista_vogais = [letra for letra in frase if letra in vogais]
lista_consoantes = [letra for letra in frase if letra not in vogais and letra.isalnum()]

lista_vogais.sort()

# Saída
print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)