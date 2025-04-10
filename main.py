import json

# abrir e ler o arquivo followers
with open('followers_1.json', 'r') as arquivo:
    dadosFollowers = json.load(arquivo)

# abrir e ler o arquivo following
with open('following.json', 'r') as arquivo:
    dadosFollowing = json.load(arquivo)

# lista para armazenar os seguidores (followers)
listaSeguidores = []
listaSeguindo = []

# laço de repetição que extrai a relação de seguidores e adiciona em uma lista
for i in dadosFollowers:
    for stringData in i['string_list_data']:
        listaSeguidores.append(stringData['value'])

# laço de repetição que extrai a relação de seguintes e adiciona em uma lista
for i in dadosFollowing['relationships_following']:
    for stringData in i['string_list_data']:
        listaSeguindo.append(stringData['value'])

# calcular diferença entre listas e descobrir não-seguidores
naoSeguidores = list(set(listaSeguindo) - set(listaSeguidores))

# Exportar a lista naoSeguidores para um arquivo txt
with open('nao_seguidores.txt', 'w') as arquivo:
    for usuario in naoSeguidores:
        arquivo.write(f"{usuario}\n")

# Exibir a lista de não-seguidores
print(naoSeguidores)