## Questão1

## Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
# Lista de entrada
lista_pares = []

# Processamento(Achando pares e colocando na lista)
for i in range(20, 51):
    if i % 2 == 0:
        lista_pares.append(i)

# Saída
# print(lista_pares)
        

## Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]

# Entrada/Processamento
lista     = [1,2,3,4,5,6,7,8,9]
quadrados =  list(x ** 2 for x in lista)

lista_quadrados = (quadrados) 

# Saída
# print(lista_quadrados)


## Todos os números entre 1 e 100 que sejam divisíveis por 7

# Entrada/Processamento
lista_7 = []
for i in range(1, 100):
    if i % 7 == 0:
        lista_7.append(i)

# Saída
# print(lista_7)

       
## Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex: ['par', 'impar',… , 'impar'])

# Lista de Entrada
par_impar = []

# Processamento
for i in range(0, 30, 3):
    if i % 2 == 0:
        par_impar.append("Par")
    else:
        par_impar.append("ímpar")

# Saida
# print(par_impar)
        


