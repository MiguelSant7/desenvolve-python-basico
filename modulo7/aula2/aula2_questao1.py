#Apresentação
print("______Olá, digite uma data e eu vou escreve-la por extenso______\n")

# Entrada 
data = input("Digite sua data de nascimento(XX/XX/XXXX): ")

# Dados com os nomes dos meses

meses = ['janeiro', 
         'fevereiro', 
         'março', 
         'abril', 
         'maio', 
         'junho', 
         'julho', 
         'agosto', 
         'setembro', 
         'outubro', 
         'novembro', 
         'dezembro', 
]

# Separação
dia, mes, ano = data.split("/")

# Conversão
mes_por_extenso = meses[int(mes) - 1]

# Impressão
print(f"Você nasceu no dia {dia} de {mes_por_extenso} de {ano}")