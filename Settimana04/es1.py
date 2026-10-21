"""
- Inserire un numero intero positivo. 
Se non fosse positivo, ripetere la richiesta.
"""

x = int(input("Numero: "))

while x <= 0:
    print("Dovevi inserire un numero positivo")
    x = int(input("Numero: "))

x = -99
while x <= 0:
    x = int(input("Numero: "))
    if x <= 0:
        print("Dovevi inserire un numero positivo")
