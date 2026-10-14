"""
- Sostituire, in una stringa tutte le cifre numeriche 
con il numero successivo (es. ogni 3 diventa 4, il 9 diventa 0)
"""

s = input("stringa: ")

nuova = ""

for ch in s:
    if ch.isdigit():
        if ch == "9":
            nch = "0"
        else:
            nch = str(int(ch)+1)
    else:
        nch = ch
    nuova += nch
print(nuova)

print()

nuova = ""
for ch in s:
    if ch.isdigit():
        if ch == "9":
            nuova +="0"
        else:
            nuova += str(int(ch)+1)
    else:
        nuova+=ch
print(nuova)