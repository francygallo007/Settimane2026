"""
- Contare il numero di lettere maiuscole in una stringa
"""

s = input("Parola: ")
maiuscole = 0

for i in s:
    if i.isupper():
        maiuscole += 1
print(maiuscole)
