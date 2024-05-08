##Questao1 - Transformando em código

#Leia "x"
#Se "x" não for maior que 5, imprima "Fim"
#Se "x" for maior que 5, imprima "Maior que 5"

#Entrada
x = int(input("Digite um número: "))

#Processamento/Saída
while x > 5:
    print("Maior que 5")
    x = int(input("Digite um número: "))

print("Fim")