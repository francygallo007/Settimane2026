righe = 5
colonne = 8
tabella = []

for riga in range(righe):
    tabella.append([0] * colonne)

for riga in tabella:
    print(riga)

lista_paesi = ["Canada", "Italia", "Russia", "USA", "Serbia"]

lista_ordinata = sorted(lista_paesi)
print(lista_ordinata)

# shallow copy

nuova_tabella = list(tabella)
nuova_tabella[2][2] = 1

for i in tabella:
    print(i)

print()
for i in nuova_tabella:
    print(i)