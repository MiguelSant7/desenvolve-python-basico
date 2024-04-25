#Classe de RPG (Pontos)]
    #Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
    #Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
    #Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.77

#Entrada
classe       = str(input("Digite a sua classe: "))
pontos_força = float(input("Digite os pontos de força: "))
pontos_magia = float(input("Digite os pontos de magia: "))

#Processamento
classe_guerreiro = classe == ("Guerreiro" or "guerreiro") and pontos_força >= 15 and pontos_magia <=10
classe_mago      = classe == ("Mago"      or "mago")      and pontos_força <= 10 and pontos_magia >= 15
classe_arqueiro  = classe == ("Arqueiro"  or "arqueiro")  and  pontos_força > 5  and pontos_força < 15.77, pontos_magia > 5 and pontos_magia < 15.77


permissao = classe_guerreiro or classe_mago or classe_arqueiro #Confirmaçãos

#Saída
print(f"Conferindo pontos: {permissao}")


