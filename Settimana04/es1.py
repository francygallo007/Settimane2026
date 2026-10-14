"""
- Inserire un numero intero positivo. 
Se non fosse positivo, ripetere la richiesta.
"""

x = int(input("Numero: "))

while x <= 0:
    x = int(input("Numero: "))
