#Questao3 - Jogo de adivinhação(random)

#Bibliotecas
import random

#Entrada
print("___Tente acertar um número aleatório de 1 a 10___")
numero_aleatorio = random.randint(0, 10)

#Processamento/Saída
while True:
    n = int(input("Digite um número: "))
    if n == numero_aleatorio:
        print("Você ganhou!!!")
        break
    elif n < numero_aleatorio:
        print("Mais")
    else:
        print("Menos")