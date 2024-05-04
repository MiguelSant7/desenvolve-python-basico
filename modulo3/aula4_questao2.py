#Avaliando filmes

#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

#Entrada
avaliação = int(input("Avalie o filme em uma escala de 1 a 5: "))

#Processamento/Saída
if avaliação == 5:
    print("Exelente!")
elif avaliação == 4:
    print("Muito Bom!")
elif avaliação == 3:
    print("Bom!")
elif avaliação == 2:
    print("Regular.")
elif avaliação == 1:
    print("Ruim.")
else:
    print("Sua nota é inválida")
