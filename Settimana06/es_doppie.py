parole = [ "cane", "topo", "pesce nero", "canarino" ]


trovata = False # si ricorda se ho visto almeno una parola con le doppie
for parola in parole:

    # scoprire se 'parola' contiene doppie
    doppie = False
    for i in range(1, len(parola)):
        if parola[i]==parola[i-1]:
            doppie = True

    if doppie == True:  # parola contiene delle doppie
        trovata = True

if trovata:
    print("C'è almeno una parola con le doppie")
else:
    print("Tutte le parole sono prive di doppie")


'''
# caso singolo: ho una parola e devo scoprire se conteine delle
# doppie

parola = "gato"
doppie = False
for i in range(1, len(parola)):
    if parola[i]==parola[i-1]:
        doppie = True

print(doppie)
'''