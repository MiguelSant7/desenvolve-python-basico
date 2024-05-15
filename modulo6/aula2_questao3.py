#Questao3 - Intersecções das listas aleatórias

#Importações
import random

#Lista de intersecções
interseccao = []

#Processamento
for i1 in range(20):
        lista1 = [random.randint(0, 50) for i in range(10)]
        lista2 = [random.randint(0, 50) for i in range(10)]

for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
        interseccao.append(elemento)

#Contando intersecções(precisei estudar conteúdo externo)
contagem = {elemento: interseccao.count(elemento) for elemento in interseccao}

#Saída
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Intersecção: {interseccao}")
print(f"Contagem: {contagem}")