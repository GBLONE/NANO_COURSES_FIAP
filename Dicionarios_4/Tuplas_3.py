usuarios = {}
emails = ["xpto@xyz.com", "xkcd@phd.com"]

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome"), input("Digite o nível")]

for chave, dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ", chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])

# (TUPLAS) ela é uma estrutura de dados volatil, assim como os dicionarios e as listas. Única diferença é que ela é
# imutável, ou seja; toda vez que voce gera um valor voce não consegue manipular o valor que tem dentro dela. Voce só
# consegue consumir esse valor, só consultá-lo.
# Operadores e suas diferenças:
#       Chaves {} == Dicionarios_4
#       Colchetes [] == Listas
#       Parênteses () == Tuplas
