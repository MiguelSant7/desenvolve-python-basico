###Questao2 - Soma e média dos valores da lista

#Importações
import random

#Entrada
num_elementos = random.randint(5, 20)
elementos     = []
soma          = 0

#Processamento
for i in range(num_elementos):
    valor = random.randint(1, 10)
    elementos.append(valor)
    soma += valor
    media = soma / num_elementos

#Saída
print(f"A lista de elementos é: {elementos}")
print(f"A soma dos valores da lista é: {soma}")
print(f"A média dos valores da lista é: {media:,.2f}")
 