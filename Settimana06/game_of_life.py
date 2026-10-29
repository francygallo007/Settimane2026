N_RIGHE = 10
N_COLONNE = 10

griglia = []

for riga in range(N_RIGHE):
    griglia.append([0]*N_COLONNE)

for i in range(4, 8):
    griglia[3][i] = 1

for riga in range(N_RIGHE):
    for colonna in range(N_COLONNE):
        print(griglia[riga][colonna], end=" ")
    print()

comando = input()

while comando == "":
    nuova_griglia = []
    for riga in range(N_RIGHE):
        nuova_griglia.append([0]*N_COLONNE)

    for i in range(N_RIGHE):
        for j in range(N_COLONNE):
            conta_vivi = 0
            for n_i in range(-1, 2):
                for n_j in range(-1, 2):
                    if i+n_i < N_RIGHE and j+n_j < N_COLONNE:
                        if griglia[i+n_i][j+n_j] == 1:
                            if not(n_i == 0 and n_j == 0):
                                conta_vivi += 1
            #print(conta_vivi)
            # se è vivo e ha 2 o 3 vicini allora resta vivo
            # altrimenti si spegne
            if griglia[i][j] == 1:
                if conta_vivi == 2 or conta_vivi == 3:
                    griglia[i][j] = 1
                else:
                    griglia[i][j] == 0
            # se è spento e ha esttamente 3 vicini allora prende vita
            elif griglia[i][j] == 0:
                if conta_vivi == 3:
                    griglia[i][j] = 1
                else:
                    griglia[i][j] = 0

    for riga in range(N_RIGHE):
        for colonna in range(N_COLONNE):
            print(nuova_griglia[riga][colonna], end=" ")
        print()
    griglia = nuova_griglia
    comando = input()

