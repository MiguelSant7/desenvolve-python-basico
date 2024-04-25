#Calculo de notas necessárias

#Entrada
valor_reais = int(input("Digite um valor: "))

#Notas
notas_100   = valor_reais // 100
valor_reais = valor_reais % 100

notas_50    = valor_reais // 50
valor_reais = valor_reais % 50

notas_20    = valor_reais // 20
valor_reais = valor_reais % 20

notas_10    = valor_reais // 10
valor_reais = valor_reais % 10

notas_5     = valor_reais // 5
valor_reais = valor_reais % 5

#Saída
print(f"São necessárias {notas_100} notas de R$100")
print(f"São necessárias {notas_50} notas de R$100")
print(f"São necessárias {notas_20} notas de R$100")
print(f"São necessárias {notas_10} notas de R$100")
print(f"São necessárias {notas_5} notas de R$100")
