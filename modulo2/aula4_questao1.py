#Um programa para calcular m2 da área total de um terreno

#Entrada
largura       = int (input("Digite a largura do terreno em metros: "))
comprimento   = int (input("Digite o comprimento do terreno em metros: "))
valor_terreno = float (input("Digite o valor do terreno: "))

#Processamento
area_terreno = largura * comprimento        #calculo para descobrir área total largura * cumprimento
valor_por_m2 = valor_terreno / area_terreno #Divisão da área total pelo valor do terreno

#Saída
print(f"O terreno possui {area_terreno}m2 e cada m2 custa RS${valor_por_m2:,.2f}")