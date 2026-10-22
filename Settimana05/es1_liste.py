# Leggi una lista di numeri interi positivi da tastiera,
# terminando l'inserimento quanto viene
# inserito il valore -1

# calcola e stampa una lista ottenuta
# cancellando dalla lista di partenza tutti
# i numeri maggiori di 5

numeri = []

dato = int(input("Dato: "))
while dato != -1:
    numeri.append(dato)
    dato = int(input("Dato: "))

print(numeri)

i = 0
while i<len(numeri):
    if numeri[i] > 5:
        print("DEVO CANCELLARE", numeri[i], "in posizione", i)
        numeri.pop(i)
    else:
        i = i + 1

i = len(numeri)-1
while i>=0:
    if numeri[i]>5:
        numeri.pop(i)
    i = i - 1

for i in range(len(numeri)-1, -1, -1):
    if numeri[i]>5:
        numeri.pop(i)

altri = []
for v in numeri:
    if v<=5:
        altri.append(v)

print(numeri)