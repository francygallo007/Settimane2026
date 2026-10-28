a = [ 3, 5, 12, -5, 8, 44, -12, 0, 1 ]

print(len(a))

print(a)
for i in range(len(a)):
    print(a[i])

for v in a:
    print("*", v)

# incrementa tutti i numeri della lista 'a' di una unità

for i in range(len(a)): # in questo caso si va a modificare il valore nella lista
    a[i] = a[i] + 1
print("dopo", a)

for v in a: # invece qua viene solo modificato il valore della variabile v
    v = v + 1
print("dopo ancora", a)

for i, v in enumerate(a): # sia indice che valore nella lista
    print("alla posizione", i, "abbiamo il valore", v)


