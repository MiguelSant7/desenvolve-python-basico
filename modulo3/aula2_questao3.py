#Jogos de tabuleiro (Confirmação de idade, quantidade de jogos e quantas vezes venceu)
    #tiver entre 16 e 18 anos
    #já tiver jogado pelo menos 3 jogos
    #já ter vencido pelo menos 1 jogo, 

#Entrada
idade_jogador       = int(input("Digite a sua idade: "))
partidas_jogadas    = int(input("Agora diga quantos jogos participou: "))
jogos_ganhos        = int(input("Desses jogos, diga quantos você ganhou:  "))

#Processamento
idade_permitida     = idade_jogador >= 16 and idade_jogador <= 18
partidas_permitidas = partidas_jogadas >= 3
partidas_vencidas   = jogos_ganhos >= 1

aptidao = idade_permitida and partidas_jogadas and partidas_vencidas

#Saída
print(f"apto a ingressar no clube: {aptidao}")