import serial
from serial.tools import list_ports

# lista as portas Arduino_8.
conexao = ""
for port in list_ports.comports():
    print(f'Dispositivo: {port.description} - Porta: {port.device}')
    if("ARDUINO_8" in port.description.upper()):
        try:
            conexao = serial.Serial(port.device, 115200)
            print(f"Conexão realizada com {conexao.portstr}.")
        except:
            pass

if conexao != "":
    while True:
        resposta = conexao.readline()
        print(float(resposta.decode()))
    conexao.close()
