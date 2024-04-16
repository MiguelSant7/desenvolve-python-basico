#Armazene o texto "o resultado é"  em uma variável, o valor 10 em outra variável, e o valor 3.5 numa terceira variável.
variavel_texto       = "o resultado é"
variavel_valor_int   = 10
variavel_valor_float = 3.5

#Some os valores da segunda e terceira variável e armazene em outra variável.
variavel_soma = variavel_valor_int + variavel_valor_float

#Imprima todas as variáveis na ordem de criação e imprima também seus tipos.
print (f"{variavel_texto}... já o seu tipo é: {type(variavel_texto)}")
print (f"O valor da segunda variável é: {variavel_valor_int}, já o seu tipo é: {type(variavel_valor_int)}")
print (f"O valor da terceira variável é: {variavel_valor_float}, já o seu tipo é: {type(variavel_valor_float)}")
print (f"O valor da quarta variável é: {variavel_soma}, já o seu tipo é: {type(variavel_soma)}")