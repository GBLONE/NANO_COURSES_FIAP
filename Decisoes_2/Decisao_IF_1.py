nome = str(input('Digite seu Nome: '))
idade = int(input('Sua Idade: '))

if idade >= 65:
    print(f'O paciente {nome} com {idade} anos, POSSUI atendimento prioritário!')
else:
    print(f'O paciente {nome} com {idade} anos,  NÃO possui atendimento prioritário!')
print("_____________FIM______________")

# ("if") Se for isso, faça isso.
# ("else") Se for aquilo outro faça o outro.
# ("idade >= 65") a idade tem que ser Maior ou igual a 65, para ter atendimento prioritário.
