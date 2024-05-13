#Questao5 - Emojis

#Bibliotecas
import emoji

#Entrada
emojis_disponiveis = {
    ":red_heart:": "❤️", 
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
    }

#Processamento
print(emojis_disponiveis)
for codigo, emoji_unicode in emojis_disponiveis.items():
    print(f"{codigo} - {emoji_unicode}")

frase = input("Digite uma frase que será emojizada: ")

frase_emoji = emoji.emojize(frase) #Emojizando a frase

#Saída
print("\nFrase emojizada: ", frase_emoji)