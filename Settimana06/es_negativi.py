import random

# numeri = []

# for i in range(5):
#     n = int(input("Numero: "))
#     numeri.append(n)

# print(numeri)

# numeri = [4, 3, -3, 0, 2]

numeri = []

for i in range(5):
    n = random.randint(-10, 10)
    numeri.append(n)

print(numeri)

#---------------

negativi = False
n_negativi = 0
for v in numeri:
    if v<0:
        negativi = True
        n_negativi = n_negativi + 1

if negativi:  #  n_negativi>0
    print("Ci sono dei negativi", n_negativi)
else:
    print("Nessun negativo")