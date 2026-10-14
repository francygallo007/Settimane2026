"""
- Cancellare tutte le lettere maiuscole da una stringa
"""
s = input("stringa: ")
nuova =  ""

for i in s:
    if not i.isupper():
        nuova += i
print(nuova)

  