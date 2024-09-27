import random

def encrypt(nomes):
    # Gerar um valor n aleatório entre 1 e 10
    chave = random.randint(1, 10)
    
    nomes_criptografados = []  # Lista para armazenar os nomes criptografados
    
    # Percorrer cada nome na lista de nomes
    for nome in nomes:
        nome_criptografado = ""
        # Criptografar cada caractere do nome
        for caractere in nome:
            novo_caractere = ord(caractere) + chave  # Deslocar o caractere pela chave
            if novo_caractere > 126:  # Se passar do limite 126, voltamos para o início (33)
                novo_caractere = 33 + (novo_caractere - 127)
            nome_criptografado += chr(novo_caractere)
        
        # Adicionar o nome criptografado à lista
        nomes_criptografados.append(nome_criptografado)
    
    return nomes_criptografados, chave

# Exemplo de uso
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

# Impressão dos resultados
print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_cript}")
