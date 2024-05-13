#Questao1 - Numeros decimais absolutos

#Entrada
print("___Vamos calcular a diferença absoluta entre dois números___")
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))

#Processamento
diferenca = abs(round(n1 - n2, 2))

#Saída
print(f"A diferença absoluta entre {n1} - {n2} é: {diferenca}")