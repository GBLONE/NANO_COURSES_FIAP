equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite \"S\" para continuar ou qualquer tecla para finalizar: ").upper()

for indice in range(0, len(equipamentos)):
  print("\nEquipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])

# (Multiplas Listas) São listas que paralelamente feitas para o mesmo proposito, produto, dados, etc.
# (Indices) É um número identificador dos elementos de cada lista.
