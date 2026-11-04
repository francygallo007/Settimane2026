from random import randint

from pprint import pprint

N = int(input("Caselle lato della griglia? "))
M = int(input("Numero di fiori nella nel campo? "))

campo = []

for i in range(N):
    nuova = []
    for col in range(N):
        nuova.append(False)
    campo.append(nuova)

pprint(campo)

for fiore in range(M):
    riga_fiore = randint(0, N-1)
    col_fiore = randint(0, N-1)

    while campo[riga_fiore][col_fiore] == True:
        riga_fiore = randint(0, N-1)
        col_fiore = randint(0, N-1)
    campo[riga_fiore][col_fiore] = True

for riga in range(N):
    for col in range(N):
        if campo[riga][col]:
            print("🌸", end ="")
        else:
            print("🟢", end="")
    print()

# Calcola gli adiacenti a ciascuna casella

vicini = []

for riga in range(N):
    nuova_riga = []
    for col in range(N):
        n_vicini = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if campo[riga+i][col+j]:
                    if (
                        (i != 0 or j != 0) and 
                        riga+i < N and
                        riga+i >= 0 and
                        col+j < N and
                        col+j >= 0
                    ):
                        n_vicini += 1
                    
        nuova_riga.append(n_vicini)
    vicini.append(nuova_riga)

pprint(vicini)