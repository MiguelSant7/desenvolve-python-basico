###Questao4 - interagindo com a lista do usuário


#Entrada/Processamento
n1     = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []

for i in range(n1):
    elementos1 = int(input(f"Digite os {n1} elementos da lista 1: "))
    lista1.append(elementos1)


#----------
n2     = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []

for i in range(n2):
    elementos2 = int(input(f"Digite os {n2} elementos da lista 1: "))
    lista2.append(elementos2)

lista_intercalada = []
tamanho_minimo = min(len(lista1), len(lista2))

for i in range(tamanho_minimo):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

for elemento in lista1[tamanho_minimo:]:
    lista_intercalada.append(elemento)

for elemento in lista2[tamanho_minimo:]:
    lista_intercalada.append(elemento)


#Saída
print("Lista intercalada:", lista_intercalada)
