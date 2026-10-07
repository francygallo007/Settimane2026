nome = "ciao"

i = 0
while i < len(nome):
    lettera = nome[i]
    print(lettera)
    i += 1

print()

for lettera in nome:
    print(lettera)

print()
 
for i in range(len(nome)):
    print(i)

for i, lettera in enumerate(nome):
    print(i, lettera)

