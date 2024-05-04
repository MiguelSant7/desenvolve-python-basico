#Par ou ímpar

#Entrada
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

#Processamento/Saída
print("Par" if (numero_1+numero_2) % 2 == 0 else "Impar") #Se o resto(%) da soma dos dois números for divisivel por 0 é par, caso contrário, ímpar