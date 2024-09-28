# Vamos empreender! Cada grupo deve idealizar uma empresa e criar o software para gerenciar os interesses dessa empresa. Libere a sua imaginação :)

# - ESPECIFICAÇÕES - 
# Antes das especificações, primeiro quero te apresentar um conceito comum em sistemas de gerência de dados: o CRUD! Esse conceito é definido pelas seguintes funcionalidades: 
# Create: criar ou adicionar novas entradas 
# Read: ler, recuperar ou ver entradas existentes (ex: listar todos) 
# Update: Atualizar ou editar entradas existentes 
# Delete: Remover entradas existentes
# Vamos ao que interessa. Para garantir o sucesso da sua empresa, você precisa gerenciar dois tipos de informação.

# - Usuários -
# Controle de acesso (login) com pelo menos dois níveis de permissão de usuário (ex: gerente, funcionário, estagiário, cliente, etc.)
# Pelo menos uma categoria de usuário deve ter todas as permissões
# Para as categorias de usuário com permissão limitada, seus menus devem conter apenas operações permitidas para ele
# O registro de usuários deve ser feito em arquivo (organize como preferir, em um .csv, .txt, ou até binário)
# Proponha uma estrutura de dados para carregar de maneira organizada as informações de usuário
# CRUD de usuários com pelo menos uma funcionalidade para cada letra da sigla

# - Produtos ou Serviços -
# O registro dos produtos e/ou serviços da sua empresa, bem como os seus atributos (preço, quantidade, etc.), devem ser armazenados em arquivo;
# Quando lidos do arquivo, seus registros devem ser salvos em uma estrutura de dados proposta por você, podendo haver mais de uma estrutura de acordo com a necessidade;
# CRUD de registros de produtos e/ou serviços com pelo menos uma funcionalidade para cada letra da sigla, incluindo obrigatoriamente as seguintes funcionalidades:
#           Funcionalidade para buscar um registro específico (seja por nome, por código, etc.);
#           Funcionalidade para imprimir os registros ordenados por nome;
#           Funcionalidade para imprimir os registros ordenados por preço;
# - CONCEITOS - 
# Lembre-se do que aprendemos em sala. Seu código deve conter obrigatoriamente os seguintes conceitos:
# Estruturas condicionais
# Estruturas de repetição
# Funções
# Strings
# Estruturas de dados (lista, set, tupla, dicionário)
# Gerência de arquivos
# - ENTREGAS - 
# Você deve criar uma pasta no seu repositório da disciplina no GitHub com o nome Trabalho_Prático. A pasta deve conter:
# O script principal com o código (ainda não aprendemos a dividir nossas soluções em múltiplos arquivos, então toda a codificação pode se concentrar em um único script python)
# Pelo menos dois arquivos com os registros de usuários e produtos/serviços. O sistema já deve ter usuários e produtos/serviços cadastrados para que a equipe de avaliação possa testar o seu sistema.
# Um documento descritivo do seu trabalho. Deve constar nele:
#           Introdução: qual empresa você está modelando, quais tipos de usuário vão usufruir do sistema e quais produtos e serviços a empresa oferece;
#           Implementação: Para cada elemento da sua solução (usuário e produto/serviço) você deve: (1) descrever a estrutura de dados escolhida para carregar as informações, (2) como o arquivo de registro está estruturado e (3) a lista de funcionalidades daquele elemento (associe cada funcionalidade a uma letra da sigla CRUD).
#           Conclusão: Aproveite esse espaço para descrever coisas como dificuldades encontradas, escolhas bem sucedidas, o que faltou fazer, o que faria diferente, etc.
# - CRITÉRIOS DE AVALIAÇÃO - 
# Implementação das funcionalidades solicitadas;
# Funcionamento apropriado das funcionalidades;
# Organização do código (principalmente indentação, nomes de variáveis e comentários);
#           Todas as funções devem estar comentadas com uma breve descrição de seu funcionamento, entradas e saídas;
# Clareza e organização do documento descritivo.



## Bibliotecas utilizadas
import csv

