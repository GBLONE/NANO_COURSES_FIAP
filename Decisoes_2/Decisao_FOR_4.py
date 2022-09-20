tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)

for valor in range(1, 11, 1): # range(inicio, fim, encremento)
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))

# ("for") A caracteristica mais forte do FOR é; é que você pode definir uma faixa onde ele vai analisar e com isso você
# consegue determinar : O inicio, o Final e o encremento que você quer dar no seu laço.
