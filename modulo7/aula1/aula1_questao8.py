def calcular_primeiro_digito(cpf):
    # Extrair os primeiros 9 dígitos do CPF
    cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()]
    
    # Verificar se o CPF possui pelo menos 9 dígitos
    if len(cpf_numeros) < 9:
        return None  # Retorna None se o CPF for inválido
    
    # Multiplicadores de 10 a 2
    multiplicadores = list(range(10, 1, -1))
    
    # Calcular a soma dos produtos
    soma = sum(cpf_numeros[i] * multiplicadores[i] for i in range(9))
    
    # Calcular o resto da divisão por 11
    resto = soma % 11
    
    # Definir o primeiro dígito verificador
    if resto < 2:
        return 0
    else:
        return 11 - resto

# Solicitar o CPF do usuário
cpf = input("Digite um CPF no formato XXX.XXX.XXX-XX: ")

# Remover caracteres especiais e verificar o primeiro dígito
primeiro_digito_calculado = calcular_primeiro_digito(cpf)

# Comparar com o primeiro dígito verificador informado no CPF
if primeiro_digito_calculado is not None:
    primeiro_digito_informado = int(cpf[12])
    if primeiro_digito_calculado == primeiro_digito_informado:
        print("Primeiro dígito verificador é válido.")
    else:
        print("Primeiro dígito verificador é inválido.")
else:
    print("CPF inválido.")