# Carregando dados
def carregar_dados(arquivo):
    with open(arquivo, mode='r', newline='', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        return [linha for linha in leitor]

# salvando dados nos arquivos
def salvar_dados(arquivo, dados, campos):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

# Carregando dados dos usuarios e cursos
usuarios = carregar_dados('usuarios.csv')
cursos = carregar_dados('cursos.csv')

## Realização de login
def login():
    usuario = input("Usuário: ")  # Entrada dos usuarios
    senha = input("Senha: ")      #
    for u in usuarios:
        if u['usuario'] == usuario and u['senha'] == senha:
            return u # Retorna usuario apos leitura
    return None

## Função para listar todos os usuários
def listar_usuarios():
    for u in usuarios:
        print(f"Nome: {u['nome']}, Tipo: {u['tipo']}")

# Função para adicionar um novo usuário
def adicionar_usuario():
    nome = input("Nome: ")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    tipo = input("Tipo (Admin/Instrutor/Aluno): ")
    novo_usuario = {'nome': nome, 'usuario': usuario, 'senha': senha, 'tipo': tipo}
    usuarios.append(novo_usuario)
    salvar_dados('usuarios.csv', usuarios, ['nome', 'usuario', 'senha', 'tipo'])

# Função para editar um usuário existente
def editar_usuario():
    usuario = input("Digite o usuário que deseja editar: ")
    for u in usuarios:
        if u['usuario'] == usuario:
            u['nome'] = input(f"Nome ({u['nome']}): ") or u['nome']
            u['senha'] = input(f"Senha: ")
            u['tipo'] = input(f"Tipo ({u['tipo']}): ") or u['tipo']
            salvar_dados('usuarios.csv', usuarios, ['nome', 'usuario', 'senha', 'tipo'])
            return
    print("Usuário não encontrado.")

# Função para deletar um usuário
def deletar_usuario():
    usuario = input("Digite o usuário que deseja deletar: ")
    for u in usuarios:
        if u['usuario'] == usuario:
            usuarios.remove(u)
            salvar_dados('usuarios.csv', usuarios, ['nome', 'usuario', 'senha', 'tipo'])
            return
    print("Usuário não encontrado.")

# Função para listar todos os cursos
def listar_cursos():
    for c in cursos:
        print(f"Nome: {c['nome']}, Instrutor: {c['instrutor']}, Preço: {c['preco']}")

# Função para adicionar um novo curso
def adicionar_curso():
    nome = input("Nome do curso: ")
    instrutor = input("Instrutor: ")
    preco = float(input("Preço: "))
    vagas = int(input("Vagas: "))
    novo_curso = {'nome': nome, 'instrutor': instrutor, 'preco': preco, 'vagas': vagas, 'inscritos': 0}
    cursos.append(novo_curso)
    salvar_dados('cursos.csv', cursos, ['nome', 'instrutor', 'preco', 'vagas', 'inscritos'])

# Função para editar um curso existente
def editar_curso():
    nome_curso = input("Digite o nome do curso que deseja editar: ")
    for c in cursos:
        if c['nome'] == nome_curso:
            c['preco'] = float(input(f"Preço ({c['preco']}): ") or c['preco'])
            c['vagas'] = int(input(f"Vagas ({c['vagas']}): ") or c['vagas'])
            salvar_dados('cursos.csv', cursos, ['nome', 'instrutor', 'preco', 'vagas', 'inscritos'])
            return
    print("Curso não encontrado.")

# Função para deletar um curso
def deletar_curso():
    nome_curso = input("Digite o nome do curso que deseja deletar: ")
    for c in cursos:
        if c['nome'] == nome_curso:
            cursos.remove(c)
            salvar_dados('cursos.csv', cursos, ['nome', 'instrutor', 'preco', 'vagas', 'inscritos'])
            return
    print("Curso não encontrado.")

# Função principal de gerenciamento
def gerenciar():
    print("Bem-vindo ao sistema EduTech!")
    user = login()
    if user:
        print(f"Bem-vindo {user['nome']} ({user['tipo']})")
        if user['tipo'] == 'Admin':
            while True:
                print("\n1. Listar Usuários")
                print("2. Adicionar Usuário")
                print("3. Editar Usuário")
                print("4. Deletar Usuário")
                print("5. Listar Cursos")
                print("6. Adicionar Curso")
                print("7. Editar Curso")
                print("8. Deletar Curso")
                print("9. Sair")
                
                opcao = input("Escolha uma opção: ")

                if opcao == '1':
                    listar_usuarios()
                elif opcao == '2':
                    adicionar_usuario()
                elif opcao == '3':
                    editar_usuario()
                elif opcao == '4':
                    deletar_usuario()
                elif opcao == '5':
                    listar_cursos()
                elif opcao == '6':
                    adicionar_curso()
                elif opcao == '7':
                    editar_curso()
                elif opcao == '8':
                    deletar_curso()
                elif opcao == '9':
                    break
                else:
                    print("Opção inválida!")
    else:
        print("Login ou senha incorretos!")

# Executar o sistema de gerenciamento
gerenciar()
