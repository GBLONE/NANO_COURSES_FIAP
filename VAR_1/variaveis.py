nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a quantidade de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionários.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [empresa] é: ", type(empresa))
print("O tipo de dado da variável [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variável [mediaMensalidade] é: ", type(mediaMensalidade))

# Variáveis são espaços em memória que são guardados os dados fornecidos pelo usuario. Cada variável é identificada
# por um identificador proprio que tem que começar necessariamente por uma letra nunca por um número, sempre minuscula
# (boa prática). Cuidado com os caracteres especiais, unico que se utiliza é o Underline ("_"). Strings são letras ou
# números que não se faz conta (Ex: CPF, CEP, Idade, etc), Inteiros são números sem vírgulas usado para quantidades
# inteiras como de uma empresa ou número de usuários de uma rede, e que você pode somar etc. Float são números decimais
# (números flutuantes, números com virgulas ou pontos) que você pode calcular e com eles também.