#Aposentadoria (M e F)
    #A: Para mulheres, ter mais de 60 anos. Para homens, 65.
    #B: Ou ter trabalhado pelo menos 30 anos
    #C: Ou ter 60 anos  e trabalhado pelo menos 25.

#Entrada
genero        = str(input("Digite seu genero, M para masculino e F para feminino: "))
idade         = int(input("Digite sua idade: "))
tempo_servico = int(input("Informe quanto tempo você possui de trabalho: "))

#Processamento
genero_m = genero == "M"
genero_f = genero == "F"


permissao_m = idade >= 65 or tempo_servico >= 30 or tempo_servico >= 25 and idade == 60 #Checando permissões
permissao_f = idade >= 60 or tempo_servico >= 30 or tempo_servico >= 25 and idade == 60 #Checando permissões

pode_aposentar = permissao_f and permissao_m #Confirmação

#Saída
print(f"Conferindo se pode aposentar: {pode_aposentar}")