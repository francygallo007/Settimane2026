"""
INPUT
    Seme di briscola, prima e seconda carta giocata
OUTPUT
    Vincitore tra le due carte
CONDIZIONI


"""
#INIZIO PROGRAMMA
Seme = input("Inserisci il seme di briscola: ")
Carta1 = input("Inserisci la prima carta giocata: ")
Carta2 = input("Inserisci la seconda carta giocata: ")

if Carta1[1] == Seme and Carta1[1] != Carta2[1]:
    print("Vince", Carta1)
else:
    print("Vince", Carta2)
