##Questao3 - Revisando notas

#Leia n1, n2, n3
#Defina que n1 + n2 + n3 / 3 esteja dentro da variável "m"
#Se m for mair ou igual a 60, imprima "Aprovado -> imprima "Fim"
#Se m for >= 40, imprima "Recuperação" -> imprima "Fim"
#Caso não seja maior que 40 imprima "Reprovado" -> "Fim"

#Entrada
n1, n2, n3 = int(input("Informe o primeiro número: ")), int(input("Informe o segundo número: ")) \
    , int(input("Informe o terceiro número: "))

m = (n1 + n2 + n3) / 3

#Processamento/Saída
while m <= 60:
    if m >= 60:
        print("Aprovado")
        m == 60
    elif m >= 40:
        print("recuperação")
    else:
        print("Reprovado")
    m = 61
print("Fim")


