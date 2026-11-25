
colori_preferiti = {
    "Romeo" : "verde",
    "Adam" : "viola",
    "Juliet" : "blu",
    "Eve" : "blu"
}

dizionario = {}
altro_dizionario = dict()

dizionario["Adam"] = "viola"
dizionario["Eve"] = ["verde", "viola"]
print(colori_preferiti)
print(dizionario)

# Se ci sono 2 chiavi uguali viene tenuto l'ultimo scritto.
# Possiamo accedere ai valori dei dizionari con le chiavi, NON
# attraverso gli indici.

numeri = {
    1 : "primo",
    2 : "secondo",
    3 : "terzo"
}
print(numeri[1]) # 1 non è l'indice ma la chiave

if 0 in numeri.keys():
    print(numeri[0])
else:
    print("Chiave non presente")

print(numeri.get(0, "chiave mancante"))

for elemento in numeri.items(): # dict.items() per stampare tutte le tuple
    print(elemento)

for chiave, valore in numeri.items(): # dict.items() per stampare tutte le tuple
    print(valore)

