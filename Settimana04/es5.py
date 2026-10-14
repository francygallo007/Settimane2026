"""
Acquisire 10 numeri interi.
Dopo averli acquisiti tutti, 
dire se erano TUTTI PARI.
"""
tutti_pari = True # Flag

for i in range(10):
    x = int(input("Numero: "))
    if x%2 != 0:
        tutti_pari = False
if tutti_pari:
    print("tutti_pari")
else:
    print("Qualche dispari")


