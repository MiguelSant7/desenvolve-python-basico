# Apresentação
print("_____Olá, sou o verificador de senhas_____\n")


# Processamento
def validador_Senha(senha):
    if len(senha) < 8:
        print("Senha inválida, deve ter pelo menos 8 caracteres.")
        return False
        
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero    = False
    tem_especial  = False
    
    # Definição dos caracteres especiais
    caracteres_especiais = "@#$%&*!?"
    
    # Filtro de caraceres
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in caracteres_especiais:
            tem_especial = True
    
    # Verificação
    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        print("Senha válida!")
        return True
    else:
        print("Senha inválida: deve conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.")
        return False

# Entrada
senha = input("Digite a sua senha: ")

# Processamento e saída
validador_Senha(senha)