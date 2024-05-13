#Questao2 - Raiz dos aleatórios(random(randint)), math(sqtr)

#Bibliotecas
import math
import random

#Entrada
print("___Informe um valor entre 1 e 100 e acharemos a raiz da soma desses valores___")
n = int(input("Digite um valor: "))
soma = 0

#Processamento
for i in range(n):
 valores = random.randint(0, 100)
 soma += valores

raiz = math.sqrt(soma)

print(f"A raiz da soma é {raiz}")




