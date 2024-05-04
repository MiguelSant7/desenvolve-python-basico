#Calculando o valor do frete

#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

#Entrada 
distancia_km   = int(input("Informe a distância da entrega: "))
peso_do_pacote = int(input("Informe o peso do pacote: "))

#Processamento/Saída
if distancia_km <=100:
    frete = peso_do_pacote * 1
    print(f"- O frete é de {frete}")
elif distancia_km >=101 and distancia_km <= 300:
    frete = peso_do_pacote * 1.5
    print (f"- O frete é de {frete}")
else:
    frete = peso_do_pacote * 2
    print(f"- O frete é de {frete}")

##Taxa adicional
if peso_do_pacote > 10:
    frete = frete + 10
    print("- Taxa de R$10,00 por exceder 10kg.")

#Sáida(Taxa final)
print(f"O valor final do frete é R${frete}")
