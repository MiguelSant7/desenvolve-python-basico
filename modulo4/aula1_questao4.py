##Questao4 - Encontrando o maior

#Leia "n"
#Defina o maior como 0
#Se 0 for maior que n leia "x"
#Se x for maior que o maior, maior ganhará o valor de x
#Se x nao for maior que o maior, tire 1 de n
#Se n nao for maior que o maior, imprima o valor

#Entrada
n     = int(input("Digite o valor: "))
maior = 0 

#Processamento/Saída
while n > 0:
    x = int(input(""))
    if x > maior:
        maior = x
    n -= 1
print(f"O maior valor é: {maior}")