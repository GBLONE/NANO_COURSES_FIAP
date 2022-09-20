inventario = []
resposta = "S"
while resposta == "S":
  inventario.append(input("Equipamento: "))
  inventario.append(float(input("Valor: ")))
  inventario.append(int(input("Número Serial: ")))
  inventario.append(input("Departamento: "))
  resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
  print(elemento)


# (LISTA EM ABERTO(que está nesse código)) se preenche de forma que necessita.
# (Lista estática) Onde já é fornecido a quantidade de elementos que eu preciso.
# (Lista Dinamica) que é aquela que eu peço que os úsuarios vai colocando os elementos nela.
# (APPEND) é uma função para inserir o dado dentro da lista.
# (Upper) é uma função para deixar todos os caracteres em maiusculos.
