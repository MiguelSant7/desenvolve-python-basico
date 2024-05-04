#Verificando se um ano é bissexto ou não bissexto

#Entrada
verificando_ano = int(input("Escreva o ano que deseja verificar se é bissexto: "))


#Processamento/Saída
if (verificando_ano % 4 == 0 and verificando_ano % 100 != 0) or (verificando_ano % 400 == 0):
    print(f"O ano {verificando_ano} é bissexto.")
else:
    print(f"O ano {verificando_ano} não é bissexto.")
