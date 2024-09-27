## Programa para identificação de número de celular

# Entrada do número
numero = input("Informe seu número: ")

# Avaliando a quantidade de elementos

if len(numero) == 8:
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":
    print("Número invalido")

# Imprimindo
numero_formatado = f"{numero[:5]}-{numero[:5]}"

print(numero_formatado)

