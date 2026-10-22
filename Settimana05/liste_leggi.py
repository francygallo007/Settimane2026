# Inserisci da tastiera 4 numeri interi e memorizzali
# in una lista

numeri = []
for i in range(4):
    n = int(input("Numero "))
    numeri.append(n)

    # numeri[i] = n  # no perché la posizione i non esiste ancora

    print(numeri)

# Calcola una lista che contenga il doppio dei valiro
# appena letti

doppi = []
for v in numeri:
    doppi.append( v*2 )

print(numeri)
print(doppi)
