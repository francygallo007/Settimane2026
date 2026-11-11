infile = open("intervistaLinus.txt", "r", encoding="utf-8")

tot = 0

for riga in infile:
    parole = riga.split()
    tot += len(parole)

infile.close()


print(f"Le parole totali sono {tot}")

infile = open("intervistaLinus.txt", "r", encoding="utf-8")
testo = infile.read()
infile.close()

tot_domande = 0
pos = 0

while pos != -1:
    pos = testo.find("?")
    tot_domande += 1
    testo = testo[pos+1:]

print(f"Il testo ha {str(tot_domande)} domande")


