#Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados

#Entrada de dados

#Produto 1
nome_1       = str(input("Digite o nome do primeiro produto: "))
preço_1      = float(input("Digite o preço unitário desse produto: "))
quantidade_1 = int(input("Digite a quantidade desse produto:"))
total_1      = preço_1 * quantidade_1

#Produto 2
nome_2       = str(input("Digite o nome do segundo produto: "))
preço_2      = float(input("Digite o preço unitário desse produto: "))
quantidade_2 = int(input("Digite a quantidade desse produto:"))
total_2      = preço_2 * quantidade_2

#Produto 3
nome_3       = str(input("Digite o nome do terceiro produto: "))
preço_3      = float(input("Digite o preço unitário desse produto: "))
quantidade_3 = int(input("Digite a quantidade desse produto:"))
total_3      = preço_3 * quantidade_3

#Total de compras
total_compras = total_1 + total_2 + total_3
formatação    = f"R${total_compras:,.2f}"

#Saída
print(f"Total: {formatação}")
