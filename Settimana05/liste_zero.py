a = [ 3, 5, 12, -5, 8, 44, -12, 0, 1 ]

print(len(a))

print(a)

for i in range(len(a)):
    print(a[i])

for v in a:
    print("*", v)

for i, v in enumerate(a):
    print("alla posizione", i, "abbiamo il valore", v)

for i in range(len(a)):
    v = a[i]
    print("alla posizione", i, "abbiamo il valore", v)


# incrementa tutti i numeri della lista 'a' di una unità
print("PRIMA", a)
for i in range(len(a)):
    a[i] = a[i]+1
print("DOPO", a)
for v in a:
    v = v + 1
print("DOPO ANCORA", a)



