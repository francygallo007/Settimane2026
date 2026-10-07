totale = 0
numero = float(input("Inserisci un numero: "))
contatore = 0 

while numero >= 0:
    contatore = contatore + 1
    totale = totale + numero
    numero = float(input("Dammi un numero: "))   
print(totale)


finito = False
totale = 0
numero = float(input("Inserisci un numero: "))
contatore = 0
if numero < 0:
    finito = True 
while not finito:

    contatore = contatore + 1
    totale = totale + numero
    numero = float(input("Dammi un numero: "))
    if numero < 0:
        finito = True
    
