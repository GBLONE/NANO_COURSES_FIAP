import socket

resp = "S"

while(resp == "S"):
    url = input('Digite uma URL: ')
    ip = socket.gethostbyname(url)
    print("O IP refenrete a URL informada é:", ip)
    resp = input("Digite <s> para continuar: ").upper()

# Programa introdutório só para saber o que o socket faz.
