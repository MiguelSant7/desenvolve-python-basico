# Programa que pega o nome do usuário e imprime de forma crescente(+1 letra por linha)


# Entrada
nome = input("Informe seu nome: ")

# Função lambda par ler e imprimir em ordem 
func = lambda nome: [print(nome[:i]) for i in range(1, len(nome) + 1)]

# Chamado da função
func(nome)


#### Modo alternativo #####

# for i in range(1, len(nome) + 1):
#     print(nome[:i])  

###########################