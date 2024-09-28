livros = [
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1216},
    {"Título": "Clean Code", "Autor": "Robert C. Martin", "Ano de publicação": 2012, "Número de páginas": 425},
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 100},
    {"Título": "Harry Potter e o Prisioneiro de Azkaban", "Autor": "J.K. Rowling", "Ano de publicação": 1999, "Número de páginas": 288}
]




with open("meus_livros.csv", "w") as arquivo:
    # Escrevendo os títulos das colunas
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrevendo as informações de cada livro
    for livro in livros:
        linha = f"{livro['Título']},{livro['Autor']},{livro['Ano de publicação']},{livro['Número de páginas']}\n"
        arquivo.write(linha)

print("Arquivo 'meus_livros.csv' criado com sucesso!")