##Questao2 - Contador

#Leia "n"
#Zere o contador(cont)
#Enquanto "n" for menor que o contador, adicione +1 ao contador e imprima, leia novamente se n < cont
#se "n" nao for menor que o contador, encerre o programa imprimindo "Fim"

#entrada
n    = int(input("Escreva um número: "))
cont = 0

#processamento
while cont < n:
    cont += 1
    print(cont)
print("Fim")
