# Inserisci da tastierta 4 numeri interi e salvali in una lista

numeri = []

for i in range(4):
    n = int(input("Numero "))
    numeri.append(n) # elemento che verrà aggiunto in fondo alla lista
    # numeri[i] = n # no perchè la posizionei non esiste
    print(numeri)

# Calcola una lista che contenga il doppio dei valori appena letti

doppi = []

for  v in numeri:
    doppi.append(v*2)

    print(numeri)
    print(doppi)

# lista.insert(1, "") inserisce l'elemento in una specifica posizione e gli elementi si sposta a destra
# lista.index() fornisce la poosizione di un elemento, se non c'è ValueError
# lista.pop(posizione) eliminare l'elemento nella posizione (inserisco la posizione)
# lista.remove(element) inserisci il valore dell'elemento che voglio cancellare