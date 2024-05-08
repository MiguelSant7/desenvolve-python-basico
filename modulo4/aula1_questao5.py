##Questao5 - Média de idades

#Ler um inteiro "n"(Quantidade de respondentes)
#Leia as n idades de cada respondente
#imprimir a média de idades
#(idade1 + idade2 + idade3 + … + idade_n)/n


#Entrada
numero_de_idades = int(input("informe o número de idades: "))
contador         = 0 
soma             = 0

#Processamento
while contador < numero_de_idades:
    idade = int(input("Informe a idade:"))
    soma += idade
    contador += 1
media_idades = soma / numero_de_idades

#Saída
print(media_idades)