import random

numeri = []

for i in range(10):
    n = random.randint(-10, 10)
    numeri.append(n)

print(numeri)

# -----------------------

duplicati = False
for v in numeri:
    # togli il valore v dalla lista
    numeri_copia = list(numeri)
    numeri_copia.remove(v)
    if v in numeri_copia:
        duplicati = True


duplicati = False
for i in range(len(numeri)):
    if numeri[i] in numeri[i+1:] :
        duplicati = True

duplicati = False
for v in numeri:
    if numeri.count(v) >= 2:
        duplicati = True

duplicati = False
for i in range(len(numeri)):

    # cerca se v è presente **altrove**
    presente = False
    for j in range(len(numeri)):
        if numeri[i] == numeri[j] and i != j:
            presente == True

    if presente: # numeri[i] è presente altrove?
        duplicati = True
