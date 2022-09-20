def perguntar():
    return input("O que deseja realizar?\n" +
            "<I> - Para Inserir um usuário\n" +
            "<P> - Para Pesquisar um usuário\n" +
            "<E> - Para Excluir um usuário\n" +
            "<L> - Para Listar um usuário: ").upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input('Digite o Nome: ').upper(),
                                                   input('Digite a última data de acesso: '),
                                                   input('Qual a última estação acessada: ').upper()]
    salvar(dicionario)


def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))


def excluir(dicionario):
    delete = [input("Digite o login para excluír: ").upper()]
    while open("bd.txt", "a+"):
        for delete in dicionario:
            delete.remove()
        return print('Deletado...')


def pesquisar(dicionario):
    buscar = [input("Digite o login para pesquisar: ").upper()]
    for buscar in dicionario:
        buscar.find(dicionario)
    return print(f'Sua Busca:{buscar}')


def listar(dicionario):
    busca = [input('Aperte A para listar usuários: ').upper()]
    while busca == "A":
        while listar in busca:
            busca = listar.find(dicionario)
    return print(f'{dicionario}')
