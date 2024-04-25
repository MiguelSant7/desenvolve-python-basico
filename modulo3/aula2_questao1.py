#Leitura e confirmação de idades

#Entrada
Juliana_idade = int(input("Qual a idade de Juliana? "))
Cris_idade    = int(input("Qual a idade de Cris? "))

#Processamento
liberação = Juliana_idade and Cris_idade >= 18

#Saída
print (f"Conferindo liberação: {liberação}")