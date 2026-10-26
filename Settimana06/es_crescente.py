numeri = [ 0.2, 1.5, 5.0, -7.1, 10.0 ]

crescente = True
for i in range(1, len(numeri)):
    if numeri[i] <= numeri[i-1]:
        crescente = False

if crescente:
    print("Lista crescente")
else:
    print("Lista non crescente")