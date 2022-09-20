import platform
from datetime import datetime
import getpass

print('Nome maquina:.............', platform.node())
print('Arquitetura:..............', platform.architecture())
print('Sistema Operacional:......', platform.system())
print('Versão do SO:.............', platform.release())
print('Processador:..............', platform.processor())
print('Versão do Python:.........', platform.python_version())
print('Horário da maquina:.......', datetime.now())

usuario = (getpass.getuser())
senha = (getpass.getpass('Digite sua senha:...'))

if usuario == 'gbl_c' and senha == 'Hello':
    print(f'Bem-vindo {usuario}')
else:
    print('Você não tem acesso:')
