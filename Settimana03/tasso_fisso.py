''' 
vogliamo calcolare il bilancio del conto 
che parte da un valore saldo_iniziale
considerato un tasso fisso di interesse composito annuo del 5%
e fermarci all'anno in cui il totale supera 20000 euro
e restituire in uotput l'anno di stop e il saldo finale
e la differenza tra saldo finale e iniziale
'''

saldo_iniziale = 1000
saldo = saldo_iniziale
TASSO = 5
anno = 0 


while anno < 10: #saldo <= 2000:
    saldo += saldo * TASSO/100
    anno += 1 
     
differenza = saldo - saldo_iniziale
print("Anno: " + str(anno) + "\nSaldo: "+ str(saldo) + "\nDifferenza: "+ str(differenza))


i = 0
totale = 0
while totale < 10:
    i += 1
    tatle += 1
    print(i, totale)