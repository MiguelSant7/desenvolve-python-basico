##Questao6 - Contando cobaias


#entrada
#####n_sapos, n_ratos, n_coelhos = int(input("Informe quantos sapos: ")), int(input("Quantos ratos? ")), int(input("Quantos coelhos? "))
#####total_n = n_sapos + n_ratos + n_coelhos


#####Percentual
#####Percentual_sapos   = (n_sapos / total_n) * 100
#####Percentual_ratos   = (n_ratos / total_n) * 100
#####Percentual_coelhos = (n_coelhos / total_n) * 100

#processamento
cont         = 0
soma         = 0
soma_sapos   = 0
soma_ratos   = 0
soma_coelhos = 0

n    = int(input("Informe o número de cobaias: "))

while cont < n:
    quant = int(input("Informe a quantidade: "))
    tipo  = str(input("Informe o tipo(Sapo, Rato, Coelho): "))
    if tipo == "Sapo":
        soma_sapos += quant
    elif tipo == "Rato":
        soma_ratos += quant
    elif tipo == "Coelho":
        soma_coelhos += quant
    else:
        print("Nome de cobaia inválida")
    cont += 1

#Percentual
total_cobaias = soma_sapos + soma_ratos + soma_coelhos
Percentual_sapos   = (soma_sapos / quant) * 100
Percentual_ratos   = (soma_ratos / quant) * 100
Percentual_coelhos = (soma_coelhos / quant) * 100


#Saida(Total)
print (f"Total de cobaias {soma_sapos+soma_ratos+soma_coelhos}")
print ("Total de sapos: ", soma_sapos)
print ("Total de ratos: ", soma_ratos)
print ("Total de coelhos: ", soma_coelhos)

#Saída(Percentual)
print ("Percentual do sapo: ", Percentual_sapos)
print ("Percentual do rato: ", Percentual_ratos)
print ("Percentual do coelho: ", Percentual_coelhos)

