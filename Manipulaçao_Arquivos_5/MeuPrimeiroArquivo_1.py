with open("primeiro_arquivo.txt", "r") as primeiro_arquivo:
    for linha in primeiro_arquivo.readlines():
        print(linha)

# Modos para abrir os arquivos em open():
# r = que significa leitura, Read.
# w = de Write que é escrita.
# a = serve para os dois, tanto para leitura do arquivo
# quanto para escrita, ele significa append.
# x = que significa exclusivo, você vai abrir ele e ninguem mais
# vai poder manipular esse arquivo enquanto você não fechar ele.
# *Obs: Também teremos a opção de combinar esses modos de abertura
# do arquivo. Por exemplo, podemos colocar R+W, ou então, W+X,
# ou simplismente, WX, ele vai fazer essa informação.
