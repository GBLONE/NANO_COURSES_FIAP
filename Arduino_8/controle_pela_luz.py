import serial
from serial.tools import list_ports

conexao = ""
for port in list_ports.comports():
    print(f'Dispositivo: {port.description} - Porta {port.device}')
    if ("ARDUINO" in port.description.upper()):
        try:
            conexao = serial.Serial(port, 115200)
            print(f"Conexão realizada com {conexao.portstr}")
        except:
            pass

if conexao != "":
    print("Iniciando...")
    while True:
        print("Recebendo Dados...")
        resposta = conexao.readline()
        valor = float(resposta.decode())
        print(valor)
        if (valor < 700):
            conexao.write(b'1')
        else:
            conexao.write(b'0')
    conexao.close()
    print("Conexão encerrada.")
else:
    print('Sem portas disponíveis.')