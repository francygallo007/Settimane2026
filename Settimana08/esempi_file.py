outfile = open("output.txt", "w") # w: write
print(outfile)
outfile.write("Hello, world!\n")
outfile.close() 
# bisogna sempre chiudere perchè altrimenti non lo si può 
# modificare in futuro perchè lo considera aperto

infile = open("Diario.txt", "r", encoding='utf-8')
content=infile.read()
print(content)
infile.close()

# programma che legga il file allenamento e mi comunichi le mie statistiche
# della settimana, in particolare il totale di ore di allenamento e la
# velocità media ponderata

durata = []
velocità = []
infile = open("allenamenti.txt", "r", encoding="utf-8")
for riga in infile:
    riga_s = riga.split()
    durata.append(float(riga_s[1]))
    velocità.append(float(riga_s[2]))
infile.close()

print(durata)
print(velocità)

print("In totale questa settimana ti sei allenato", str(sum(durata)), " minuti")

numeratore = 0

for i in range(len(durata)):
    numeratore += durata[i]*velocità[i]

media_p = numeratore/sum(durata)

print(media_p)


