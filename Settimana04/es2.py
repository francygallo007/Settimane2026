"""
- Inserire 10 numeri interi. 
Calcolare il valore dato dalla somma di tutti i numeri pari,
meno la somma di tutti i numeri dispari
"""

pari = 0
dispari = 0

for i in range(10):
    x = int(input("Numero: "))
    if x%2 == 0:
        pari = pari + x
    else:
        dispari = dispari + x  
print(pari-dispari)


somma = 0
i = 0
while i<10:
    x = int(input("Numero: "))
    if x%2 == 0:
        somma += x
    else:
        somma -= x
    i += 1
print(somma)