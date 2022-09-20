import serial
from serial.tools import list_ports

# listas as portas arduino.
for port in list_ports.comports():
    print(f"Dispositivo: {port.description} - porta: {port.device}")

conexao = serial.Serial('COM1', 115200)

acao = input("Digite:\n<L> para Ligar\n<D> para Desligar: ").upper()
while acao == "L" or acao == "D":
    if acao == "L":
        conexao.write(b'1')
    else:
        conexao.write(b'0')
    acao = input("Digite:\n<L para Ligar\n<D> para Desligar: ").upper()
conexao.close()
print("Conexão Encerrada.")
