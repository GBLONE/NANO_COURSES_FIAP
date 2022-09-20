# Decisão encadeadas
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

doença_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper()
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
elif doença_infectocontagiosa == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")

# ("if") Se for isso, faça isso.
# ("else") Se for aquilo outro faça o outro.
# ("elif") Serve para encadear as decisões, uso de "if" excessivo pode prejudicar o código e por isso fazendo ele da +
# + forma que está no código para simplificar e deixar a sua lógica mais clara.
