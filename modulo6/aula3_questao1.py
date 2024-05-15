#Questao1 - Fatiamento de lista


#Entrada
print("Digite pelo menos 4 números inteiros (Digite 0 para parar):")


#Processamento
numeros = []
while True:
    numero = int(input("Digite um número inteiro: "))
    if numero == 0 and len(numeros) >= 4:
        break
    elif numero == 0:
        print("Você precisa digitar pelo menos 4 números inteiros")
    else:
        numeros.append(numero)


#Saída
print("Lista original:", numeros)                  #Imprimir a lista original
print("Os 3 primeiros elementos:", numeros[:3])    #Imprimir os 3 primeiros elementos
print("Os 2 últimos elementos:", numeros[-2:])     #Imprimir os 2 últimos elementos
print("Lista invertida:", numeros[::-1])           #Imprimir a lista invertida
print("Elementos de índice par:", numeros[::2])    #Imprimir os elementos de índice par
print("Elementos de índice ímpar:", numeros[1::2]) #Imprimir os elementos de índice ímpar