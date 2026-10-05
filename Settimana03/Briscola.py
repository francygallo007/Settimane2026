# Identifica costanti 
SEMI = "CQFP"
VALORI = "24567JQK3A"

# Acquisisci i dati
Seme = input("Inserisci il seme di briscola: ").upper()
Carta1 = input("Inserisci la prima carta giocata: ").upper()
Carta2 = input("Inserisci la seconda carta giocata: ").upper()

seme1 = Carta1[1]
seme2 = Carta2[1]
valore1 = Carta1[0]
valore2 = Carta2[0]

# valore = 2 4 5 6 7 J Q K 3 A
# ordine = 1 2 3 4 56 7 8 9 10
ordine1 = VALORI.index(valore1) + 1
ordine2 = VALORI.index(valore2) + 1

# Verifica la correttezza dei dati (facciamo dopo)
"""
Seme == 1
Seme in SEMI

Carta1 == 2
seme1 in SEMI
valore1 in valori

Carta2 == 2 
seme2 in SEMI
valore2 in valori
"""
# Determina il vincitore

"""
if carta1 ha seme di briscola, ma carta2 non ha seme di briscola:
    vince carta1
if carta2 ha seme di briscola, ma carta1 non ha seme di briscola:
    vince carta2
"""
if seme1 == Seme and seme2 != Seme:
    print("vince", Carta1)
elif seme2 == Seme and seme1 != Seme:
    print("vince", Carta2)
elif seme1 != seme2 :
    print("vince", Carta1)
elif ordine1 > ordine2:
    print("vince", Carta1)
else:
    print("vince", Carta2)

# Stampa il risultato
