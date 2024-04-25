#Programa de conversão para graus Fahrenheit em Celsius

#Entrada
fahrenheit = float (input("Digite o valor de Fahrenheit: "))

#Processamento
celsius    = (fahrenheit - 32) * 5 / 9 #Fórmula de conversão de Fahrenheit para Celsius (Alternativa: C=(F-32)/1,8))

#Saída
print (f"{fahrenheit} fahrenheit são {int (celsius)} graus celsius")