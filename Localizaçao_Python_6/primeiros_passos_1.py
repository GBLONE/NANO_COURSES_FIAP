from pygeocoder import Geocoder

endereco = "1222, Lins de Vasconcelos, Sao Paulo, SP"
print(Geocoder('código de crendencial API Google Cloud'.geocode(endereco).coordinates))

#Esse sistema ("""GEOCODER""") precisa que acesse e ative sua conta no Google Cloud:
#link: https://console.cloud.google.com/welcome?project=pygeocoder-360217&supportedpurview=project
