"""
- Dire se una stringa contiene 
almeno una lettera maiuscola
"""
s = input("Inserisci testo: ")
maiuscola = False
for ch in s:
    if ch.isupper():
        maiuscola = True

if maiuscola:
    print("esiste una maiuscola")
else:
    print("nessuna maiuscola")

#Dire se una stringa contiene al suo interno 
#due segni di punteggiatura consecutivi

spazio = False
for i in range(len(s)):
    if s[i].isspace() and s[i-1].isspace:
        spazio = True
if spazio:
    print("Esistono due spazi consecutivi")
else:
    print("Non ci sono 2 spazi consecutivi")