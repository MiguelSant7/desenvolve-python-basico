import random

def imprime_enforcado(tentativas):
    # Lê os estágios do enforcado
    with open("gabarito_enforcado.txt", "r") as f:
        estagios = f.read().strip().split("\n\n")  # Divide os estágios por duas quebras de linha
    print(estagios[tentativas])

def jogo_da_forca():
    # Abre o arquivo e escolhe uma palavra aleatoriamente
    with open("gabarito_forca.txt", "r") as f:
        palavras = f.read().strip().splitlines()
    
    palavra_selecionada = random.choice(palavras).lower()
    letras_adivinhadas = set()
    tentativas = 0
    max_tentativas = 6

    # Exibe o progresso inicial
    progresso = ["_" for _ in palavra_selecionada]
    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem {} letras: {}".format(len(palavra_selecionada), " ".join(progresso)))

    # Loop principal do jogo
    while tentativas < max_tentativas and "_" in progresso:
        letra = input("Adivinhe uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_adivinhadas.add(letra)

        if letra in palavra_selecionada:
            print("Boa! A letra '{}' está na palavra.".format(letra))
            # Atualiza o progresso
            for idx, char in enumerate(palavra_selecionada):
                if char == letra:
                    progresso[idx] = letra
        else:
            tentativas += 1
            print("Errado! Você tem {} tentativas restantes.".format(max_tentativas - tentativas))
            imprime_enforcado(tentativas)

        print("Progresso: {}".format(" ".join(progresso)))

    # Verifica o resultado do jogo
    if "_" not in progresso:
        print("Parabéns! Você adivinhou a palavra: '{}'".format(palavra_selecionada))
    else:
        print("Você perdeu! A palavra era: '{}'".format(palavra_selecionada))

# Executa o jogo
if __name__ == "__main__":
    jogo_da_forca()
