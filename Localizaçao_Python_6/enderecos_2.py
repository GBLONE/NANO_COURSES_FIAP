from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo'
resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco)
print(resultado)

# Para Instalação de uma biblioteca externa se deve baixair no site do python e no Prompt de Comando
# digita "pip install pygeocoder" e pegue o nome do arquivc que você baixou do site.
# Quando instalar a biblioteca, você vai ter ir para o site do Google Cloud, lá você poderá abaixar uma API de maps no
# caso (no Google Cloud tem a versão paga e gratuita, onde a gratuita tem limites de acessos a essa API).
# Quando você conseguir, eles vão dar uma chave para você conseguir acessar a API, essa chave você cola no GeoCoder()
# para fazer a API funcionar no seu código.
# Geocoder acessa a informação na nuvem do Google que foi onde você pega a chave (Google Cloud).
