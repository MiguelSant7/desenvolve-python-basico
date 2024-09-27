import random

# Apresentação 
print("🤖_____Olá, sou a maquina do embaralhamento_____🤖\n")



# Função
def embaralhar_palavras(frase):
    palavras = frase.split()  
    palavras_embaralhadas = [] 

    for palavra in palavras:
        if len(palavra) > 3:  # Embaralha palavras com mais de 3 letras
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            letras_internas = list(palavra[1:-1])  # Pega as letras internas
            random.shuffle(letras_internas)  # Embaralha 
            # Reconstrutor
            palavra_embaralhada = primeira_letra + ''.join(letras_internas) + ultima_letra
        else:
            palavra_embaralhada = palavra  

        palavras_embaralhadas.append(palavra_embaralhada)  # Adiciona à lista

    return ' '.join(palavras_embaralhadas)  # Junção de palavras

# Saída
frase = input("Digite uma frase: ")
resultado = embaralhar_palavras(frase)
print(resultado)
