# Acquisisci i dati
Seme = input("Inserisci il seme di briscola: ")
Carta1 = input("Inserisci la prima carta giocata: ")
Carta2 = input("Inserisci la seconda carta giocata: ")

# Verifica la correttezza dei dati (facciamo dopo)

# Determina il vincitore
seme1 = Carta1[1]
seme2 = Carta2[1]
valore1 = Carta1[0]
valore2 = Carta2[0]

# valore = 2 4 5 6 7 J Q K 3 A
# ordine = 1 2 3 4 56 7 8 9 10

valori = "24567JQK3A"
ordine1 = valori.index(valore1) + 1
ordine2 = valori.index(valore2) + 1


"""
if carta1 ha seme di briscola, ma carta2 non ha seme di briscola:
    vince carta1
if carta2 ha seme di briscola, ma carta1 non ha seme di briscola:
    vince carta2

"""
if seme1 == Seme and seme2 != Seme:
    print("vince", Carta1)
else:
    if seme2 == Seme:
        print("vince", Carta2)

    if seme1 != seme2 :
        print("vince", Carta1)
    else:
        #di sicuro seme1 == seme2
        if ordine1 > ordine2:
            print("vince", Carta1)
        else:
            print("vince", Carta2)




# Stampa il risultato
