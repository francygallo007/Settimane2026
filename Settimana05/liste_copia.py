a = [ 2, 5, 8 ]

b = a  # crea un ALIAS -> a e b sono la stessa lista

b = list(a)  # crea una nuova lista, inizializzata con riferimenti (alias) ai singoli elementi della prima lista
b = a[:]     # anche questo fa la stessa cosa

print(a)
print(b)

b.append(7)

b = b + [7]

print(a)
print(b)