import json

dicionario = {
    "CHAVES": ["CHAVES DO 8", "14/04/2017", "RECEP_01"],
    "QUICO": ["QUICO FLORES", "24/04/2017", "RAIOX_01"],
    "FLORINDA": ["DONA FLORINDA", "18/04/2017", "RECEP_03"]
}

with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)
