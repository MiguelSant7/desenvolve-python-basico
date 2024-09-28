import csv

# Inicializa um dicionário para armazenar a música mais popular de cada ano
musicas_por_ano = {}

# Abre o arquivo CSV para leitura
with open("spotify-2023.csv", "r", encoding='latin-1') as arquivo:
    leitor_csv = csv.reader(arquivo)

    # Ignora o cabeçalho
    next(leitor_csv)

    for linha in leitor_csv:
        # Verifica se a linha tem o número correto de colunas
        if len(linha) < 10:
            continue

        track_name = linha[0].strip('"')  # Nome da música
        artist_name = linha[1].strip('"')  # Nome do artista
        released_year = int(linha[3])  # Ano de lançamento
        streams = int(linha[8])  # Número de streams

        # Ignora músicas com mais de um artista
        artist_count = int(linha[2])
        if artist_count > 1:
            continue

        # Verifica se o ano está dentro do intervalo desejado
        if 2012 <= released_year <= 2022:
            # Se já existe uma música para o ano, verifica se a nova tem mais streams
            if released_year in musicas_por_ano:
                if streams > musicas_por_ano[released_year][3]:  # Comparando streams
                    musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]
            else:
                # Se não existe, adiciona a nova música
                musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

# Converte o dicionário para uma lista
resultado = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano.keys())]

# Imprime a lista resultante
print(resultado)
