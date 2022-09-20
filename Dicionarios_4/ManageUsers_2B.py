from Funçoes_2 import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(dicionario=usuarios)

    if opcao == "E":
        excluir(dicionario=usuarios)

    if opcao == "P":
        pesquisar(dicionario=usuarios)

    if opcao == "L":
        listar(dicionario=usuarios)
    opcao = perguntar()
