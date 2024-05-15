###Questao2 - FatiandO domínios

#Entrada de Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

#Processamento (Criando a lista de domínios)
dominios = [url[4:-4] for url in urls]

#Saída
print("Domínios:", dominios)
