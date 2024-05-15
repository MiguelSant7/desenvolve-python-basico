###Questao1 - Lista ordenada, original, índice de maior valor

#Importações
import random

#Entrada/Processamento
lista = []

for i in range(20):
    lista_aleatoria = random.randint(-100, 100)
    lista.append (lista_aleatoria)

maior = lista.index (max(lista)) 
menor = lista.index (min(lista))

#Saída
print(f"A lista ordenada é: {sorted(lista)} ")
print(f"A lista original é: {lista}")
print(f"O índice do maior valor da lista é: {maior}")
print(f"O índice do menor valor da lista é: {menor}")